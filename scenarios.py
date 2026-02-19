# scenarios.py
# patient scenarios for testing the voice agent

scenarios = [
    {"name": "appointment", "message": "Hi, I’d like to book an appointment for next Monday, please."},
    {"name": "reschedule", "message": "Hello, can I move my Monday appointment to Wednesday?"},
    {"name": "cancel", "message": "I need to cancel my appointment for Monday."},
    {"name": "medication_refill", "message": "Could I get a refill for my blood pressure medication?"},
    {"name": "office_hours", "message": "What time do your offices open and close this week?"},
    {"name": "location", "message": "Can you tell me the office address?"},
    {"name": "insurance", "message": "Do you accept my health insurance plan?"},
    {"name": "edge_case", "message": "Is it possible to schedule an appointment at 3:30 AM?"},
    {"name": "mixed_requests", "message": "I need to reschedule an appointment and also refill my meds."},
    {"name": "stress_test", "message": "Please tell me everything about my appointments, medications, and insurance."}
]
