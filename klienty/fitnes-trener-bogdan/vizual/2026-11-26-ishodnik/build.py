import json,re
def acc(t): return re.sub(r'\*(.+?)\*',r'<span class="r">\1</span>',t)
CSS='''<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@600;700&family=Montserrat:wght@500;600;700;800&display=block" rel="stylesheet">
<style>*{margin:0;padding:0;box-sizing:border-box}body{background:#333}
.s{position:relative;overflow:hidden;background:#0A0A0A;color:#fff;font-family:Montserrat;margin:10px}
.k{width:1080px;height:1350px}.st{width:1080px;height:1920px}
.ph{position:absolute;inset:0;background-size:cover;background-position:center}
.gb{position:absolute;inset:0;background:linear-gradient(180deg,rgba(10,10,10,0) 30%,rgba(10,10,10,.85) 62%,#0A0A0A 82%)}
.gt{position:absolute;inset:0;background:linear-gradient(0deg,rgba(10,10,10,0) 35%,rgba(10,10,10,.85) 62%,#0A0A0A 80%)}
.glow{position:absolute;inset:0;background:radial-gradient(circle at 100% 0%,#5C0A0Dcc 0,transparent 55%),radial-gradient(circle at 0% 100%,#5C0A0D88 0,transparent 45%)}
.slash{position:absolute;width:240px;height:2400px;background:linear-gradient(#E1141B,#A50E14);transform:rotate(24deg);right:-170px;top:-300px}
.slash2{position:absolute;width:36px;height:2400px;background:#E1141B;transform:rotate(24deg);right:120px;top:-300px}
.num{position:absolute;right:72px;top:64px;font:700 26px Montserrat;color:#B3B3B3;letter-spacing:3px;z-index:5}
.nick{position:absolute;left:72px;bottom:56px;font:600 24px Montserrat;color:#B3B3B3;z-index:5}
.wrap{position:absolute;left:72px;right:72px;z-index:4}
.mid{top:150px;bottom:150px;display:flex;flex-direction:column;justify-content:center}
.label{font:700 24px Montserrat;color:#fff;background:#E1141B;display:inline-block;padding:10px 18px;letter-spacing:2px;align-self:flex-start}
h1{font:700 104px/1 Oswald;text-transform:uppercase}
h2{font:700 100px/1.02 Oswald;text-transform:uppercase}
.r{color:#E1141B}
.body{font:500 44px/1.42 Montserrat;margin-top:36px}
.card{background:#161616;border-left:12px solid #E1141B;padding:44px 48px;margin-top:56px;font:500 44px/1.45 Montserrat}
.card b{font-weight:800}
.muted{color:#B3B3B3}
.pill{position:absolute;right:72px;bottom:48px;border:2px solid #fff;border-radius:999px;padding:14px 30px;font:700 26px Montserrat;letter-spacing:2px;z-index:6;background:#0A0A0Acc}
.chips{display:flex;flex-direction:column;gap:22px;margin-top:50px}
.chip{background:#161616;border:2px solid #2E2E2E;padding:26px 34px;font:700 44px/1.3 Montserrat}
.chip.red{border-color:#E1141B}
.qs div{display:flex;gap:26px;align-items:flex-start;font:600 44px/1.35 Montserrat;margin-top:34px}
.qs i{flex:0 0 72px;height:72px;background:#E1141B;font:700 44px/72px Oswald;text-align:center;font-style:normal}
.list div{font:600 48px/1.3 Montserrat;margin-top:28px;padding-left:44px;position:relative}
.list div:before{content:"▸";color:#E1141B;position:absolute;left:0}
.box{position:absolute;left:110px;right:110px;border:4px dashed #5A5A5A;border-radius:26px;display:flex;align-items:center;justify-content:center;font:600 32px Montserrat;color:#999;text-align:center;z-index:8}
</style></head><body>'''
S=[]
def K(id,inner,n,bg=''): S.append((id,f'<div class="s k" id="{id}">{bg}<div class="num">{n:02d} / 09</div>{inner}<div class="nick">@konoplyanik2.0</div></div>',False))
G='<div class="glow"></div>'; SL=G+'<div class="slash"></div><div class="slash2"></div>'
def ph(f,pos='center',g='gb'): return f'<div class="ph" style="background-image:url({f}.jpg);background-position:{pos}"></div><div class="{g}"></div>'
# carousel
K('k1',ph('03-kurtka-park-pohliad-v-kameru','50% 20%')+'<div class="wrap" style="bottom:150px"><h1 style="font-size:100px">НАЙБІЛЬША ПОМИЛКА ДІВЧАТ — ДУМАТИ, ЩО ЇМ БРАКУЄ <span class="r">ІНФОРМАЦІЇ</span></h1><div class="body muted" style="font-size:34px;margin-top:24px">Усе є в інтернеті. Ось 4 причини, чому все одно не виходить, і що реально працює.</div></div><div class="pill">ГОРТАЙ →</div>',1)
txt=[('ЗНАННЯ НЕ ЛЕЖАТЬ У *ХОЛОДИЛЬНИКУ*','ПРИЧИНА 1','Прочитала 20 статей про білок, а в холодильнику — <b>сирки, ковбаса й батон</b>.<br><br>Що буде на вечерю, вирішує те, що лежить на полиці о 19:30, а не вкладка в браузері.'),
('ПОРАДИ *СУПЕРЕЧАТЬ* ОДНА ОДНІЙ','ПРИЧИНА 2',None),
('МЕНЮ НА МІСЯЦЬ ЛАМАЄТЬСЯ В *СЕРЕДУ*','ПРИЧИНА 3','Інтернет дає план на 30 днів із п’ятьма прийомами їжі. У середу затрималась на роботі, з’їла піцу в офісі — і <b>«почну з понеділка»</b>.<br><br>Запасного варіанта немає, тому один вечір валить увесь місяць.'),
('*СТАТТЯ* НЕ БАЧИТЬ ТВОЮ ТАРІЛКУ','ПРИЧИНА 4','Ти впевнена, що снідаєш із білком: два яйця й кава. Це <b>12–13 г білка</b> — менше, ніж половина пачки кисломолочного сиру.<br><br>Жодна стаття не покаже, де твоє «знаю» розходиться з тарілкою.')]
for i,(h,l,b) in enumerate(txt):
    if b is None:
        inner=f'<div class="wrap mid"><h2>{acc(h)}</h2><div class="chips"><div class="chip"><span class="muted" style="font-size:30px">ЗРАНКУ В СТРІЧЦІ:</span><br>«Сніданок — найважливіший прийом їжі»</div><div class="chip red"><span class="muted" style="font-size:30px">УВЕЧЕРІ:</span><br>«Пропускай сніданок, інтервальне голодування 16/8»</div></div><div class="body">Без фільтра ти робиш те, що <b>побачила останнім</b>.</div></div>'
    else:
        inner=f'<div class="wrap mid"><h2>{acc(h)}</h2><div class="card">{b}</div></div>'
    K(f'k{i+2}',inner,i+2,SL if i%2 else G)
K('k6','<div class="wrap mid"><h2><span class="r">ФІЛЬТР</span> ІЗ ТРЬОХ ПИТАНЬ</h2><div class="qs"><div><i>1</i><span>Чи зможу я так у звичайний вівторок?</span></div><div><i>2</i><span>Чи куплю це в магазині біля дому?</span></div><div><i>3</i><span>Чи немає в ній заборони назавжди?</span></div></div><div class="body">Хоч одне «ні» — <b>гортай далі</b>.</div></div>',6,G)
K('k7','<div class="wrap mid"><h2>ПЛАН НА ОДИН <span class="r">ВЕЧІР</span></h2><div class="chips"><div class="chip"><span class="r" style="font-family:Oswald;font-size:64px">13:00</span><br>Вирішуєш, що буде на вечерю, і перевіряєш, чи це є вдома.</div><div class="chip red"><span class="r" style="font-family:Oswald;font-size:64px">19:00</span><br>Не вибираєш голодною біля холодильника — просто готуєш.</div></div></div>',7,SL)
K('k8',ph('11-yizha-svynyna-na-skovorodi','50% 60%','gt')+'<div class="wrap" style="top:130px"><h2>ТРИ <span class="r">ЗАПАСНІ</span> ВЕЧЕРІ</h2><div class="list"><div>Омлет з овочами</div><div>Паста з тунцем і помідорами</div><div>Гречка з куркою з учорашнього</div></div><div class="body" style="font-size:36px">По 15 хвилин. План зірвався — береш одну з трьох замість доставки.</div></div>',8)
K('k9',ph('04-kurtka-cegla-ok-zhest-usmishka','50% 25%')+'<div class="wrap" style="bottom:140px"><h1 style="font-size:96px">ЯКА ТВОЯ <span class="r">ВЕЧЕРЯ</span> НА 15 ХВИЛИН?</h1><div class="body" style="font-size:38px;margin-top:24px">Напиши в коментарях, що готуєш, коли план зірвався. Під цим постом збереться готовий список вечерь на будь-який вечір.</div></div>',9)
# stories
def phb(f,top,pos='50% 0%'):
    return f'<div class="glow"></div><div class="ph" style="background-image:url({f}.jpg);top:{top}px;background-position:{pos}"></div><div style="position:absolute;left:0;right:0;top:{top}px;height:260px;background:linear-gradient(180deg,#0A0A0A,rgba(10,10,10,0))"></div>'
def ST(id,inner,bg,sticker=None):
    st=f'<div class="box" style="top:{sticker[0]}px;height:{sticker[1]}px">{sticker[2]}</div>' if sticker else ''
    S.append((id,f'<div class="s st" id="{id}">{bg}{inner}{st}<div class="nick" style="bottom:240px">@konoplyanik2.0</div></div>',bool(sticker)))
ST('s1','<div class="wrap" style="top:250px"><h1 style="font-size:88px">ДУМАЄШ, ТРЕНЕР ЗАВЖДИ БУВ У ФОРМІ?</h1><h1 style="font-size:118px;margin-top:20px">Я ВАЖИВ <span class="r">135 КГ</span></h1><div class="body" style="font-size:40px;margin-top:20px">Зараз — на 30+ кг менше. Я Богдан.</div></div>',phb('09-svetr-cegla-znyzu-geroyichno',820,'50% 15%'))
ST('s2','<div class="wrap" style="top:250px"><h1 style="font-size:104px">8 РОКІВ ТРЕНЕРОМ.<br><span class="r">1000+</span> КЛІЄНТІВ.</h1><div class="body" style="font-size:38px;margin-top:22px">Я тренер і кінезіотерапевт. Дивлюся не тільки на вагу, а й на те, як рухається тіло: мобільність, перекоси, затиснені м’язи.</div></div>',phb('07-svetr-cegla-vpevnena-poza-1',880,'50% 18%'))
ST('s3','<div class="wrap" style="top:250px"><h1 style="font-size:150px">А ЦЕ <span class="r">ЛУНА</span></h1><div class="body" style="font-size:44px">Французький бульдог і частина команди. Буде на прогулянках і в роликах. Порад про їжу від неї не буде — тільки від мене.</div></div>',phb('12-lavka-chervone-hudi-z-lunoyu',700,'60% 40%'),(1420,200,'місце під стикер «Слайдер» 😍<br>«Наскільки Луна мила?»'))
ST('s4','<div class="wrap" style="top:250px"><h1 style="font-size:120px">ТУТ ПРО ЇЖУ БЕЗ <span class="r">ЗАБОРОН</span></h1><div class="list"><div>Конкретні продукти й сніданки</div><div>Які аналізи здати, якщо вага стоїть</div><div>Добавки: що, скільки і навіщо</div><div>Прості плани на день під звичайний графік</div></div><div class="body" style="font-size:44px">І без «не їж після 18:00».</div></div>',G+'<div class="ph" style="background-image:url(11-yizha-svynyna-na-skovorodi.jpg);top:auto;height:620px;background-position:50% 40%;opacity:.9"></div><div style="position:absolute;left:0;right:0;bottom:0;height:620px;background:linear-gradient(180deg,#0A0A0A,rgba(10,10,10,.1) 45%)"></div>')
ST('s5','<div class="wrap" style="top:250px"><h1 style="font-size:130px"><span class="r">ЗАПИТАЙ</span> ПРО ЇЖУ</h1><div class="body" style="font-size:38px;margin-top:20px">Що з’їсти на сніданок, які аналізи здати, чи потрібна добавка — пиши. Найчастіші питання розберу в сторис.</div></div>',phb('04-kurtka-cegla-ok-zhest-usmishka',760,'50% 10%'),(1480,180,'місце під стикер «Питання»<br>«Твоє питання про їжу»'))
open('p.html','w').write(CSS+''.join(h for _,h,_ in S)+'</body></html>')
json.dump([[i,s] for i,_,s in S],open('ids.json','w'))
