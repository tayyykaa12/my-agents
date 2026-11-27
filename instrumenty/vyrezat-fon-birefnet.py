import sys, numpy as np, onnxruntime as ort
from PIL import Image, ImageFilter
m=sys.argv[1]; sess=ort.InferenceSession(m,providers=['CPUExecutionProvider'])
inp=sess.get_inputs()[0].name
for src,dst in zip(sys.argv[2::2],sys.argv[3::2]):
    im=Image.open(src).convert('RGB'); W,H=im.size
    x=np.asarray(im.resize((1024,1024),Image.BILINEAR),dtype=np.float32)/255.
    x=(x-[0.485,0.456,0.406])/[0.229,0.224,0.225]
    x=x.transpose(2,0,1)[None].astype(np.float32)
    out=sess.run(None,{inp:x})[-1][0,0]
    out=1/(1+np.exp(-out)) if out.min()<0 or out.max()>1 else out
    a=Image.fromarray((np.clip(out,0,1)*255).astype(np.uint8)).resize((W,H),Image.BILINEAR)
    im=im.convert('RGBA'); im.putalpha(a)
    bb=a.point(lambda v:255 if v>20 else 0).getbbox(); im=im.crop(bb) if bb else im
    im.save(dst); print(dst, im.size)
