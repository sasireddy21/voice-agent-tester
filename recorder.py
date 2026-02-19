import requests, time
from transcriber import transcribe
from analyzer import analyze

def save_recording(url):
    filename = f"transcripts/call_{int(time.time())}.wav"
    r = requests.get(url + ".wav")
    with open(filename, "wb") as f:
        f.write(r.content)
    print("Saved:", filename)
    text = transcribe(filename)
    analyze(text, filename)
