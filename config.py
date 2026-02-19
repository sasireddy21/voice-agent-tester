# Twilio configuration for your voice-agent-tester project

# If you eventually use a .env file, load it
import os
from dotenv import load_dotenv

load_dotenv()

TWILIO_SID = "YOUR_TWILIO_SID"
TWILIO_TOKEN = "YOUR_TWILIO_AUTH_TOKEN"
TWILIO_NUMBER = "+15555555555"   # placeholder phone number
TEST_NUMBER = "+18054398008"     # placeholder test number
BASE_URL = "https://your-ngrok-url.ngrok-free.dev"  # placeholder ngrok URL

