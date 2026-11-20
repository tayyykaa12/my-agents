"""Убрать фон с картинки.

logo:   однотонный фон (берётся из верхних строк), края пересчитываются, есть вариант для светлого фона.
        python3 instrumenty/ubrat-fon.py logo vhod.jpg vyhod.png vyhod-dlya-svetlogo.png 3
mascot: белый фон вокруг персонажа или предмета.
        python3 instrumenty/ubrat-fon.py mascot vhod.jpg vyhod.png
"""
import sys, numpy as np
from PIL import Image

def dilate(m, r=1):
    o = m.copy()
    for dy in range(-r, r + 1):
        for dx in range(-r, r + 1):
            o |= np.roll(np.roll(m, dy, 0), dx, 1)
    return o

def logo(src, out_dark, out_light, scale):
    im = Image.open(src).convert('RGB')
    im = im.resize((im.width * scale, im.height * scale), Image.LANCZOS)
    p = np.asarray(im).astype(np.float64)
    bg = np.median(p[:10].reshape(-1, 3), axis=0)
    d = np.sqrt(((p - bg) ** 2).sum(2))
    a = np.clip((d - 25) / 70, 0, 1)
    f = np.where(a[..., None] > 0, (p - (1 - a[..., None]) * bg) / np.maximum(a[..., None], 1e-6), 0)
    f = np.clip(f, 0, 255)
    o = Image.fromarray(np.dstack([f, a * 255]).astype(np.uint8), 'RGBA')
    o = o.crop(o.getbbox()); o.save(out_dark)
    arr = np.asarray(o).astype(np.float64)
    c = arr[..., :3]; sat = c.max(2) - c.min(2)
    white = (sat < 45) & (c.mean(2) > 140)
    arr[white, :3] = bg
    Image.fromarray(arr.astype(np.uint8), 'RGBA').save(out_light)

def mascot(src, out, thr=232, scale=2):
    im = Image.open(src).convert('RGB')
    p = np.asarray(im).astype(np.float64)
    near_white = p.min(2) >= thr
    seed = np.zeros_like(near_white); seed[0, :] = seed[-1, :] = seed[:, 0] = seed[:, -1] = True
    bgm = seed & near_white
    while True:
        n = dilate(bgm) & near_white
        if n.sum() == bgm.sum(): break
        bgm = n
    alpha = np.where(bgm, 0.0, 1.0)
    band = dilate(bgm, 2) & ~bgm
    lum = p.mean(2)
    alpha[band] = np.clip((215 - lum[band]) / 50, 0, 1)
    from PIL import ImageFilter
    alpha = np.asarray(Image.fromarray((alpha*255).astype(np.uint8)).filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(0.7))).astype(np.float64)/255
    alpha[bgm & ~dilate(~bgm,1)] = 0
    o = Image.fromarray(np.dstack([p, alpha * 255]).astype(np.uint8), 'RGBA')
    o = o.crop(o.getbbox())
    o.resize((o.width * scale, o.height * scale), Image.LANCZOS).save(out)

if __name__ == '__main__':
    if sys.argv[1] == 'logo': logo(sys.argv[2], sys.argv[3], sys.argv[4], int(sys.argv[5]))
    else: mascot(sys.argv[2], sys.argv[3])
