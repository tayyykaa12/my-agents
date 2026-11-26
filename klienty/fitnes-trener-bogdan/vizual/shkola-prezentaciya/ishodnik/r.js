const { chromium } = require('playwright');const fs=require('fs');
(async()=>{const d=process.argv[2];const ids=JSON.parse(fs.readFileSync(d+'/ids.json'));const b=await chromium.launch();
const p=await b.newPage({viewport:{width:1100,height:2000}});await p.goto('file://'+d+'/p.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(1200);
fs.mkdirSync(d+'/out',{recursive:true});
for(const [id,st] of ids){const L=p.locator('[id="'+id+'"]'); if(st){await L.screenshot({path:`${d}/out/${id}-mistse-pid-stiker.png`});await p.evaluate(i=>{document.querySelector('[id="'+i+'"] .box').style.visibility='hidden'},id);} await L.screenshot({path:`${d}/out/${id}.png`});}
await b.close();})();
