services = [
    {
        "name":    "Automated Data Reports",
        "client":  "small business owners who export data manually",
        "problem": "spending 2-4 hours per week copying data between spreadsheets and writing summaries",
        "outcome": "a Python script that reads their data source and produces a formatted weekly report in under 30 seconds",
        "tools":   "Python, pandas, CSV/Excel/JSON",
        "example": "28-day fitness log analysis with weekly breakdown and protocol comparison"
    },
    {
        "name":    "API Integration Scripts",
        "client":  "operations teams using two or more disconnected tools",
        "problem": "manually copying data between platforms with no automation between them",
        "outcome": "a Python script that pulls from one API and pushes to another automatically on a schedule",
        "tools":   "Python, requests, FastAPI, JSON",
        "example": "Multi-endpoint dashboard pulling from three simulated SMP data sources"
    },
    {
        "name":    "AI Writing Automation",
        "client":  "business owners who write the same types of responses repeatedly",
        "problem": "spending hours writing first drafts of emails, summaries, or customer responses",
        "outcome": "a Python tool that generates structured drafts using the OpenAI API in the required voice and format",
        "tools":   "Python, OpenAI API, python-dotenv",
        "example": "SMP coaching message generator that mirrors the Chat API response structure"
    },
    {
        "name":    "ISP Billing & Support Integration",
        "client":  "internet service providers in Mombasa and its growing suburban service areas that manage billing, CRM, and WhatsApp support in separate systems",
        "problem": "customer activations, payment updates, and disconnection notices are recorded in multiple tools, which slows renewals, duplicates records, and leaves support teams without real-time account status",
        "outcome": "an automated integration that syncs customer activations, payment status, and service suspensions between the billing platform, CRM, and WhatsApp support queue in real time",
        "tools":   "Python, requests, JSON, SQLite/PostgreSQL, API integration",
        "example": "ISP onboarding flow that creates a customer record, updates the balance after payment, and flags expired accounts for the support team"
    },
]

for i, s in enumerate(services, 1):
    print(f"SERVICE {i}: {s['name'].upper()}")
    print()
    print(f"  Who I help:    {s['client']}")
    print(f"  Their problem: {s['problem']}")
    print(f"  What I deliver:{s['outcome']}")
    print(f"  Tools used:    {s['tools']}")
    print(f"  Proof of work: {s['example']}")
    print()

    # Generate a one-line pitch
    pitch = f"I help {s['client']} by building {s['outcome']}."
    print(f"  One-line pitch: \"{pitch}\"")
    print("-" * 60)