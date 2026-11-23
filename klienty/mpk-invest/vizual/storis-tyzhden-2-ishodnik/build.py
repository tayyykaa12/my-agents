import json
CSS='''<!doctype html><html lang="uk"><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@700&family=Montserrat:wght@500;600;800&display=block" rel="stylesheet">
<style>*{margin:0;padding:0;box-sizing:border-box}body{background:#444}
.s{position:relative;width:1080px;height:1920px;overflow:hidden;background:#1C1C1C;color:#fff;font-family:Montserrat}
.tex{position:absolute;inset:0;background:url(gravel.jpg) center/cover;filter:grayscale(1) brightness(.7)}
.sh{position:absolute;inset:0;background:linear-gradient(180deg,rgba(28,28,28,.6),rgba(28,28,28,.92) 60%,#1C1C1C)}
.flat{position:absolute;inset:0;background:radial-gradient(120% 70% at 85% 0%,#2a2a2a 0%,#1C1C1C 55%,#151515 100%)}
.edge{position:absolute;left:0;right:0;bottom:0;height:520px;background:url(gravel.jpg) center/cover;filter:grayscale(1) brightness(.45);-webkit-mask-image:linear-gradient(to top,rgba(0,0,0,.7),transparent)}
.logo{position:absolute;left:80px;top:250px;width:250px}
.h{font-family:Oswald;font-weight:700;text-transform:uppercase;line-height:1}
.o{color:#F28C1E}
.label{font-weight:600;font-size:28px;letter-spacing:.22em;text-transform:uppercase;color:#A6A6A6}
.body{font-weight:500;font-size:46px;line-height:1.4;color:#E4E4E2}
.plate{display:inline-block;background:#E4E4E2;color:#1C1C1C;font-family:Oswald;font-weight:700;font-size:56px;padding:16px 28px;line-height:1.15;margin:10px 0}
.box{position:absolute;left:110px;right:110px;border:4px dashed #5A5A5A;border-radius:26px;display:flex;align-items:center;justify-content:center;font:600 32px Montserrat;color:#777;text-align:center;padding:20px}
.shch{position:absolute;z-index:2}
.bubble{background:#2E2E2E;border-left:10px solid #F28C1E;padding:34px 40px;font:600 46px/1.35 Montserrat}
.card{position:absolute;width:640px;left:220px;box-shadow:0 30px 80px rgba(0,0,0,.6);transform:rotate(-3deg);border:6px solid #2E2E2E}
.cta{position:absolute;left:80px;right:80px}
.ph{font-weight:800;font-size:68px;line-height:1.35}
.site{font-weight:800;font-size:56px;color:#F28C1E;margin-top:20px}
.step{font-family:Oswald;font-weight:700;font-size:200px;color:#F28C1E;line-height:.9}
.list div{font-family:Oswald;font-weight:700;font-size:84px;text-transform:uppercase;display:flex;align-items:center;gap:30px;margin:26px 0}
.list i{width:70px;height:70px;border:5px solid #F28C1E;border-radius:10px;flex:none}
.list .w{color:#F28C1E}
</style></head><body>'''
S=[]
def add(id,inner,bg='flat',sticker=None):
    b={'flat':'<div class="flat"></div><div class="edge"></div>','tex':'<div class="tex"></div><div class="sh"></div>'}[bg]
    st=(f'<div class="box" style="top:{sticker[0]}px;height:{sticker[1]}px;right:{sticker[3] if len(sticker)>3 else 110}px">{sticker[2]}</div>') if sticker else ''
    S.append((id,f'<div class="s" id="{id}">{b}{inner}{st}</div>',bool(sticker)))
LOGO='<img class="logo" src="logo.png">'
def cta(top=1050,title='Замовте <span class="o">доставку</span>'):
    return f'<div class="cta" style="top:{top}px"><div class="h" style="font-size:140px">{title}</div><div style="height:50px"></div><div class="ph">050 010 66 25</div><div class="ph">050 444 45 21</div><div class="site">mpc-invest.com.ua</div></div>'
SH=lambda st: f'<img class="shch" src="shch.png" style="{st}">'
def T(top,html,right=80): return f'<div style="position:absolute;left:80px;right:{right}px;top:{top}px">{html}</div>'
# 23.11
add('23-1',LOGO+T(470,'<div class="label">НОВА КАРУСЕЛЬ</div><div class="h" style="font-size:140px;margin-top:24px">СКІЛЬКИ ЩЕБЕНЮ <span class="o">ЗАМОВЛЯТИ?</span></div><div class="body" style="margin-top:30px">Рахуємо за 4 кроки. Карусель у стрічці →</div>')+'<img class="card" src="k4.png" style="top:1080px;width:560px;left:260px">','tex')
add('23-2',T(330,'<div class="label">ФОРМУЛА</div><div class="h" style="font-size:118px;margin-top:24px">ОБ\'ЄМ × ЩІЛЬНІСТЬ = <span class="o">ТОННИ</span></div><div class="body" style="margin-top:34px;font-size:40px;color:#A6A6A6">Щільність залежить від фракції. Перед розрахунком уточніть її для вашої фракції.</div>'),'flat',(1080,560,'місце під стикер «Вікторина»<br>«Що множимо на щільність, щоб отримати тонни?»'))
add('23-3',LOGO+cta())
# 24.11 1Б
add('24-1',LOGO+T(470,'<div class="label">ПИТАННЯ ДО ЩЕБІНЬЧИКА</div><div class="h" style="font-size:124px;margin-top:24px">ПРОРАБУ ЧИ <span class="o">ЗАКУПІВЕЛЬНИКУ</span></div><div class="body" style="margin-top:30px">Ось 4 відповіді від Щебіньчика.</div>')+SH('width:640px;left:220px;bottom:180px'),'tex')
add('24-2',T(300,'<div class="label">ПИТАННЯ 1</div><div class="h" style="font-size:110px;margin-top:20px">ЯКІ ФРАКЦІЇ <span class="o">ЩЕБЕНЮ</span> Є?</div><div style="margin-top:44px"><div class="plate">ГРАНІТНИЙ ЩЕБІНЬ</div><div class="body" style="margin:10px 0 24px">5–10 · 5–20 · 10–20 · 20–40 · 40–70 мм</div><div class="plate">ЩПС</div><div class="body" style="margin:10px 0 24px">0–40 · 0–70 мм</div><div class="plate">ПІСОК З ВІДСІВІВ</div></div>')+SH('width:420px;right:20px;bottom:200px'))
add('24-3',T(300,'<div class="label">ПИТАННЯ 2</div><div class="h" style="font-size:110px;margin-top:20px">А СКІЛЬКИ МОЖНА <span class="o">ЗАМОВИТИ?</span></div><div class="bubble" style="margin-top:44px">Об\'єми: від мішка до самоскида.</div>')+SH('width:380px;right:30px;bottom:230px'),'tex',(1020,420,'місце під стикер «Опитування»<br>«Що вам частіше потрібно?» Щебінь / Пісок',420))
add('24-4',T(300,'<div class="label">ПИТАННЯ 3</div><div class="h" style="font-size:110px;margin-top:20px">А ЩО ВИ <span class="o">ОБІЦЯЄТЕ?</span></div><div class="bubble" style="margin-top:44px">Привеземо вчасно, щоб майстри не чекали.</div><div class="bubble" style="margin-top:24px">Гарантія точної ваги.</div>')+SH('width:360px;right:30px;bottom:230px'),'flat',(1180,360,'місце під стикер «Питання»<br>«Що ще спитати у Щебіньчика?»',420))
add('24-5',LOGO+T(470,'<div class="label">ПИТАННЯ 4</div><div class="h" style="font-size:110px;margin-top:20px">ЯК <span class="o">ЗАМОВИТИ?</span></div><div class="body" style="margin-top:24px">Телефоном або на сайті.</div>',380)+cta(1000)+SH('width:360px;right:20px;top:330px'))
# 25.11
add('25-1',LOGO+T(470,'<div class="label">НОВА КАРУСЕЛЬ</div><div class="h" style="font-size:120px;margin-top:24px">ЯК ЗАМОВИТИ ЩЕБІНЬ: <span class="o">ВІД ЗАЯВКИ ДО ДОСТАВКИ</span></div><div class="body" style="margin-top:28px;font-size:40px">Вперше замовляєте щебінь? Ось шлях від заявки до доставки. Чотири кроки, карусель у стрічці →</div>')+'<img class="card" src="k5.png" style="top:1240px;width:470px;left:300px">','tex')
add('25-2',T(360,'<div class="bubble" style="font-size:64px">Щебіньчик: це зрозуміло?</div>')+SH('width:600px;left:240px;bottom:200px'),'flat',(640,380,'місце під стикер «Слайдер» 👍<br>«Наскільки зрозумілі чотири кроки?»'))
add('25-3',LOGO+cta())
# 26.11 2Б
add('26-1',LOGO+T(470,'<div class="label">ШЛЯХ ЗАМОВЛЕННЯ</div><div class="h" style="font-size:118px;margin-top:24px">З ЧОГО ПОЧАТИ, ЩОБ ЗАМОВИТИ <span class="o">ЩЕБІНЬ?</span></div><div class="body" style="margin-top:28px">4 кроки від заявки до доставки.</div>')+SH('width:560px;left:260px;bottom:170px'),'tex')
add('26-2',T(300,'<div class="step">1</div><div class="h" style="font-size:120px">ЗАЯВКА</div><div class="body" style="margin-top:24px">Подзвоніть або залиште заявку на сайті.</div><div class="bubble" style="margin-top:36px;max-width:620px">Скажи, що потрібно.</div>')+SH('width:360px;right:20px;top:760px'),'flat',(1250,360,'місце під стикер «Опитування»<br>«Як вам зручніше?» Дзвінок / Сайт'))
add('26-3',T(300,'<div class="step">2</div><div class="h" style="font-size:120px">ФРАКЦІЯ <span class="o">Й ОБ\'ЄМ</span></div><div style="margin-top:44px"><div class="plate">ЩЕБІНЬ</div> <div class="plate">ЩПС</div> <div class="plate">ПІСОК</div></div><div class="body" style="margin-top:36px">Об\'єми: від мішка до самоскида.</div>'),'tex')
add('26-4',T(300,'<div class="step">3</div><div class="h" style="font-size:120px">ДОСТАВКА</div><div class="bubble" style="margin-top:40px">Привеземо вчасно, щоб майстри не чекали.</div>')+SH('width:360px;right:20px;top:820px'),'flat',(1250,360,'місце під стикер «Питання»<br>«Який етап замовлення розібрати детальніше?»'))
add('26-5',LOGO+T(470,'<div class="step" style="font-size:150px">4</div><div class="h" style="font-size:104px">ГАРАНТІЯ <span class="o">ТОЧНОЇ ВАГИ</span></div>',380)+cta(1060)+SH('width:340px;right:20px;top:330px'))
# 27.11
add('27-1',LOGO+T(470,'<div class="label">НОВА КАРУСЕЛЬ</div><div class="h" style="font-size:130px;margin-top:24px">4 ПЕРЕВІРКИ ПРИ <span class="o">РОЗВАНТАЖЕННІ</span></div><div class="body" style="margin-top:28px">Фракція → домішки → вага → документи. Карусель у стрічці →</div>')+'<img class="card" src="k6.png" style="top:1160px;width:520px;left:280px">','tex')
add('27-2',T(330,'<div class="label">ЧЕК-ЛИСТ ПРОРАБА</div><div class="list" style="margin-top:30px"><div><i></i>Фракція</div><div><i></i>Чистота і домішки</div><div class="w"><i></i>Вага</div><div><i></i>Документи</div></div>'),'flat',(1180,380,'місце під стикер «Слайдер» 👍<br>«Як часто ви перевіряєте всі 4 пункти?»'))
add('27-3',LOGO+T(620,'<div class="h" style="font-size:170px">НАДІШЛІТЬ <span class="o">ПРОРАБУ</span></div><div class="body" style="margin-top:40px">Перешліть карусель «4 перевірки при розвантаженні» тому, хто приймає щебінь на об\'єкті.</div><div class="h o" style="font-size:150px;margin-top:40px">→</div>'),'tex')
# 29.11
add('29-1',LOGO+T(470,'<div class="h" style="font-size:112px">ЩО ВАМ КОРИСНІШЕ: <span class="o">ВІДЕО</span> ЧИ КАРТКИ-ШПАРГАЛКИ?</div><div class="body" style="margin-top:28px;color:#A6A6A6;font-size:40px">Дякуємо, що ви з нами цього тижня.</div>')+SH('width:330px;right:40px;bottom:220px'),'flat',(1130,400,'місце під стикер «Опитування»<br>«Що вам корисніше?» Короткі відео / Картки-шпаргалки',400))
add('29-2',LOGO+T(720,'<div class="h" style="font-size:150px">ПИТАННЯ ПРО ЩЕБІНЬ?</div><div class="h" style="font-size:150px;margin-top:20px"><span class="o">ПИШІТЬ У ДИРЕКТ →</span></div>'),'tex')
open('s.html','w').write(CSS+''.join(h for _,h,_ in S)+'</body></html>')
json.dump([[i,st] for i,_,st in S],open('ids.json','w'))
