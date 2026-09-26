import csv
import os
import random
import time
from datetime import datetime, timezone

OUTPUT_DIR = "data/incoming"

os.makedirs(OUTPUT_DIR, exist_ok=True)


EVENT_TYPES = [
    "page_view",
    "login",
    "logout",
    "api_request",
    "file_download",
    "search"
]


def generate_event():
    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "user_id": f"U{random.randint(1000, 9999)}",
        "event_type": random.choice(EVENT_TYPES),
        "endpoint": random.choice([
            "/",
            "/login",
            "/dashboard",
            "/api/users",
            "/api/data",
            "/search"
        ]),
        "response_time_ms": random.randint(20, 800),
        "cpu_percent": round(random.uniform(20, 95), 2),
        "memory_percent": round(random.uniform(30, 90), 2),
        "status_code": random.choice([200, 200, 200, 201, 400, 404, 500])
    }


def generate_batch(batch_number, records=100):
    filename = os.path.join(
        OUTPUT_DIR,
        f"batch_{batch_number}.csv"
    )

    with open(filename, "w", newline="") as file:

        fieldnames = [
            "timestamp",
            "user_id",
            "event_type",
            "endpoint",
            "response_time_ms",
            "cpu_percent",
            "memory_percent",
            "status_code"
        ]

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        for _ in range(records):
            writer.writerow(generate_event())

    print(f"Created {filename} with {records} events")


if __name__ == "__main__":

    for batch in range(10):

        generate_batch(
            batch_number=batch,
            records=100
        )

        time.sleep(2)