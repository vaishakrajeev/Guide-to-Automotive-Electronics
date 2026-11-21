import json, os, subprocess, sys, urllib.request
BASE = "https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/en/en_GB"
VOICES = [  # (label, model, speaker name or None)
    ("1-alan", "alan/medium/en_GB-alan-medium", None),
    ("2-alan-low", "alan/low/en_GB-alan-low", None),
    ("3-northern-english-male", "northern_english_male/medium/en_GB-northern_english_male-medium", None),
    ("4-semaine-spike", "semaine/medium/en_GB-semaine-medium", "spike"),
    ("5-semaine-obadiah", "semaine/medium/en_GB-semaine-medium", "obadiah"),
    ("6-vctk-p226", "vctk/medium/en_GB-vctk-medium", "p226"),
    ("7-vctk-p232", "vctk/medium/en_GB-vctk-medium", "p232"),
    ("8-vctk-p254", "vctk/medium/en_GB-vctk-medium", "p254"),
]
PITCH = 0.94
piper, text = sys.argv[1], open(sys.argv[2]).read().strip()
os.makedirs("voice-samples/out", exist_ok=True); os.makedirs("models", exist_ok=True)
for label, m, spk in VOICES:
    onnx = os.path.join("models", os.path.basename(m) + ".onnx")
    if not os.path.exists(onnx):
        urllib.request.urlretrieve(f"{BASE}/{m}.onnx", onnx)
        urllib.request.urlretrieve(f"{BASE}/{m}.onnx.json", onnx + ".json")
    cfg = json.load(open(onnx + ".json")); rate = cfg["audio"]["sample_rate"]
    cmd = [piper, "--model", onnx, "--output_file", "/tmp/a.wav", "--length_scale", "1.05", "--sentence_silence", "0.35"]
    if spk is not None:
        cmd += ["--speaker", str(cfg["speaker_id_map"][spk])]
    subprocess.run(cmd, input=text.encode(), check=True)
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", "/tmp/a.wav", "-af",
        f"asetrate={rate}*{PITCH},aresample={rate},atempo={1/PITCH:.4f},loudnorm=I=-16:TP=-1.5",
        "-ac", "1", "-b:a", "64k", f"voice-samples/out/{label}.mp3"], check=True)
    print("made", label)
