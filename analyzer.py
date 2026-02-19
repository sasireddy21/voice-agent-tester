import os

def analyze(text, audio_file):
    issues = []
    if "confusion" in text.lower():
        issues.append("Agent comprehension issue")
    if "repeated" in text.lower():
        issues.append("Looped response")
    report_file = f"reports/{os.path.basename(audio_file)}.report.txt"
    with open(report_file, "w") as f:
        f.write("Transcript Analysis\n\n")
        for issue in issues:
            f.write(f"- {issue}\n")
    print("Report saved:", report_file)
