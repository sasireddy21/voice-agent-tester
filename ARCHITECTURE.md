# Voice Agent Tester - Architecture Overview

## System Overview

The Voice Agent Tester is an automated Python-based system designed to evaluate and stress-test an AI-powered voice agent. It simulates realistic patient interactions, records conversations, transcribes them, and identifies potential issues in the AI agent’s responses. The system supports multiple scenarios including appointment scheduling, rescheduling, medication refills, and general queries about office hours, locations, and insurance.

The primary goal of this architecture is to provide a reliable, repeatable, and scalable testing framework for voice AI systems, ensuring both quality and coverage of edge cases.


## Key Components

1. **`app.py` (Flask Web Server)**

   * Hosts a lightweight Flask server that provides Twilio-compatible webhook endpoints.
   * Handles incoming requests from the Twilio API during calls and responds with dynamically generated messages based on the test scenarios.

2. **`call_trigger.py`**

   * Orchestrates automated calls to the test number using Twilio’s REST API.
   * Initiates calls, tracks Call SID, and triggers the Flask endpoints for conversation handling.
   * Stores call audio files and transcripts in designated folders.

3. **`scenarios.py`**

   * Contains predefined test scenarios simulating real patient interactions.
   * Provides messages for each call, including scheduling, rescheduling, and general queries.
   * Supports adding new scenarios for future testing.

4. **`config.py`**

   * Stores all environment-specific configuration, such as Twilio SID, Auth Token, phone numbers, and the Ngrok public URL.
   * For security, actual credentials are replaced with placeholders in the repository.

5. **`transcripts/` and `reports/`**

   * `transcripts/` stores text and audio files for each call.
   * `reports/` contains bug reports documenting AI agent failures, hallucinations, awkward phrasing, or unexpected behavior.

## Design Considerations

* **Modularity:** Each component is independent, allowing easy updates or replacements without affecting other modules.
* **Automation:** Calls, recordings, and transcripts are automatically generated to reduce manual testing effort.
* **Extensibility:** New scenarios can be added easily to test additional AI behaviors.
* **Security:** Sensitive credentials are never pushed to the repository; `.gitignore` ensures local virtual environments and cache files are excluded.
* **Transparency:** Transcripts and bug reports provide a clear audit trail for evaluation of AI performance.


## Workflow Summary

1. `call_trigger.py` initiates a call to the test number.
2. The Flask server (`app.py`) handles incoming Twilio requests and plays scenario-specific messages.
3. Conversations are recorded, and audio files are saved in `transcripts/`.
4. Transcripts are generated from the recordings and saved as `.txt` files.
5. Any issues with AI responses are documented in `reports/`.

This architecture ensures that each test run produces reproducible, high-quality results suitable for evaluation and continuous improvement of AI voice agents.
