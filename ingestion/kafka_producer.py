from kafka import KafkaProducer
import json
import time
import random
from data.synthetic_data_generator import generate_event

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

topic = "customer_events"

if __name__ == "__main__":
    for _ in range(20):
        event = generate_event()
        producer.send(topic, event)
        print("➡️ Sent:", event)
        time.sleep(random.uniform(0.5, 2))
