from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse
from scenarios import SCENARIOS
import random

app = Flask(__name__)

@app.route("/voice", methods=["POST"])
def voice():
    scenario = random.choice(SCENARIOS)
    response = VoiceResponse()
    for line in scenario:
        response.say(line)
        response.pause(1)
    response.record(action="/recording", max_length=30)
    return str(response)

@app.route("/recording", methods=["POST"])
def recording():
    from recorder import save_recording
    recording_url = request.form.get("RecordingUrl")
    save_recording(recording_url)
    return "OK"

if __name__ == "__main__":
    app.run(port=5000)
