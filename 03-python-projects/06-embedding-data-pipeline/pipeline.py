import pandas as pd
from tqdm import tqdm

from cleaner import clean_dataframe
from batcher import create_batches
from embedder import generate_embeddings
from storage import save_embeddings


def run_pipeline():
    print("Loading CSV...")

    df = pd.read_csv("data/sample.csv")

    print(f"Rows before cleaning: {len(df)}")

    df = clean_dataframe(df)

    print(f"Rows after cleaning: {len(df)}")

    texts = df["text"].tolist()

    batch_size = 2

    print("\nCreating Batches:\n")

    all_embeddings = []

    batches = list(create_batches(texts, batch_size))

    for batch_number, batch in enumerate(
        tqdm(
            batches,
            desc="Processing batches"
        ),
        start=1
    ):
        print(f"Batch {batch_number}")
        print(batch)

        try:
            embeddings = generate_embeddings(batch)

            print(
                f"Generated {len(embeddings)} embeddings"
            )

            print(
                f"Embedding dimension: {len(embeddings[0])}"
            )

            for text, embedding in zip(
                batch,
                embeddings
            ):
                all_embeddings.append(
                    {
                        "text": text,
                        "embedding": embedding
                    }
                )

        except Exception as error:
            print(
                f"Error processing batch {batch_number}: {error}"
            )

        print()

    save_embeddings(all_embeddings)

    print("Embeddings saved successfully.")


if __name__ == "__main__":
    run_pipeline()