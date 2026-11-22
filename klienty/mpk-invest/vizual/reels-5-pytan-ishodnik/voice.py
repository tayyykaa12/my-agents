import sys, subprocess, json, wave
voice, outdir, ls = sys.argv[1], sys.argv[2], sys.argv[3]
segs = [
 "П'ять питань постачальнику щебеню, які варто задати до оплати.",
 "Перше. Яка це фракція, і чи є сертифікат якості?",
 "Друге. Ціна вказана з доставкою чи без?",
 "Третє. Як зважують, і чи гарантують точну вагу?",
 "Четверте. Коли машина буде на об'єкті?",
 "П'яте. Чи привезуть потрібний об'єм, від мішка до самоскида?",
 "Замовте доставку в Ем Пе Ка Інвест. Привеземо вчасно, щоб майстри не чекали.",
]
durs=[]
for i,t in enumerate(segs):
    f=f"{outdir}/seg{i}.wav"
    subprocess.run([sys.argv[4], "-m", voice, "--length-scale", ls, "--sentence-silence", "0.15", "-f", f], input=t.encode(), check=True, capture_output=True)
    with wave.open(f) as w: durs.append(w.getnframes()/w.getframerate())
print(json.dumps(durs))
