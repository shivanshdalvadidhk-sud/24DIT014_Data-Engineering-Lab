import json
import os
import time

import pandas as pd

from kafka import KafkaConsumer


RESULT_DIR = "data/results"

os.makedirs(
    RESULT_DIR,
    exist_ok=True
)


consumer = KafkaConsumer(

    "user-telemetry",

    bootstrap_servers=[
        "localhost:9092"
    ],

    group_id="telemetry-processors",

    auto_offset_reset="latest",

    enable_auto_commit=True,

    value_deserializer=lambda value:
        json.loads(
            value.decode("utf-8")
        )
)


results = []

print("Kafka streaming consumer started...")


try:

    for message in consumer:

        event = message.value

        received_at = time.time()

        # Producer timestamp → Consumer timestamp
        latency_ms = (
            received_at -
            event["sent_at"]
        ) * 1000

        result = {

            "timestamp":
                event["timestamp"],

            "user_id":
                event["user_id"],

            "event_type":
                event["event_type"],

            "partition":
                message.partition,

            "offset":
                message.offset,

            "latency_ms":
                round(
                    latency_ms,
                    3
                ),

            "cpu_percent":
                event["cpu_percent"],

            "memory_percent":
                event["memory_percent"],

            "response_time_ms":
                event["response_time_ms"]
        }

        results.append(result)

        print(
            f"Received | "
            f"partition={message.partition} | "
            f"offset={message.offset} | "
            f"latency={latency_ms:.2f} ms"
        )

        # Save results every 100 events
        if len(results) % 100 == 0:

            pd.DataFrame(
                results
            ).to_csv(
                "data/results/streaming_results.csv",
                index=False
            )

            print(
                f"\nProcessed "
                f"{len(results)} events\n"
            )


except KeyboardInterrupt:

    print("\nConsumer stopped.")

finally:

    consumer.close()

    if results:

        pd.DataFrame(
            results
        ).to_csv(
            "data/results/streaming_results.csv",
            index=False
        )