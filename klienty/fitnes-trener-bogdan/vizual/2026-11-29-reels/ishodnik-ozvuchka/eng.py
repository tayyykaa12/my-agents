import json
HEAD='''<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@500;600;700&family=Montserrat:wght@500;600;700;800&display=block" rel="stylesheet">
<style>*{margin:0;padding:0;box-sizing:border-box}body{background:#000}
#v{position:relative;width:1080px;height:1920px;overflow:hidden;background:#0A0A0A;font-family:Montserrat;color:#fff}
.sc{position:absolute;inset:0;opacity:0}
.bgR{position:absolute;inset:0;background:radial-gradient(ellipse at 50% 40%,#b3121a 0,#7a0b10 45%,#3a0507 100%)}
.bgD{position:absolute;inset:0;background:radial-gradient(ellipse at 50% 45%,#2a0a0c 0,#120607 45%,#050505 100%)}
.ctr{position:absolute;left:70px;right:70px;text-align:center}
.w{display:inline-block;opacity:0;filter:blur(14px);transform:scale(.6);margin:0 .14em}
.H{font:700 128px/1.0 Oswald;text-transform:uppercase}
.M{font:700 86px/1.05 Oswald;text-transform:uppercase}
.S{font:600 50px/1.3 Montserrat}
.XS{font:600 36px/1.3 Montserrat;color:#bbb}
.r{color:#E1141B}.rb{color:#ff3b3f}
.pin{position:absolute;top:230px;left:60px;right:60px;text-align:center;font:700 74px/1.05 Oswald;text-transform:uppercase}
.cut{position:absolute;left:50%;bottom:0;transform-origin:50% 100%}
.glow{position:absolute;left:50%;bottom:-200px;width:1300px;height:1300px;transform:translateX(-50%);background:radial-gradient(circle,#E1141Bcc 0,#E1141B33 40%,transparent 68%)}
.fall{position:absolute;width:170px}
.nick{position:absolute;left:0;right:0;bottom:250px;text-align:center;font:600 30px Montserrat;color:#ffffff88;z-index:9}
</style></head><body><div id="v">'''
def build(scenes,T,out,falls=None):
    st,du,end=T['starts'],T['durs'],T['end']
    body=''
    for i,(html,kind) in enumerate(scenes):
        a=st[i]; b=st[i+1] if i+1<len(st) else end
        body+=f'<div class="sc" data-a="{a}" data-b="{b}" data-d="{du[i]}" data-k="{kind}">{html}</div>'
    fl=''
    if falls:
        for k,(svg,x,delay,sp,rot) in enumerate(falls):
            fl+=f'<div class="fall" data-x="{x}" data-dl="{delay}" data-sp="{sp}" data-rot="{rot}" style="left:{x}px">{svg}</div>'
    js='''<div id="falls">'''+fl+'''</div><div class="nick">@konoplyanik2.0</div></div><script>
window.END=__END__;const FE=__FE__;const cl=x=>Math.max(0,Math.min(1,x)),eo=x=>1-Math.pow(1-cl(x),3);
function setT(t){document.querySelectorAll('.sc').forEach(s=>{const a=+s.dataset.a,b=+s.dataset.b,d=+s.dataset.d;
 const on=t>=a-0.05&&t<b; const fi=cl((t-a+0.05)/0.18), fo=b>=END?1:1-cl((t-(b-0.12))/0.12); s.style.opacity=on?Math.min(fi,fo):0;
 const ws=s.querySelectorAll('.w'); const n=ws.length; const span=Math.max(0.6,d*0.75);
 ws.forEach((w,k)=>{const at=a+(n>1?k*span/(n):0); const p=eo((t-at)/0.28); w.style.opacity=p; w.style.filter=`blur(${(1-p)*14}px)`; w.style.transform=`scale(${0.6+0.4*p})`;});
 const c=s.querySelector('.cut'); if(c){const p=eo((t-a)/0.5); c.style.transform=`translateX(-50%) translateY(${(1-p)*160}px) scale(${1+0.04*cl((t-a)/(b-a))})`; c.style.opacity=p;}
 });
 document.querySelectorAll('.fall').forEach(f=>{const dl=+f.dataset.dl,sp=+f.dataset.sp; const y=-260+(t-dl)*sp; f.style.top=y+'px'; f.style.transform=`rotate(${(t-dl)*f.dataset.rot}deg)`; f.style.opacity=(t>=dl&&t<FE)?1:0;});}
setT(0);</script></body></html>'''
    js=js.replace('__END__',str(end)).replace('__FE__',str((falls and max(x[2] for x in falls)+3) or 0))
    open(out,'w').write(HEAD+body+js)
def words(txt,cls):
    out=''
    for tok in txt.split(' '):
        red=tok.startswith('*')
        tok=tok.strip('*')
        out+=f'<span class="w{" rb" if red else ""}">{tok}</span>'
    return f'<div class="{cls}">{out}</div>'
