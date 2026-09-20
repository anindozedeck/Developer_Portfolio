def service_offer(skill, price, delivery):
    return f"Service: {skill} | Price: KES {price} | Delivery: {delivery} days"

print(service_offer("Python Automation", 15000, 3))
print(service_offer("Data Report", 8000, 2))