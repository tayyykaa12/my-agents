from engine import build
st='stroke="#fff" stroke-width="5" stroke-linecap="round" fill="none"'
red='stroke="#E1141B" stroke-width="6" stroke-linecap="round" fill="none"'
P1=f'<svg viewBox="0 0 200 200" width="520"><rect x="120" y="120" width="70" height="8" fill="#555"/><rect x="150" y="96" width="34" height="24" fill="#333" stroke="#777" stroke-width="2"/><circle cx="82" cy="44" r="20" {st}/><path d="M80 64 L78 80 L74 140 M74 140 L74 196 M76 90 L110 118 L140 120" {st}/><path d="M128 46 L106 46 M106 46 L114 39 M106 46 L114 53" {red}/><text x="100" y="22" fill="#B3B3B3" font-size="12" font-family="Montserrat">НАЗАД</text></svg>'
P2=f'<svg viewBox="0 0 200 200" width="520"><g transform="rotate(-22 100 72)"><circle cx="100" cy="44" r="20" {st}/></g><path d="M100 70 L100 82 M50 92 L150 92 M100 82 L100 160 M50 92 L44 150 M150 92 L156 150" {st}/><path d="M122 34 C140 40 146 56 140 72 M140 72 L132 66 M140 72 L146 63" {red}/><path d="M60 102 L60 118 M60 118 L54 111 M60 118 L66 111" {red}/></svg>'
P3=f'<svg viewBox="0 0 200 200" width="520"><circle cx="100" cy="36" r="20" {st}/><path d="M100 56 L100 68 M46 80 L154 80 M100 68 L100 170 M46 80 L52 140 M154 80 L148 140" {st}/><path d="M78 92 C70 108 70 124 80 134 M122 92 C130 108 130 124 120 134" stroke="#B3B3B3" stroke-width="4" fill="none"/><path d="M58 112 L84 112 M84 112 L76 105 M84 112 L76 119 M142 112 L116 112 M116 112 L124 105 M116 112 L124 119" {red}/></svg>'
def ph(f,pos): return f'<div class="ph" style="background-image:url({f}.jpg);background-position:{pos}"></div><div class="shade"></div>'
def ex(n,name,why,steps,dose,pic):
    li=''.join(f'<div class="ln s" style="font-size:44px;margin-top:10px">▸ {x}</div>' for x in steps)
    return f'<div class="c" style="top:240px"><div class="ln" style="display:flex;align-items:flex-end;gap:26px"><div class="num" style="font-size:220px">{n}</div><div class="m" style="font-size:90px">{name}</div></div><div class="ln xs" style="margin-top:10px">{why}</div><div class="ln" style="margin-top:20px;text-align:center">{pic}</div>{li}<div class="ln m r" style="margin-top:20px">{dose}</div></div>'
S=[(0,2.6,ph('10-zal-chervone-hudi-portret','50% 18%')+'<div class="c" style="bottom:330px"><div class="ln h">ШИЯ «<span class="r">КАМ’ЯНІЄ</span>»</div><div class="ln h">ПІСЛЯ НОУТБУКА</div><div class="ln m" style="margin-top:16px">3 РУХИ НА 2 ХВИЛИНИ</div><div class="ln xs" style="margin-top:10px">КІНЕЗІОТЕРАПЕВТ</div></div>',True),
(2.6,4.2,'<div class="c" style="top:640px"><div class="ln h">ПРЯМО ЗА <span class="r">СТОЛОМ</span>,</div><div class="ln h">НЕ ВСТАЮЧИ</div></div>',False),
(4.2,9.2,ex(1,'ПІДБОРІДДЯ НАЗАД','Вмикає глибокі згиначі шиї',['Голова рівно, погляд прямо','Відсунь підборіддя назад','Тримай 3 секунди'],'10 РАЗІВ',P1),False),
(9.2,14.2,ex(2,'ВУХО ДО ПЛЕЧА','Розтягує верхню трапецію',['Плечі опущені','Повільно нахили голову вбік','Тягне, але не болить'],'20 С КОЖЕН БІК',P2),False),
(14.2,19.2,ex(3,'ЛОПАТКИ РАЗОМ','Вмикає м’язи між лопатками',['Лікті зігнуті, плечі вниз','Зведи лопатки назад і вниз','Тримай 3 секунди'],'10 РАЗІВ',P3),False),
(19.2,21.6,'<div class="c" style="top:640px"><div class="ln m">ЯКЩО БІЛЬ ГОСТРИЙ АБО ВІДДАЄ В РУКУ —</div><div class="ln h r" style="margin-top:20px">ДО ЛІКАРЯ</div></div>',False),
(21.6,24.5,ph('10-zal-chervone-hudi-portret','50% 25%')+'<div class="c" style="bottom:330px"><div class="ln h"><span class="r">ЗБЕРЕЖИ</span></div><div class="ln h">І ЗРОБИ ЗАРАЗ</div></div>',True)]
build(S,24.5,'reel2.html')
