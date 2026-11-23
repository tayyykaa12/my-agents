import re,json,os
D=os.path.dirname(os.path.abspath(__file__))
src=open(D+'/build.py').read()
CSS=re.search(r"CSS='''(.*?)'''",src,re.S).group(1)
CSS+='''
.myth{font:700 30px Montserrat;color:#B3B3B3;letter-spacing:3px;margin-bottom:18px}
.myth b{color:#fff;background:#E1141B;padding:6px 14px;margin-right:14px}
.strike{position:relative;display:inline}
h2.m{font-size:104px}
.tag{font:800 30px Montserrat;color:#E1141B;letter-spacing:3px;margin-bottom:14px}
.card .tag{margin-bottom:18px}
.cover h1{font-size:150px;line-height:.95}
'''
def acc(t): return re.sub(r'\*(.+?)\*',r'<span class="r">\1</span>',t)
def S(id,inner,n,deco):
    return f'<div class="s" id="{id}">{deco}<div class="num">{n:02d} / 08</div>{inner}<div class="nick">@konoplyanik2.0</div></div>'
G='<div class="glow"></div>'; SL=G+'<div class="slash"></div><div class="slash2"></div>'
K=[]
K.append(S('m-1',SL+'<img class="bog" src="bogdan.png" style="width:700px;right:-90px;bottom:0"><div class="wrap t cover" style="top:150px;right:300px"><div class="label">▸ ЧЕСНО ПРО ХАРЧУВАННЯ</div><h1>ЇЖА —<br>НЕ <span class="r">ВОРОГ</span></h1><div class="body" style="font-size:40px;font-weight:700;margin-top:40px;max-width:520px">5 міфів, які можна почути на старті,</div><div class="body muted" style="font-size:34px;margin-top:10px;max-width:470px">і як воно насправді.</div></div><div class="pill">ГОРТАЙ →</div>',1,''))
M=[('ВУГЛЕВОДИ — *ВОРОГ*','Білки, жири й вуглеводи — <b>три основи харчування</b>.<br><br>Питання не в забороні, а в тому, <b>які саме й скільки</b>.'),
('ЩОБ СХУДНУТИ, *ГОЛОДУЙ*','Голод не вчить складати раціон.<br><br>Його важко тримати, і він <b>легко веде до зриву</b>.'),
('«КОРИСНЕ» — *БЕЗ МЕЖ*','Напис «fit» чи «натуральний» <b>не скасовує порції</b>.<br><br>Дивись на склад і на розмір порції.'),
('ПРАВИЛЬНО — ЦЕ *НУДНО*','Раціон не мусить бути вічною куркою з броколі.<br><br>Він складається з <b>їжі, яку ти реально їси</b>.'),
('ЗРИВ — ЗНАЧИТЬ *З ПОНЕДІЛКА*','Зрив — це <b>один прийом їжі</b>, а не кінець.<br><br>Наступний знову твій вибір.')]
for i,(h,b) in enumerate(M):
    K.append(S(f'm-{i+2}',f'<div class="big">{i+1}</div><div class="wrap"><div class="myth"><b>МІФ {i+1}</b>ЯК КАЖУТЬ</div><h2 class="m">{acc(h)}</h2><div class="card"><div class="tag">НАСПРАВДІ</div>{b}</div></div>',i+2,SL if i%2 else G))
K.append(S('m-7','<div class="wrap"><h2>ЩО <span class="r">СПІЛЬНЕ</span> У ВСІХ П\'ЯТИ</h2><div class="card">Усі п\'ять тягнуть <b>до крайнощів</b>: або все можна, або все заборонено.<br><br><span class="r" style="font-weight:800">Спокійніший підхід</span> — без заборон, крок за кроком.</div></div>',7,G))
K.append(S('m-8',SL+'<div class="wrap"><div class="label">⤓ ЗБЕРЕЖИ</div><h2 style="font-size:150px">ЗБЕРЕЖИ, ЩОБ <span class="r">НЕ ЗАБУТИ</span></h2><div class="body" style="font-size:44px;max-width:760px">Наступного разу, коли почуєш <b>«це не можна»</b> або <b>«усе пропало»</b>, повернешся до цих п\'яти слайдів.</div></div>',8,''))
open(D+'/m.html','w').write(f'<html><head><meta charset="utf-8"><style>{CSS}</style></head><body>'+''.join(K)+'</body></html>')
json.dump([f'm-{i}' for i in range(1,9)],open(D+'/ids.json','w'))
