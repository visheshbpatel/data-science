import json
import os


def save_embeddings(data, filename="output/embeddings.json"):

    os.makedirs("output",exist_ok=True)

    with open(filename, "w", encoding="utf-8") as file:

        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False
        )