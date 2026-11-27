import json
from eng import build,words
T=json.load(open('r1_timing.json'))
st='stroke-linecap="round"'
V={
'beet':'<svg viewBox="0 0 100 100" width="100%"><path d="M50 30 C20 30 18 70 50 92 C82 70 80 30 50 30Z" fill="#8a1f4d"/><path d="M50 30 L42 6 M50 30 L50 4 M50 30 L60 8" stroke="#3f8a3a" stroke-width="5" stroke-linecap="round"/></svg>',
'cab':'<svg viewBox="0 0 100 100" width="100%"><circle cx="50" cy="54" r="40" fill="#8cc06a"/><path d="M50 16 C40 40 40 70 50 94 M50 16 C62 40 62 70 50 94 M14 50 C35 46 65 46 86 50" stroke="#5e9a42" stroke-width="3" fill="none"/></svg>',
'car':'<svg viewBox="0 0 100 100" width="100%"><path d="M30 26 L70 26 L52 96 Z" fill="#f08a24"/><path d="M40 26 L34 4 M50 26 L50 2 M60 26 L66 4" stroke="#3f8a3a" stroke-width="5" stroke-linecap="round"/></svg>',
'pum':'<svg viewBox="0 0 100 100" width="100%"><ellipse cx="50" cy="58" rx="42" ry="32" fill="#e8811f"/><path d="M50 26 C36 40 36 80 50 90 M50 26 C64 40 64 80 50 90" stroke="#c96512" stroke-width="3" fill="none"/><rect x="46" y="12" width="8" height="16" rx="3" fill="#5b4a2a"/></svg>',
'rad':'<svg viewBox="0 0 100 100" width="100%"><circle cx="50" cy="52" r="36" fill="#2a2a2a" stroke="#555" stroke-width="2"/><circle cx="50" cy="52" r="22" fill="#f1efe9"/><path d="M50 16 L44 2 M50 16 L56 2" stroke="#3f8a3a" stroke-width="5" stroke-linecap="round"/></svg>',
'top':'<svg viewBox="0 0 100 100" width="100%"><path d="M28 40 C20 20 52 14 58 30 C76 22 90 44 76 58 C86 76 62 92 50 80 C34 92 14 76 24 62 C12 54 16 42 28 40Z" fill="#b08a5c"/></svg>'}
def item(n,name,kc,tip,icon):
    return ('<div class="bgD"></div><div class="pin">6 ЗИМОВИХ <span class="r">ОВОЧІВ</span></div>'
     f'<div class="ctr" style="top:420px;display:flex;flex-direction:column;align-items:center;gap:34px"><div style="width:400px">{V[icon]}</div>'
     +words(f"*{n}. {name}","H")+words(kc,"M")+words(tip,"S")+'</div>')
cut=lambda f,h,extra='': f'<div class="glow"></div><img class="cut" src="{f}" style="height:{h}px">{extra}'
S=[('<div class="bgR"></div>'+f'<div class="ctr" style="top:330px">{words("6 ЗИМОВИХ ОВОЧІВ","H")}{words("ЗАМІСТЬ","H")}{words("ТЕПЛИЧНИХ ОГІРКІВ","M")}</div>'+cut('08.png',1050),'r'),
('<div class="bgD"></div>'+f'<div class="ctr" style="top:380px">{words("*250 ККАЛ","H")}</div><div class="ctr" style="top:560px">{words("= 1 бутерброд з ковбасою","S")}</div><div class="ctr" style="top:700px">{words("АБО *600 Г БУРЯКУ","M")}</div>'+cut('06.png',900),'d'),
(item(1,'БУРЯК','43 ККАЛ · 2,8 Г КЛІТКОВИНИ','Запечи цілим','beet'),'i'),
(item(2,'КАПУСТА','25 ККАЛ','Повна тарілка — 50 ккал','cab'),'i'),
(item(3,'МОРКВА','41 ККАЛ','Тільки з ложкою олії','car'),'i'),
(item(4,'ГАРБУЗ','26 ККАЛ','Часточками в духовку','pum'),'i'),
(item(5,'РЕДЬКА','34 ККАЛ','З яблуком і сметаною','rad'),'i'),
(item(6,'ТОПІНАМБУР','73 ККАЛ · ІНУЛІН','Їжа для корисних бактерій','top'),'i'),
('<div class="bgR"></div>'+f'<div class="ctr" style="top:420px">{words("щоб не забути в магазині","S")}</div><div class="ctr" style="top:520px">{words("ЗБЕРЕЖИ","H")}</div>'+cut('08.png',980),'e')]
falls=[(V[k],x,dl,sp,rot) for k,x,dl,sp,rot in [('beet',60,0.0,650,40),('car',820,0.15,720,-50),('pum',430,0.4,600,30),('cab',180,1.0,680,-35),('rad',760,1.3,640,45),('top',520,1.8,700,-30)]]
build(S,T,'r1.html',falls)
