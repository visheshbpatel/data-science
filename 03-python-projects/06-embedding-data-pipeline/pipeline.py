import asyncio
import pandas as pd
from tqdm import tqdm

from cleaner import clean_dataframe
from batcher import create_batches
from embedder import generate_embeddings
from storage import save_embeddings
from checkpoint import save_checkpoint, load_checkpoint


MAX_RETRIES = 3


async def process_batch(
    batch_number,
    batch,
    all_embeddings
):
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            embeddings = await generate_embeddings(batch)

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

            save_checkpoint(batch_number)

            return

        except Exception as error:
            print(
                f"Batch {batch_number} failed "
                f"(Attempt {attempt}/{MAX_RETRIES}): {error}"
            )

    print(
        f"Skipping batch {batch_number} "
        f"after {MAX_RETRIES} failed attempts"
    )


async def run_pipeline():
    print("Loading CSV...")

    df = pd.read_csv(
        "data/large_sample.csv"
    )

    print(
        f"Rows before cleaning: {len(df)}"
    )

    df = clean_dataframe(df)

    print(
        f"Rows after cleaning: {len(df)}"
    )

    texts = df["text"].tolist()

    batch_size = 2

    print("\nCreating Batches:\n")

    all_embeddings = []

    batches = list(
        create_batches(
            texts,
            batch_size
        )
    )

    last_processed_batch = load_checkpoint()

    print(
        f"Resuming from batch "
        f"{last_processed_batch + 1}"
    )

    tasks = []

    for batch_number, batch in enumerate(
        tqdm(
            batches,
            desc="Processing batches"
        ),
        start=1
    ):
        if batch_number <= last_processed_batch:
            continue

        print(f"Batch {batch_number}")
        print(batch)

        task = process_batch(
            batch_number,
            batch,
            all_embeddings
        )

        tasks.append(task)

    await asyncio.gather(*tasks)

    save_embeddings(
        all_embeddings
    )

    print(
        "Embeddings saved successfully."
    )