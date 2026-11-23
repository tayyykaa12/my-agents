const { chromium } = require('playwright'); const fs=require('fs');
(async()=>{const dir=process.argv[2]; const ids=JSON.parse(fs.readFileSync(dir+'/ids.json'));
const b=await chromium.launch(); const p=await b.newPage({viewport:{width:1100,height:1400},deviceScaleFactor:1});
await p.goto('file://'+dir+'/m.html'); await p.evaluate(()=>document.fonts.ready); await p.waitForTimeout(800);
for(const id of ids) await p.locator('#'+id).screenshot({path:`${dir}/${id}.png`});
await b.close();})();
