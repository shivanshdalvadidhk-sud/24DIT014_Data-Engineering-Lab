import glob
import os
import time
import pandas as pd


INPUT_DIR = "data/incoming"
RESULT_DIR = "data/results"

os.makedirs(RESULT_DIR, exist_ok=True)


def process_batch(filename):

    start_time = time.perf_counter()

    df = pd.read_csv(filename)

    # Processing
    average_response = df["response_time_ms"].mean()
    average_cpu = df["cpu_percent"].mean()
    average_memory = df["memory_percent"].mean()

    errors = df[df["status_code"] >= 400]

    processing_time = (
        time.perf_counter() - start_time
    )

    result = {
        "file": os.path.basename(filename),
        "records": len(df),
        "average_response_ms": round(average_response, 2),
        "average_cpu": round(average_cpu, 2),
        "average_memory": round(average_memory, 2),
        "errors": len(errors),
        "processing_time_seconds": round(
            processing_time, 6
        )
    }

    print(result)

    return result


def main():

    processed = set()
    results = []

    print("Starting micro-batch processor...")

    while True:

        files = glob.glob(
            os.path.join(INPUT_DIR, "*.csv")
        )

        for filename in files:

            if filename in processed:
                continue

            result = process_batch(filename)

            results.append(result)

            processed.add(filename)

        if len(processed) >= 10:
            break

        time.sleep(2)

    pd.DataFrame(results).to_csv(
        f"{RESULT_DIR}/batch_results.csv",
        index=False
    )

    print("\nBatch processing complete.")


if __name__ == "__main__":
    main()