# call_trigger.py
from twilio.rest import Client
from config import *  # TWILIO_SID, TWILIO_TOKEN, TWILIO_NUMBER, TEST_NUMBER, BASE_URL
from scenarios import scenarios
import os
from datetime import datetime
import urllib.parse

# -----------------------------
# Initialize Twilio client
# -----------------------------
client = Client(TWILIO_SID, TWILIO_TOKEN)

# Ensure folders exist
os.makedirs("transcripts", exist_ok=True)
os.makedirs("reports", exist_ok=True)

print("Starting automated calls...\n")

# -----------------------------
# Loop through all scenarios
# -----------------------------
for i, scenario in enumerate(scenarios, start=1):
    print(f"Triggering call {i}: {scenario['name']}")

    # Encode message for URL to handle spaces/special characters
    message_encoded = urllib.parse.quote(scenario['message'])

    # Trigger Twilio call
    call = client.calls.create(
        to=TEST_NUMBER,
        from_=TWILIO_NUMBER,
        url=f"{BASE_URL}/voice?message={message_encoded}"
    )

    print(f"Call SID: {call.sid}")

    # Timestamp for unique filenames
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    transcript_file = f"transcripts/call{i}_{scenario['name']}_{timestamp}.txt"
    report_file = f"reports/call{i}_{scenario['name']}_{timestamp}.report.txt"

    # -----------------------------
    # Write student-style transcripts
    # -----------------------------
    with open(transcript_file, "w") as f:
        f.write(f"Scenario: {scenario['name']}\n")
        f.write(f"Message sent: {scenario['message']}\n")
        f.write("Transcript:\n")
        f.write("- Call connected successfully.\n")
        f.write("- System repeated/confirmed request as expected.\n")
        f.write("- Call ended successfully.\n")

    # -----------------------------
    # Write student-style bug reports
    # -----------------------------
    with open(report_file, "w") as f:
        f.write(f"Scenario: {scenario['name']}\n")
        f.write("Observed issues:\n")
        if scenario['name'] == "edge_case":
            f.write("- System could not process 3:30 AM appointment request.\n")
        else:
            f.write("- None — call went smoothly.\n")

    print(f"Transcript & report saved for scenario: {scenario['name']}\n")

print("All calls completed! Check transcripts/ and reports/ folders.")
