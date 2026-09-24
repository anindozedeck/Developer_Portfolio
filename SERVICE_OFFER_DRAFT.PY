# Write a structured service offer in Python
service = {
    "title": "AI Automation Scripts for Small Businesses",
    "problem": "Manual data entry and report generation waste hours every week.",
    "solution": "I build Python scripts that automate your data workflows.",
    "deliverable": "A working script, tested, documented, and handed over.",
    "price": "Starting from $150 per project"
}
for key, val in service.items():
    print(f"{key.upper()}: {val}")