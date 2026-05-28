import asyncio
from sentence_transformers import SentenceTransformer


model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


async def generate_embeddings(text_batch):
    loop = asyncio.get_event_loop()

    embeddings = await loop.run_in_executor(
        None,
        model.encode,
        text_batch
    )

    return embeddings.tolist()