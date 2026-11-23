import html,sys,json
K=sys.argv[1]
E=html.escape
CAR={
'k4':[('cover','МПК ІНВЕСТ · ШПАРГАЛКА','Скільки тонн щебеню <span class="o">замовляти?</span>','Щебінь продається в тоннах. Рахуємо за 4 кроки. Гортайте →',None),
 ('step','КРОК 1','Об\'єм','Товщину переведіть в метри: 10 см = 0,1 м.','ПЛОЩА × ТОВЩИНА = ОБ\'ЄМ, м³'),
 ('step','КРОК 2','Тонни','Щебінь продається в тоннах, тому об\'єм переводимо у вагу.','ОБ\'ЄМ × ЩІЛЬНІСТЬ = ТОННИ'),
 ('step','ВАЖЛИВО','Щільність','Орієнтовна насипна щільність гранітного щебеню. Для різних фракцій вона трохи відрізняється — точну уточнюйте при замовленні.','≈ 1,4 т/м³'),
 ('step','ПРИКЛАД','Умовний приклад','Числа для ілюстрації, не рекомендація для вашого об\'єкта.','100 м² × 0,1 м = 10 м³|10 м³ × 1,4 т/м³ ≈ 14 т'),
 ('step','КРОК 3','Запас','Додайте запас на ущільнення і втрати. Розмір запасу визначайте за проєктом або технологією робіт.',None),
 ('step','КРОК 4','Фракція','Перевірте, що фракція підходить під задачу.','ЩЕБІНЬ 5–10 … 40–70 мм|ЩПС 0–40, 0–70 мм|ПІСОК'),
 ('cta',None,'Замовте <span class="o">доставку</span>','Продаємо в тоннах. Об\'єми: від мішка до самоскида.',None)],
'k5':[('cover','МПК ІНВЕСТ · ЯК ЗАМОВИТИ','Як замовити щебінь: <span class="o">від заявки до доставки</span>','Чотири кроки. Гортайте →',None),
 ('step','01','Заявка','Телефоном або на сайті mpc-invest.com.ua.',None),
 ('step','02','Фракція й об\'єм','Об\'єми: від мішка до самоскида.',None),
 ('step','03','Доставка','Привеземо вчасно, щоб майстри не чекали.',None),
 ('step','04','Гарантія точної ваги','',None),
 ('cta',None,'Замовте <span class="o">доставку</span>','',None)],
'k6':[('cover','МПК ІНВЕСТ · ЧЕК-ЛИСТ ПРОРАБА','Як прийняти щебінь <span class="o">на об\'єкті?</span>','4 перевірки при розвантаженні. Гортайте →',None),
 ('step','01','Фракція','Звірте фракцію в документі із замовленою. Подивіться, що розмір зерна відповідає замовленню.',None),
 ('step','02','Чистота й домішки','Огляньте матеріал у кузові: чи немає пилу, глини, землі та сторонніх включень.',None),
 ('step','03','Вага','Попросіть документ про вагу партії. Вага має збігатися із замовленою.',None),
 ('step','04','Документи','Попросіть документи на якість партії. Перевірте, що дані збігаються із замовленням.',None),
 ('step','ЯКЩО НЕ ЗБІГАЄТЬСЯ','Що робити при розбіжності','Зафіксуйте до підпису: фото кузова і запис у документі. Повідомте постачальника.',None),
 ('check','ЧЕК-ЛИСТ НА ОБ\'ЄКТ','Чек-лист на об\'єкт','',['Фракція','Чистота й домішки','Вага','Документи']),
 ('cta2',None,'Надішліть <span class="o">прорабу</span>','МПК Інвест · Чернігів',None)],
}
css='''<!doctype html><html lang="uk"><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@700&family=Montserrat:wght@500;600;800&display=block" rel="stylesheet">
<style>*{margin:0;padding:0;box-sizing:border-box}body{background:#444}
.s{position:relative;width:1080px;height:1350px;overflow:hidden;margin-bottom:20px;background:#1C1C1C;color:#fff;font-family:Montserrat,sans-serif}
.tex{position:absolute;inset:0;background:url(gravel.jpg) center/cover;filter:grayscale(1) brightness(.8)}
.sh{position:absolute;inset:0;background:linear-gradient(180deg,rgba(28,28,28,.55),rgba(28,28,28,.9) 70%,#1C1C1C)}
.flat{position:absolute;inset:0;background:radial-gradient(120% 80% at 80% 0%,#262626 0%,#1C1C1C 60%,#161616 100%)}
.edge{position:absolute;left:0;right:0;bottom:0;height:300px;background:url(gravel.jpg) center/cover;filter:grayscale(1) brightness(.5);-webkit-mask-image:linear-gradient(to top,rgba(0,0,0,.55),transparent)}
.h{font-family:Oswald,sans-serif;font-weight:700;text-transform:uppercase;line-height:.98}
.o{color:#F28C1E}
.label{font-weight:600;font-size:22px;letter-spacing:.25em;text-transform:uppercase;color:#A6A6A6}
.kick{font-family:Oswald;font-weight:700;color:#F28C1E;font-size:120px;line-height:1}
.kick.small{font-size:46px;letter-spacing:.08em}
.body{font-weight:500;font-size:40px;line-height:1.4;color:#E4E4E2}
.plate{display:inline-block;background:#E4E4E2;color:#1C1C1C;font-family:Oswald;font-weight:700;font-size:54px;padding:18px 30px;line-height:1.1}
.num{position:absolute;right:72px;top:72px;font-weight:600;font-size:22px;letter-spacing:.2em;color:#A6A6A6}
.logo{position:absolute;left:72px;top:72px;width:230px}
.arrow{position:absolute;right:72px;bottom:72px;width:96px;height:96px;border:2px solid #5A5A5A;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:44px;color:#fff}
.ph{font-weight:800;font-size:60px;line-height:1.3}
.chk{display:flex;align-items:center;gap:28px;font-family:Oswald;font-weight:700;font-size:72px;text-transform:uppercase;margin:22px 0}
.chk i{width:64px;height:64px;border:4px solid #F28C1E;border-radius:8px;flex:none}
</style></head><body>'''
def slide(i,n,sd,cid):
    k,kick,title,small,extra=sd
    sid=f'{cid}_{i}'
    if k=='cover':
        return f'''<div class="s" id="{sid}"><div class="tex"></div><div class="sh"></div><img class="logo" src="logo.png">
<div style="position:absolute;left:72px;right:72px;top:430px"><div class="label">{E(kick)}</div><div class="h" style="font-size:112px;margin-top:24px">{title}</div>
<div class="body" style="margin-top:36px;color:#A6A6A6">{E(small)}</div></div><div class="arrow">→</div></div>'''
    if k in('cta','cta2'):
        sub=f'<div class="body" style="margin:30px 0 50px">{E(small)}</div>' if small else '<div style="height:60px"></div>'
        return f'''<div class="s" id="{sid}"><div class="tex" style="opacity:.25"></div><div class="flat" style="opacity:.75"></div><img class="logo" src="logo.png"><div class="num">{i:02d}/{n:02d}</div>
<div style="position:absolute;left:72px;right:72px;top:360px"><div class="h" style="font-size:120px">{title}</div>{sub}
<div class="ph">050 010 66 25<br>050 444 45 21</div><div style="font-weight:800;font-size:44px;color:#F28C1E;margin-top:20px">mpc-invest.com.ua</div></div>
<img src="shch.png" style="position:absolute;right:30px;bottom:0;width:380px"></div>'''
    if k=='check':
        items=''.join(f'<div class="chk"><i></i>{E(x)}</div>' for x in extra)
        return f'''<div class="s" id="{sid}"><div class="flat"></div><div class="edge"></div><div class="num">{i:02d}/{n:02d}</div>
<div style="position:absolute;left:72px;right:72px;top:150px;bottom:260px;display:flex;flex-direction:column;justify-content:center"><div class="kick small">ДЛЯ ПРОРАБА</div><div class="h" style="font-size:100px;margin:20px 0 50px">{title}</div>{items}</div></div>'''
    big=len(kick)<=2
    kk=f'<div class="kick{"" if big else " small"}">{E(kick)}</div>'
    pl=''.join(f'<div style="margin-top:{46 if j==0 else 16}px"><span class="plate">{E(x)}</span></div>' for j,x in enumerate(extra.split('|'))) if extra else ''
    sm=f'<div class="body" style="margin-top:44px;font-size:44px">{E(small)}</div>' if small else ''
    return f'''<div class="s" id="{sid}"><div class="flat"></div><div class="edge"></div><div class="num">{i:02d}/{n:02d}</div>
<div style="position:absolute;left:72px;right:72px;top:150px;bottom:260px;display:flex;flex-direction:column;justify-content:center">{kk}<div class="h" style="font-size:112px;margin-top:22px">{E(title)}</div>{pl}{sm}</div></div>'''
out=css; ids=[]
for cid,sl in CAR.items():
    n=len(sl)
    for i,sd in enumerate(sl,1): out+=slide(i,n,sd,cid); ids.append(f'{cid}_{i}')
out+='</body></html>'
open(K+'/k.html','w',encoding='utf-8').write(out); json.dump(ids,open(K+'/ids.json','w'))
