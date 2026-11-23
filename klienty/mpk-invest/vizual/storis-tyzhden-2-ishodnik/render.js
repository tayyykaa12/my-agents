const { chromium } = require('playwright');const fs=require('fs');
(async()=>{const d=process.argv[2];const ids=JSON.parse(fs.readFileSync(d+'/ids.json'));const b=await chromium.launch();
const p=await b.newPage({viewport:{width:1080,height:1920}});await p.goto('file://'+d+'/s.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(1000);
for(const [id,st] of ids){ if(st){await p.locator('[id="'+id+'"]').screenshot({path:`${d}/out/${id}-mistse-pid-stiker.png`});
 await p.evaluate(i=>{document.querySelector('[id="'+i+'"] .box').style.visibility='hidden'},id);}
 await p.locator('[id="'+id+'"]').screenshot({path:`${d}/out/${id}.png`});}
await b.close();})();
