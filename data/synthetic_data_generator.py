import random
import uuid
import json
from datetime import datetime

customers = [str(uuid.uuid4()) for _ in range(1000)]

def generate_event():
    return {
        "customer_id": random.choice(customers),
        "event": random.choice(["login", "purchase", "logout"]),
        "amount": round(random.uniform(5, 200), 2) if random.random() > 0.7 else 0,
        "timestamp": datetime.utcnow().isoformat()
    }

if __name__ == "__main__":
    with open("data/synthetic_events.json", "w") as f:
        for _ in range(1000):
            f.write(json.dumps(generate_event()) + "\n")
    print("✅ Synthetic data generated: data/synthetic_events.json")
