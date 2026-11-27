import json
from eng import build,words
from pics import P1,P2,P3
T=json.load(open('r2_timing.json'))
cut=lambda f,h: f'<div class="glow"></div><img class="cut" src="{f}" style="height:{h}px">'
def ex(n,name,dose,steps,pic):
    return ('<div class="bgD"></div><div class="pin">3 РУХИ ДЛЯ <span class="r">ШИЇ</span></div>'
     f'<div class="ctr" style="top:400px;display:flex;flex-direction:column;align-items:center;gap:26px">'+words(f"*{n}. {name}","M")+f'<div style="width:560px">{pic}</div>'+''.join(words(x,"S") for x in steps)+words(f"*{dose}","M")+'</div>')
S=[('<div class="bgR"></div>'+f'<div class="ctr" style="top:330px">{words("ШИЯ «КАМ’ЯНІЄ»","H")}{words("ПІСЛЯ НОУТБУКА?","M")}</div>'+cut('02.png',1150),'r'),
('<div class="bgD"></div>'+f'<div class="ctr" style="top:380px">{words("*3 РУХИ","H")}{words("прямо за столом","S")}</div>'+cut('08.png',1050),'d'),
(ex(1,'ПІДБОРІДДЯ НАЗАД','10 РАЗІВ',['Тримай 3 секунди'],P1),'i'),
(ex(2,'ВУХО ДО ПЛЕЧА','20 С НА БІК',['Плечі вниз, тягне — не болить'],P2),'i'),
(ex(3,'ЛОПАТКИ РАЗОМ','10 РАЗІВ',['Назад і вниз, 3 секунди'],P3),'i'),
('<div class="bgD"></div>'+f'<div class="ctr" style="top:640px">{words("ГОСТРИЙ БІЛЬ АБО ВІДДАЄ В РУКУ —","M")}<div style="height:30px"></div>{words("*ДО ЛІКАРЯ","H")}</div>','d'),
('<div class="bgR"></div>'+f'<div class="ctr" style="top:380px">{words("ЗБЕРЕЖИ","H")}{words("і зроби зараз","S")}</div>'+cut('06.png',1000),'e')]
build(S,T,'r2.html')
