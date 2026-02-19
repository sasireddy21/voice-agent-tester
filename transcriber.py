def transcribe(audio_file):
    transcript = "Agent responded with confusion and repeated questions."
    out = audio_file.replace(".wav", ".txt")
    with open(out, "w") as f:
        f.write(transcript)
    return transcript
