"""Generate one MP3 audio overview per news item with Piper TTS.

Usage: python news/make_audio.py <piper-binary> <voice.onnx>

For every item in news/news.json it builds the text "script" (or "title. summary" if no script). If the
voice or text changed it renders the MP3 again (file names are content hashes),
sets item["audio"], and deletes MP3s that no item references any more.
"""
import hashlib, json, os, subprocess, sys, tempfile

# Pitch factor below 1.0 makes the voice deeper; tempo is compensated so speed stays the same.
PITCH = 1.0

ROOT = os.path.dirname(os.path.abspath(__file__))
JSON = os.path.join(ROOT, "news.json")
AUDIO = os.path.join(ROOT, "audio")

def main(piper, model):
    voice = f"{os.path.basename(model)}|pitch={PITCH}|ls=1.1"
    with open(model + ".json", encoding="utf-8") as f:
        rate = json.load(f)["audio"]["sample_rate"]
    with open(JSON, encoding="utf-8") as f:
        data = json.load(f)
    os.makedirs(AUDIO, exist_ok=True)
    used, made = set(), 0
    for trend in data["trends"]:
        for item in trend["items"]:
            text = item.get("script") or f'{item["title"]}. {item["summary"]}'
            key = hashlib.sha1((voice + "\n" + text).encode()).hexdigest()[:12]
            name = f"{key}.mp3"
            path = os.path.join(AUDIO, name)
            used.add(name)
            if not os.path.exists(path):
                with tempfile.TemporaryDirectory() as tmp:
                    wav = os.path.join(tmp, "a.wav")
                    subprocess.run([piper, "--model", model, "--output_file", wav,
                                    "--length_scale", "1.1", "--sentence_silence", "0.35"],
                                   input=text.encode(), check=True)
                    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", wav,
                                    "-af", (f"asetrate={rate}*{PITCH},aresample={rate},atempo={1/PITCH:.4f}," if PITCH != 1.0 else "") + "loudnorm=I=-16:TP=-1.5", "-ac", "1",
                                    "-b:a", "64k", path], check=True)
                made += 1
            item["audio"] = f"news/audio/{name}"
            dur = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                  "-of", "csv=p=0", path], capture_output=True, text=True, check=True).stdout
            item["audio_sec"] = round(float(dur))
    removed = 0
    for f in os.listdir(AUDIO):
        if f.endswith(".mp3") and f not in used:
            os.remove(os.path.join(AUDIO, f)); removed += 1
    with open(JSON, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"audio: {made} generated, {removed} removed, {len(used)} total")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
