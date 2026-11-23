const { chromium } = require('playwright');
(async()=>{const d=process.argv[2];const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
await p.goto('file://'+d+'/s.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(800);
await p.locator('#st1').screenshot({path:d+'/st1.png'});
await p.locator('#st2').screenshot({path:d+'/st2-s-pidkazkoyu.png'});
await p.evaluate(()=>{document.getElementById('box').style.display='none'});
await p.locator('#st2').screenshot({path:d+'/st2.png'});await b.close();})();
