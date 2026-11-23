import json,re,sys,os
D=os.path.dirname(os.path.abspath(__file__))
def acc(t): return re.sub(r'\*(.+?)\*',r'<span class="r">\1</span>',t)
CSS='''
@import url('https://fonts.googleapis.com/css2?family=Oswald:wght@500;600;700&family=Montserrat:wght@500;600;700;800&display=swap');
*{margin:0;padding:0;box-sizing:border-box}body{background:#333}
.s{width:1080px;height:1350px;position:relative;overflow:hidden;background:#0A0A0A;color:#fff;font-family:Montserrat,sans-serif;margin:10px}
.glow{position:absolute;inset:0;background:radial-gradient(circle at 100% 0%,#5C0A0Dcc 0,transparent 55%),radial-gradient(circle at 0% 100%,#5C0A0D88 0,transparent 45%)}
.slash{position:absolute;width:260px;height:1700px;background:linear-gradient(#E1141B,#A50E14);transform:rotate(24deg);right:-170px;top:-200px;opacity:.95}
.slash2{position:absolute;width:40px;height:1700px;background:#E1141B;transform:rotate(24deg);right:130px;top:-200px;opacity:.9}
.num{position:absolute;right:72px;top:64px;font:700 26px Montserrat;color:#B3B3B3;letter-spacing:3px;z-index:5}
.nick{position:absolute;left:72px;bottom:60px;font:600 24px Montserrat;color:#B3B3B3;z-index:5}
.wrap{position:absolute;left:72px;right:72px;top:140px;bottom:140px;z-index:4;display:flex;flex-direction:column;justify-content:center;align-items:flex-start}
.wrap.t{bottom:auto;justify-content:flex-start}
.label{font:700 24px Montserrat;color:#fff;background:#E1141B;display:inline-block;padding:10px 18px;letter-spacing:2px;margin-bottom:28px}
h1{font:700 104px/0.98 Oswald;text-transform:uppercase}
h2{font:700 122px/1 Oswald;text-transform:uppercase}
.r{color:#E1141B}
.body{font:500 44px/1.4 Montserrat;color:#fff;margin-top:44px}
.card{background:#161616;border-left:12px solid #E1141B;padding:48px 52px;margin-top:64px;font:500 48px/1.42 Montserrat;align-self:stretch}
.card b{font-weight:800}
.muted{color:#B3B3B3}
.pill{position:absolute;right:72px;bottom:52px;border:2px solid #fff;border-radius:999px;padding:14px 30px;font:700 26px Montserrat;letter-spacing:2px;z-index:6;background:#0A0A0Acc}
.bog{position:absolute;z-index:3}
.big{font:700 330px/0.8 Oswald;color:#E1141B;position:absolute;right:60px;bottom:120px;opacity:.18;z-index:1}
.chips{display:flex;flex-direction:column;gap:30px;margin-top:70px;align-self:stretch}
.chip{background:#161616;border:2px solid #2E2E2E;padding:30px 40px;font:700 54px Montserrat;align-self:flex-start}
.chip:nth-child(2){align-self:center;border-color:#E1141B}.chip:nth-child(3){align-self:flex-end}
.ribbon{background:linear-gradient(90deg,#E1141B,#A50E14);display:inline-block;padding:6px 30px 14px;font:700 180px/1 Oswald;margin-top:24px}
.li{display:flex;gap:32px;align-items:center;margin-top:44px;font:600 52px/1.3 Montserrat}
.ic{flex:0 0 84px;height:84px;background:#E1141B;display:flex;align-items:center;justify-content:center;font:700 44px Montserrat}
.ic.x{background:#161616;border:3px solid #E1141B;color:#E1141B}
.price{margin-top:40px;display:flex;align-items:baseline;gap:30px}
.price .n{font:700 170px/1 Oswald}.price .o{font:600 64px Oswald;color:#B3B3B3;text-decoration:line-through;text-decoration-color:#E1141B;text-decoration-thickness:6px}
.photo{position:absolute;inset:0;background-size:cover;background-position:center;opacity:.55;filter:grayscale(.3)}
.fade{position:absolute;inset:0;background:linear-gradient(180deg,#0A0A0Aee 20%,#0A0A0Abb 60%,#0A0A0A55)}
'''
def S(id,inner,n,deco='glow',nick=True,pill=False):
    d={'glow':'<div class="glow"></div>','slash':'<div class="glow"></div><div class="slash"></div><div class="slash2"></div>'}.get(deco,deco)
    return f'<div class="s" id="{id}">{d}<div class="num">{n:02d} / 08</div>{inner}'+('<div class="nick">@konoplyanik2.0</div>' if nick else '')+('<div class="pill">ГОРТАЙ →</div>' if pill else '')+'</div>'
bog='<img class="bog" src="bogdan.png" style="{}">'
def text(id,n,h,b,extra='',deco='glow',bigtxt=''):
    return S(id,(f'<div class="big">{bigtxt}</div>' if bigtxt else '')+f'<div class="wrap"><h2>{acc(h)}</h2>{extra}<div class="card">{b}</div></div>',n,deco)
K=[]
# ---- Карусель 1
K.append(S('k1-1','<div class="slash"></div><div class="slash2"></div>'+bog.format('width:700px;right:-90px;bottom:0')+
 '<div class="wrap t" style="top:130px;right:300px"><div class="label">▸ ЧЕСНО ПРО ХАРЧУВАННЯ</div><h1 style="font-size:96px">ХЛІБ ПРИБРАТИ, ЖИРИ СКОРОТИТИ…</h1><h1 style="font-size:116px;margin-top:20px">А ЩО <span class="r">ТОДІ</span> ЇСТИ?</h1><div class="body muted" style="font-size:32px;margin-top:34px;max-width:470px">Чесно розкладаю, чому поради різні й що з цим робити.</div></div>',1,pill=True))
K.append(S('k1-2','<div class="wrap"><h2>УСІ РАДЯТЬ <span class="r">РІЗНЕ</span></h2><div class="chips"><div class="chip">«Не їж хліб»</div><div class="chip">«Не бійся хліба»</div><div class="chip">«Тільки білок»</div></div><div class="body" style="margin-top:70px;font-size:56px;font-weight:800">Знайомо?</div></div>',2,'slash'))
K.append(text('k1-3',3,'ЧОМУ ТАК *ВИХОДИТЬ*','Кожна порада написана <b>для чиєїсь цілі</b> та чиїхось обставин.<br><br>До тебе доходить лише <b>гучний заголовок</b>.'))
qs=[('ДЛЯ КОГО','Хто це радить і для якої цілі?<br><br>Те, що підійшло комусь, <b>не мусить підійти тобі</b>.'),('ЧОМУ ТАК','Чи є пояснення, як це працює?<br><br>Без пояснення це <b>не порада, а лозунг</b>.'),('ЗАБОРОНА ЧИ СИСТЕМА','Список «не можна» не каже, що їсти.<br><br><b>Раціон — це не список заборон.</b>')]
for i,(h,b) in enumerate(qs):
    K.append(S(f'k1-{4+i}',f'<div class="big">{i+1}</div><div class="wrap"><div class="label">ПИТАННЯ {i+1}/3</div><h2>{"<span class=r>"+h+"</span>" if i<2 else "ЗАБОРОНА ЧИ <span class=r>СИСТЕМА</span>"}?</h2><div class="card">{b}</div></div>',4+i))
K.append(S('k1-7','<div class="photo" style="background-image:url(tarelka.jpg)"></div><div class="fade"></div><div class="wrap"><h2>БРАКУЄ НЕ ПОРАД, А <span class="r">ПОРЯДКУ</span></h2><div class="card"><b>Школа харчування:</b> 14 днів текстових лекцій українською.<br><br><span class="muted">Це навчання, а не дієта і не персональний раціон.</span></div></div>',7,'<div></div>'))
cta=lambda id,extra: S(id,'<div class="slash"></div><div class="slash2"></div>'+bog.format('width:480px;right:-60px;bottom:0')+f'<div class="wrap t" style="top:150px;right:420px"><h2 style="font-size:84px">ПИШИ В DIRECT<br>СЛОВО</h2><div class="ribbon">ШКОЛА</div>{extra}</div>',8)
K.append(cta('k1-8','<div class="body" style="font-size:38px">Напиши слово — і я розповім програму та умови.</div>'))
# ---- Карусель 2
K.append(S('k2-1','<div class="slash"></div><div class="slash2"></div>'+bog.format('width:700px;right:-90px;bottom:0')+
 '<div class="wrap t" style="top:130px;right:300px"><div class="label">▸ ЧЕСНО ПРО НАВЧАННЯ</div><h1 style="font-size:112px">ЩО Є, А ЧОГО <span class="r">НЕМАЄ</span></h1><h1 style="font-size:84px;margin-top:18px">У ШКОЛІ ХАРЧУВАННЯ</h1><div class="body muted" style="font-size:32px;margin-top:34px;max-width:470px">Що всередині: відео, куратор чи просто файли? Без прикрас.</div></div>',1,pill=True))
yes=[('*14 ДНІВ* У ЗРУЧНИЙ ЧАС','Онлайн-навчання. Опрацьовуєш матеріали <b>самостійно</b>, без постійних онлайн-зустрічей.'),
('ТЕКСТОВІ *ЛЕКЦІЇ*','<b>Українською.</b> Білки, жири та вуглеводи, вітаміни й мінерали, різні джерела білка.'),
('ТЕСТИ ТА *ПП‑РЕЦЕПТИ*','Перевірка засвоєних знань і <b>ПП-рецепти</b>, щоб знання лягли в тарілку.'),
('ДОСТУП *НАЗАВЖДИ*','Починаєш <b>у будь-який день</b>.<br><br>Після проходження — сертифікат <span class="muted">(він не підтверджує професійну кваліфікацію)</span>.')]
for i,(h,b) in enumerate(yes):
    K.append(S(f'k2-{2+i}',f'<div class="wrap"><div class="label">✓ ЩО Є</div><h2>{acc(h)}</h2><div class="card">{b}</div></div>',2+i,'slash' if i%2 else 'glow'))
K.append(S('k2-6','<div class="wrap"><div class="label" style="background:#161616;border:2px solid #E1141B">✕ ЧЕСНІ МЕЖІ</div><h2>ЧОГО <span class="r">НЕМАЄ</span></h2>'+''.join(f'<div class="li"><div class="ic x">✕</div><div>{t}</div></div>' for t in ['Відео й записів лекцій','Особистого супроводу','Дієти чи персонального раціону'])+'</div>',6))
K.append(text('k2-7',7,'А В ІНТЕРНЕТІ *БЕЗКОШТОВНО*?','Окремі факти — так.<br><br>Школа збирає <b>основи харчування в один порядок</b> на 14 днів.',deco='slash'))
K.append(cta('k2-8','<div class="price"><div class="n">999 <span style="font-size:80px">грн</span></div><div class="o">1999</div></div><div class="body" style="font-size:36px;margin-top:10px">до 30 листопада включно, далі 1999 грн.<br>Напиши слово — і я розповім детальніше.</div>'))
open(D+'/k.html','w').write(f'<html><head><meta charset="utf-8"><style>{CSS}</style></head><body>'+''.join(K)+'</body></html>')
ids=re.findall(r'id="(k\d-\d)"',''.join(K)); json.dump(ids,open(D+'/ids.json','w')); print(ids)
