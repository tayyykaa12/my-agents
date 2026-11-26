import json,re,html
D=json.load(open('slides.json'))
def acc(t): return re.sub(r'\*(.+?)\*',r'<span class="r">\1</span>',html.escape(t))
e=html.escape
CSS=open('../k26/build.py').read().split("CSS='''")[1].split("'''")[0]
EXTRA='''
.grid{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-top:50px}
.cell{background:#161616;border:2px solid #2E2E2E;padding:28px 30px}
.cell b{display:block;font:700 46px/1.1 Oswald;text-transform:uppercase}
.cell span{font:500 30px/1.3 Montserrat;color:#B3B3B3}
.cell.big b{font-size:110px;color:#E1141B}
.li2 div{font:500 40px/1.38 Montserrat;margin-top:24px;padding-left:46px;position:relative}
.li2 div:before{content:"▸";color:#E1141B;position:absolute;left:0;top:0}
.xx div{font:600 42px/1.35 Montserrat;margin-top:26px;display:flex;gap:24px;align-items:flex-start}
.xx i{flex:0 0 58px;height:58px;border:3px solid #E1141B;color:#E1141B;font:700 36px/52px Montserrat;text-align:center;font-style:normal}
.tag{font:600 26px Montserrat;color:#B3B3B3;letter-spacing:3px;text-transform:uppercase;margin-bottom:20px}
.price{display:flex;align-items:baseline;gap:30px;margin-top:40px}
.price .n{font:700 260px/0.9 Oswald;color:#E1141B}
.price .g{font:700 90px Oswald}
.price .o{font:600 90px Oswald;color:#777;text-decoration:line-through;text-decoration-color:#E1141B;text-decoration-thickness:8px}
'''
CSS=CSS.replace('</style>',EXTRA+'</style>')
T=9
S=[]
def K(id,inner,n,bg):
    S.append(f'<div class="s k" id="{id}">{bg}<div class="num">{n:02d} / {T:02d}</div>{inner}<div class="nick">@konoplyanik2.0</div></div>')
G='<div class="glow"></div>'; SL=G+'<div class="slash"></div><div class="slash2"></div>'
def ph(f,pos): return f'<div class="ph" style="background-image:url({f}.jpg);background-position:{pos}"></div><div class="gb"></div>'
d=D['s1']; K('s1',f'<div class="wrap" style="bottom:140px"><div class="tag" style="color:#fff">ШКОЛА ХАРЧУВАННЯ</div><h1 style="font-size:104px">{acc(d["h"])}</h1><div class="body" style="font-size:38px;margin-top:24px">{e(d["t"])}</div><div class="body muted" style="font-size:28px;margin-top:18px">{e(d["sub"])}</div></div>',1,ph('10-zal-chervone-hudi-portret','50% 15%'))
d=D['s2']; K('s2',f'<div class="wrap mid"><h2>{acc(d["h"])}</h2><div class="body muted" style="font-size:34px;margin-top:24px">{e(d["pre"])}</div><div class="li2">'+''.join(f'<div>{e(x)}</div>' for x in d['li'])+'</div></div>',2,G)
d=D['s3']; cells=''.join(f'<div class="cell{" big" if i==0 else ""}"><b>{e(a)}</b><span>{e(b)}</span></div>' for i,(a,b) in enumerate(d['grid']))
K('s3',f'<div class="wrap mid"><h2>{acc(d["h"])}</h2><div class="grid">{cells}</div><div class="body" style="font-size:34px;margin-top:36px">{e(d["post"])}</div></div>',3,SL)
for k,n,bg in (('s4',4,G),('s5',5,SL)):
    d=D[k]; post=f'<div class="body muted" style="font-size:30px;margin-top:30px">{e(d["post"])}</div>' if 'post' in d else ''
    K(k,f'<div class="wrap mid"><div class="tag">{e(d["tag"])}</div><h2>{acc(d["h"])}</h2><div class="li2">'+''.join(f'<div>{e(x)}</div>' for x in d['li'])+f'</div>{post}</div>',n,bg)
d=D['s6']; K('s6',f'<div class="wrap mid"><h2 style="font-size:92px">{acc(d["h"])}</h2><div class="body" style="font-size:38px;margin-top:26px"><b>{e(d["pre"])}</b></div><div class="li2">'+''.join(f'<div>{e(x)}</div>' for x in d['li'])+f'</div><div class="body muted" style="font-size:28px;margin-top:30px">{e(d["post"])}</div></div>',6,G)
d=D['s7']; K('s7',f'<div class="wrap mid"><h2>{acc(d["h"])}</h2><div class="xx">'+''.join(f'<div><i>✕</i><span>{e(x)}</span></div>' for x in d['x'])+f'</div><div class="body" style="font-size:36px;margin-top:36px">{e(d["post"])}</div></div>',7,SL)
def price(id,d):
    old=f'<div class="o">{d["old"]}</div>' if 'old' in d else ''
    note=f'<div class="body" style="font-size:40px;margin-top:10px"><b>{e(d["note"])}</b></div>' if 'note' in d else ''
    K(id,f'<div class="wrap mid"><h2>ВАРТІСТЬ</h2><div class="price"><div class="n">{d["price"]}</div><div class="g">ГРН</div>{old}</div>{note}<div class="body muted" style="font-size:34px;margin-top:40px">{e(d["post"])}</div></div>',8,G)
price('s8a',D['s8a']); price('s8b',D['s8b'])
d=D['s9']; K('s9',f'<div class="wrap" style="bottom:140px"><h1 style="font-size:100px">{acc(d["h"])}</h1><div class="body" style="font-size:38px;margin-top:24px">{e(d["t"])}</div><div class="body muted" style="font-size:30px;margin-top:18px">{e(d["sub"])}</div></div>',9,ph('04-kurtka-cegla-ok-zhest-usmishka','50% 20%'))
open('p.html','w').write(CSS+''.join(S)+'</body></html>')
json.dump([[i,False] for i in ['s1','s2','s3','s4','s5','s6','s7','s8a','s8b','s9']],open('ids.json','w'))
