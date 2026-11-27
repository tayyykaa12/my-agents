const { chromium } = require('playwright'); const { spawn } = require('child_process');
(async()=>{const dir=process.argv[2], out=process.argv[3], fps=30;
const b=await chromium.launch(); const p=await b.newPage({viewport:{width:1080,height:1920},deviceScaleFactor:1});
await p.goto('file://'+dir+'/'+(process.argv[4]||'reel.html')); await p.evaluate(()=>document.fonts.ready); await p.waitForTimeout(500);
const END=await p.evaluate(()=>window.END); const N=Math.round(END*fps);
const ff=spawn('ffmpeg',['-y','-v','error','-f','image2pipe','-framerate',String(fps),'-i','-','-f','lavfi','-i','anullsrc=r=44100:cl=stereo','-shortest','-c:v','libx264','-pix_fmt','yuv420p','-crf','18','-preset','medium','-c:a','aac','-movflags','+faststart',out]);
for(let f=0;f<N;f++){await p.evaluate(t=>setT(t),f/fps); const buf=await p.locator('#v').screenshot({type:'jpeg',quality:92}); if(!ff.stdin.write(buf)) await new Promise(r=>ff.stdin.once('drain',r));}
ff.stdin.end(); await new Promise(r=>ff.on('close',r)); await b.close(); console.log('frames',N);})();
