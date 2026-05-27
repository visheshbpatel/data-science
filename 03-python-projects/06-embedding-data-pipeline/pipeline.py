import pandas as pd
from cleaner import clean_dataframe
from batcher import create_batches
from embedder import generate_embeddings


def run_pipeline():
    print("Loading CSV...")

    df = pd.read_csv("data/sample.csv")

    print(f"Rows before cleaning: {len(df)}")

    df = clean_dataframe(df)

    print(f"Rows after cleaning: {len(df)}")

    text = df['text'].tolist()

    batch_size=2

    print("\nCreating Batches:")

    for batch_number , batch in enumerate(
        create_batches(text, batch_size), start=1):

        print(f"Batch {batch_number}")
        print(batch)

        embeddings = generate_embeddings(batch)

        print(f"generated {len(embeddings)} embeddings")

        print(f"embedding dimensions: {len(embeddings[0])}")


        print()
