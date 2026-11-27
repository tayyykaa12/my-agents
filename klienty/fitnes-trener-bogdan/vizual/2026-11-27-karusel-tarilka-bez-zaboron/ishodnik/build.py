import json,re,html
e=html.escape
def acc(t): return re.sub(r'\*(.+?)\*',r'<span class="r">\1</span>',e(t))
CSS=open('../k26/build.py').read().split("CSS='''")[1].split("'''")[0]
EXTRA='''
.tag{font:600 26px Montserrat;color:#B3B3B3;letter-spacing:3px;text-transform:uppercase;margin-bottom:22px}
.body b{font-weight:800}
.meal{background:#161616;border:2px solid #2E2E2E;padding:26px 30px;margin-top:20px;display:flex;gap:24px;align-items:flex-start}
.meal .t{flex:0 0 190px;font:700 36px Oswald;color:#E1141B;text-transform:uppercase}
.meal .d{font:500 32px/1.38 Montserrat}
.plate{display:flex;gap:40px;align-items:center;margin-top:40px}
.leg div{font:600 34px/1.3 Montserrat;margin:14px 0;display:flex;gap:16px;align-items:center}
.leg i{flex:0 0 30px;height:30px;border-radius:50%}
'''
CSS=CSS.replace('</style>',EXTRA+'</style>')
T=9; S=[]
def K(id,inner,n,bg):
    S.append(f'<div class="s k" id="{id}">{bg}<div class="num">{n:02d} / {T:02d}</div>{inner}<div class="nick">@konoplyanik2.0</div></div>')
G='<div class="glow"></div>'; SL=G+'<div class="slash"></div><div class="slash2"></div>'
def ph(f,pos): return f'<div class="ph" style="background-image:url({f}.jpg);background-position:{pos}"></div><div class="gb"></div>'
def txt(id,n,h,paras,bg):
    body=''.join(f'<div class="body" style="font-size:38px;margin-top:30px">{p}</div>' for p in paras)
    K(id,f'<div class="wrap mid"><h2>{acc(h)}</h2>{body}</div>',n,bg)
K('t1',ph('11-yizha-svynyna-na-skovorodi','50% 40%')+'<div class="wrap" style="bottom:150px"><div class="tag" style="color:#fff">▸ ТАРІЛКА БЕЗ ЗАБОРОН</div><h1 style="font-size:108px">ЩО ПОКЛАСТИ НА ТАРІЛКУ, ЩОБ НАРЕШТІ <span class="r">НАЇДАТИСЯ</span></h1><div class="body" style="font-size:36px;margin-top:24px">½ овочі · ¼ білок · ¼ гарнір · трохи жиру. З грамами. Хліб і масло лишаються.</div></div><div class="pill">ГОРТАЙ →</div>',1,'')
svg='''<svg width="420" height="420" viewBox="0 0 100 100"><circle cx="50" cy="50" r="48" fill="#1e1e1e" stroke="#2E2E2E" stroke-width="1"/>
<path d="M50 50 L50 4 A46 46 0 0 0 50 96 Z" fill="#3a7d3a"/><path d="M50 50 L50 4 A46 46 0 0 1 96 50 Z" fill="#E1141B"/><path d="M50 50 L96 50 A46 46 0 0 1 50 96 Z" fill="#c8a46a"/>
<circle cx="66" cy="66" r="6" fill="#f2d16b" stroke="#0A0A0A" stroke-width="1"/>
<line x1="50" y1="4" x2="50" y2="96" stroke="#0A0A0A" stroke-width="1.5"/><line x1="50" y1="50" x2="96" y2="50" stroke="#0A0A0A" stroke-width="1.5"/>
<text x="27" y="54" font-family="Oswald" font-size="9" fill="#fff" text-anchor="middle" font-weight="700">½</text><text x="70" y="32" font-family="Oswald" font-size="8" fill="#fff" text-anchor="middle" font-weight="700">¼</text><text x="74" y="80" font-family="Oswald" font-size="8" fill="#0A0A0A" text-anchor="middle" font-weight="700">¼</text></svg>'''
leg='<div class="leg"><div><i style="background:#3a7d3a"></i>Овочі — дві великі жмені</div><div><i style="background:#E1141B"></i>Білок — долоня</div><div><i style="background:#c8a46a"></i>Гарнір — кулак</div><div><i style="background:#f2d16b"></i>Жир — великий палець</div></div>'
K('t2',f'<div class="wrap mid"><h2>ПОЛОВИНА, ЧВЕРТЬ, <span class="r">ЧВЕРТЬ</span></h2><div class="plate">{svg}{leg}</div><div class="body" style="font-size:34px;margin-top:36px">Звичайна тарілка 24–26 см. Ваги не потрібні — міряєш рукою.</div></div>',2,G)
txt('t3',3,'ПОЛОВИНА — *ОВОЧІ*',['<b>250–300 г, дві великі жмені з гіркою:</b> огірки, помідори, квашена капуста, тушкована морква, запечений перець, броколі із заморозки.','Клітковина й вода займають об’єм у шлунку, а 300 г овочів — це всього <b>60–90 ккал</b>. Розтягнутий шлунок сам подає мозку сигнал «досить», а клітковина сповільнює травлення — голод не повертається через годину.'],SL)
txt('t4',4,'ЧВЕРТЬ — *БІЛОК*',['<b>Шматок із твою долоню:</b> 100–150 г готової курки, індички, свинини чи риби. Або 2–3 яйця, або 150–200 г кисломолочного сиру.','Білок насичує найсильніше: підвищує гормони ситості GLP-1 і PYY і притлумлює грелін. До 20–30% його калорій іде на саме засвоєння. І саме білок зберігає м’язи, коли ти їси менше.'],G)
txt('t5',5,'ЧВЕРТЬ — *ГАРНІР*',['<b>Порція з кулак:</b> 150 г готової гречки чи булгуру, 2 невеликі картоплини (≈180 г) або 2 скибки житнього хліба (60 г). Скрізь близько 30 г вуглеводів.','Хліб і картопля тут на рівних із крупою. Прибереш гарнір зовсім — і о 17:00 рука сама тягнеться до печива.'],SL)
txt('t6',6,'І ТРОХИ *ЖИРУ*',['<b>Порція з великий палець:</b> 1–2 ч. л. олії, 10 г вершкового масла, 15–20 г горіхів або чверть авокадо.','Жир довше тримає ситість, а без нього гірше засвоюються бета-каротин (з нього організм робить вітамін A), вітаміни E і K. Олію міряй ложкою: столова — це вже 120 ккал, а з пляшки на око ллється дві-три.'],G)
meals=[('Сніданок','Омлет із 3 яєць, 250 г помідорів, огірків і шпинату, 2 скибки житнього хліба з 10 г масла'),('Обід','120 г свинячої вирізки з пательні, 150 г гречки, 250 г салату з капусти й моркви з 1 ч. л. олії'),('Вечеря','150 г запеченого хека, 2 невеликі картоплини з духовки, 250 г броколі й перцю з 1 ч. л. олії')]
K('t7','<div class="wrap mid"><h2>3 ГОТОВІ <span class="r">ТАРІЛКИ</span></h2>'+''.join(f'<div class="meal"><div class="t">{a}</div><div class="d">{e(b)}</div></div>' for a,b in meals)+'<div class="body" style="font-size:34px;margin-top:30px">У кожній 25–35 г білка, і в жодній немає заборон.</div></div>',7,SL)
txt('t8',8,'БОРЩ І ВАРЕНИКИ — ЗА ТИМ САМИМ *ПРАВИЛОМ*',['<b>Борщ</b> уже дає овочі й трохи картоплі. Поклади в нього шматок яловичини з долоню, візьми скибку хліба — і це повний обід.','<b>6 вареників із сиром</b> — це гарнір і половина білка. Поруч салат на півтарілки, ложка сметани й склянка кефіру — і білок добраний.'],G)
K('t9',ph('10-zal-chervone-hudi-portret','50% 20%')+'<div class="wrap" style="bottom:140px"><h1 style="font-size:100px">ЗБЕРЕЖИ — І ЗАВТРА ЗБЕРИ <span class="r">ОБІД</span></h1><div class="body" style="font-size:36px;margin-top:22px">Перед тим як накладати, відкрий слайд 2: дві жмені овочів, долоня білка, кулак гарніру, палець жиру. Хліб і картопля лишаються на тарілці.</div></div>',9,'')
open('p.html','w').write(CSS+''.join(S)+'</body></html>')
json.dump([[f't{i}',False] for i in range(1,10)],open('ids.json','w'))
