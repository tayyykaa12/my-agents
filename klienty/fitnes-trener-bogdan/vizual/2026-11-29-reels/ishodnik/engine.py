import json
HEAD='''<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@600;700&family=Montserrat:wght@500;600;700;800&display=block" rel="stylesheet">
<style>*{margin:0;padding:0;box-sizing:border-box}body{background:#000}
#v{position:relative;width:1080px;height:1920px;overflow:hidden;background:#0A0A0A;font-family:Montserrat;color:#fff}
.g{position:absolute;inset:0;background:radial-gradient(circle at 100% 0%,#5C0A0Dcc 0,transparent 50%),radial-gradient(circle at 0% 100%,#5C0A0D99 0,transparent 50%)}
.sc{position:absolute;inset:0;opacity:0}
.ph{position:absolute;inset:0;background-size:cover;background-position:center}
.shade{position:absolute;inset:0;background:linear-gradient(180deg,rgba(10,10,10,0) 35%,rgba(10,10,10,.85) 62%,#0A0A0A 85%)}
.shadeT{position:absolute;inset:0;background:linear-gradient(0deg,rgba(10,10,10,0) 40%,rgba(10,10,10,.85) 68%,#0A0A0A 88%)}
.c{position:absolute;left:80px;right:80px}
.ln{opacity:0;transform:translateY(40px)}
.h{font:700 120px/1.02 Oswald;text-transform:uppercase}
.m{font:700 84px/1.05 Oswald;text-transform:uppercase}
.s{font:600 52px/1.3 Montserrat}
.xs{font:600 36px/1.3 Montserrat;color:#B3B3B3}
.r{color:#E1141B}
.num{font:700 300px/0.85 Oswald;color:#E1141B}
.big{font:700 170px/0.95 Oswald;text-transform:uppercase}
.card{background:#161616;border-left:12px solid #E1141B;padding:36px 44px}
.nick{position:absolute;left:0;right:0;bottom:250px;text-align:center;font:600 34px Montserrat;color:#B3B3B3;z-index:9}
.bar{position:absolute;left:0;top:0;height:10px;background:#E1141B;z-index:9}
</style></head><body><div id="v"><div class="g"></div>'''
def build(scenes,end,out):
    # scenes: list of (start,stop,html,kenburns)
    body=''
    for i,(a,b,h,kb) in enumerate(scenes): body+=f'<div class="sc" id="sc{i}" data-a="{a}" data-b="{b}" data-kb="{1 if kb else 0}">{h}</div>'
    js='''<div class="bar" id="bar"></div><div class="nick">@konoplyanik2.0</div></div><script>
window.END=%s;const cl=x=>Math.max(0,Math.min(1,x)),eo=x=>1-Math.pow(1-cl(x),3);
function setT(t){document.querySelectorAll('.sc').forEach(s=>{const a=+s.dataset.a,b=+s.dataset.b;
 const fi=a===0?1:cl((t-a)/0.25), fo=1-cl((t-(b-0.2))/0.2); const on=t>=a-0.01&&t<b+0.01;
 s.style.opacity=on?Math.min(fi,b>=END?1:fo):0;
 const ph=s.querySelector('.ph'); if(ph&&s.dataset.kb==='1'){ph.style.transform=`scale(${1.04+0.08*cl((t-a)/(b-a))})`;}
 s.querySelectorAll('.ln').forEach((l,k)=>{const p=eo((t-a-0.1-k*0.22)/0.4);l.style.opacity=p;l.style.transform=`translateY(${(1-p)*40}px)`;});});
 document.getElementById('bar').style.width=(cl(t/END)*1080)+'px';}
setT(0);</script></body></html>'''%end
    open(out,'w').write(HEAD+body+js)
