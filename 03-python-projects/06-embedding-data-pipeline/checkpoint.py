import json
import os


CHECKPOINT_FILE = "output/checkpoint.json"


def save_checkpoint(batch_number):
    os.makedirs("output", exist_ok=True)

    with open(CHECKPOINT_FILE, "w") as file:
        json.dump(
            {
                "last_processed_batch": batch_number
            },
            file,
            indent=4
        )


def load_checkpoint():
    if not os.path.exists(CHECKPOINT_FILE):
        return 0

    with open(CHECKPOINT_FILE, "r") as file:
        data = json.load(file)

    return data.get("last_processed_batch", 0)