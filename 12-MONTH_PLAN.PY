# Print a structured 12-month growth plan
plan = [
    ("Months 1-2", "Land first 2 paid clients using existing portfolio"),
    ("Months 3-4", "Build one SaaS micro-tool and launch it"),
    ("Months 5-6", "Raise rates and specialize in one niche"),
    ("Months 7-9", "Scale to 3-5 recurring clients"),
    ("Months 10-12", "Hit monthly income target and document the process")
]
print("12-Month Growth Plan")
print("-" * 40)
for period, goal in plan:
    print(f"{period}: {goal}")