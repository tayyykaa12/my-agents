from engine import build
V={
'beet':'<svg viewBox="0 0 100 100" width="470"><path d="M50 30 C20 30 18 70 50 92 C82 70 80 30 50 30Z" fill="#7a1e45"/><path d="M50 30 L42 6 M50 30 L50 4 M50 30 L60 8" stroke="#3f8a3a" stroke-width="5" stroke-linecap="round"/></svg>',
'cab':'<svg viewBox="0 0 100 100" width="470"><circle cx="50" cy="54" r="40" fill="#8cc06a"/><path d="M50 16 C40 40 40 70 50 94 M50 16 C62 40 62 70 50 94 M14 50 C35 46 65 46 86 50" stroke="#5e9a42" stroke-width="3" fill="none"/></svg>',
'car':'<svg viewBox="0 0 100 100" width="470"><path d="M30 26 L70 26 L52 96 Z" fill="#f08a24"/><path d="M40 26 L34 4 M50 26 L50 2 M60 26 L66 4" stroke="#3f8a3a" stroke-width="5" stroke-linecap="round"/><path d="M38 44h12M42 60h10M46 76h6" stroke="#c96b12" stroke-width="3"/></svg>',
'pum':'<svg viewBox="0 0 100 100" width="470"><ellipse cx="50" cy="58" rx="42" ry="32" fill="#e8811f"/><path d="M50 26 C36 40 36 80 50 90 M50 26 C64 40 64 80 50 90" stroke="#c96512" stroke-width="3" fill="none"/><rect x="46" y="12" width="8" height="16" rx="3" fill="#5b4a2a"/></svg>',
'rad':'<svg viewBox="0 0 100 100" width="470"><circle cx="50" cy="52" r="36" fill="#2a2a2a"/><circle cx="50" cy="52" r="22" fill="#f1efe9"/><path d="M50 88 L50 98" stroke="#2a2a2a" stroke-width="4"/><path d="M50 16 L44 2 M50 16 L56 2" stroke="#3f8a3a" stroke-width="5" stroke-linecap="round"/></svg>',
'top':'<svg viewBox="0 0 100 100" width="470"><path d="M28 40 C20 20 52 14 58 30 C76 22 90 44 76 58 C86 76 62 92 50 80 C34 92 14 76 24 62 C12 54 16 42 28 40Z" fill="#b08a5c"/><circle cx="40" cy="44" r="3" fill="#8a6a42"/><circle cx="62" cy="60" r="3" fill="#8a6a42"/></svg>'}
def ph(f,pos,shade='shade'): return f'<div class="ph" style="background-image:url({f}.jpg);background-position:{pos}"></div><div class="{shade}"></div>'
def veg(n,name,kc,tip,icon):
    return f'<div class="c" style="top:250px"><div class="ln" style="display:flex;align-items:flex-end;gap:30px"><div class="num">{n}</div><div class="big" style="font-size:150px">{name}</div></div><div class="ln" style="margin-top:40px">{V[icon]}</div><div class="ln m" style="margin-top:30px">{kc}</div><div class="ln s" style="margin-top:24px">{tip}</div></div>'
S=[(0,2.4,ph('01-kurtka-park-rozstebuye','50% 20%')+'<div class="c" style="bottom:330px"><div class="ln h">6 ЗИМОВИХ ОВОЧІВ</div><div class="ln h"><span class="r">ЗАМІСТЬ</span> ТЕПЛИЧНИХ</div><div class="ln h">ОГІРКІВ</div></div>',True),
(2.4,5.2,'<div class="c" style="top:320px"><div class="ln h">І СИТНІШИХ ЗА <span class="r">БУТЕРБРОД</span></div><div class="ln card" style="margin-top:70px"><div class="m">250 ККАЛ =</div><div class="s" style="margin-top:14px">1 бутерброд з ковбасою</div><div class="m r" style="margin-top:20px">АБО 600 Г БУРЯКУ</div></div></div>',False),
(5.2,8.0,veg(1,'БУРЯК','43 ККАЛ · 2,8 Г КЛІТКОВИНИ','Запечи цілим або натри з часником','beet'),False),
(8.0,10.8,veg(2,'КАПУСТА','25 ККАЛ','200 г капусти — повна тарілка за 50 ккал','cab'),False),
(10.8,13.8,veg(3,'МОРКВА','41 ККАЛ','Їж з ложкою олії: без жиру каротин не засвоюється','car'),False),
(13.8,16.6,veg(4,'ГАРБУЗ','26 ККАЛ','Часточками в духовку: 200°, 25 хвилин','pum'),False),
(16.6,19.4,veg(5,'РЕДЬКА','34 ККАЛ','Натри з яблуком і ложкою сметани','rad'),False),
(19.4,22.4,veg(6,'ТОПІНАМБУР','73 ККАЛ · ІНУЛІН','Їжа для корисних бактерій кишківника','top'),False),
(22.4,25.5,ph('01-kurtka-park-rozstebuye','50% 30%')+'<div class="c" style="bottom:330px"><div class="ln h" style="font-size:170px"><span class="r">ЗБЕРЕЖИ</span></div><div class="ln s">Список знадобиться в магазині</div></div>',True)]
build(S,25.5,'reel1.html')
