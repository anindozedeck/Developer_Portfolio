# Build a simple project pricing calculator
def calculate_price(hours, rate=25, complexity=1.0):
    base = hours * rate
    return base * complexity

print(f"Simple script (5h): ${calculate_price(5):.0f}")
print(f"Medium project (15h): ${calculate_price(15, complexity=1.2):.0f}")
print(f"Complex project (30h): ${calculate_price(30, complexity=1.5):.0f}")