import subprocess,wave,json,sys
P='/tmp/claude-0/-home-user-my-agents/c155b133-747f-5116-b9d7-b71925d8b33c/scratchpad'
name=sys.argv[1]; segs=json.load(open(name+'_voice.json'))
t=0.25; starts=[]; durs=[]; lst=open(name+'_list.txt','w')
subprocess.run(['ffmpeg','-y','-v','error','-f','lavfi','-i','anullsrc=r=22050:cl=mono','-t','0.25',name+'_lead.wav']); lst.write(f"file '{name}_lead.wav'\n")
for i,s in enumerate(segs):
    f=f'{name}_s{i}.wav'
    subprocess.run([P+'/tts-venv/bin/piper','-m',P+'/voices/mykyta_uk_UA-mykyta-high.onnx','--length-scale','0.86','--sentence-silence','0.12','-f',f],input=s.encode(),check=True,capture_output=True)
    with wave.open(f) as w: d=w.getnframes()/w.getframerate()
    starts.append(round(t,3)); durs.append(round(d,3)); t+=d+0.18
    lst.write(f"file '{f}'\n")
    g=f'{name}_g{i}.wav'; subprocess.run(['ffmpeg','-y','-v','error','-f','lavfi','-i','anullsrc=r=22050:cl=mono','-t','0.18',g]); lst.write(f"file '{g}'\n")
lst.close()
subprocess.run(['ffmpeg','-y','-v','error','-f','concat','-safe','0','-i',name+'_list.txt','-ar','44100','-af','loudnorm=I=-16:TP=-1.5',name+'_voice.wav'],check=True)
json.dump({'starts':starts,'durs':durs,'end':round(t+0.8,2)},open(name+'_timing.json','w'))
print(starts,round(t,2))
