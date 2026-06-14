# Embedding Data Pipeline

A production-inspired data pipeline that reads text data from CSV files, cleans the data, splits it into batches, generates embeddings using a local Sentence Transformer model, and stores the results in a structured JSON format.

This project was built to learn and demonstrate key data engineering concepts such as batching, checkpoint recovery, retry mechanisms, asynchronous processing, and embedding generation.

## Features

* CSV data ingestion
* Data cleaning and preprocessing
* Batch processing
* Embedding generation using Sentence Transformers
* Progress tracking with tqdm
* Checkpoint recovery
* Retry mechanism for failed batches
* Asynchronous batch processing
* JSON-based embedding storage

## Project Structure

```text
06-embedding-data-pipeline/
│
├── app.py
├── pipeline.py
├── cleaner.py
├── batcher.py
├── embedder.py
├── storage.py
├── checkpoint.py
│
├── data/
│   ├── sample.csv
│   └── large_sample.csv
│
├── output/
│   ├── embeddings.json
│   └── checkpoint.json
│
├── README.md
├── requirements.txt
└── .gitignore
```

## Pipeline Workflow

```text
CSV File
   ↓
Load Data
   ↓
Clean Data
   ↓
Create Batches
   ↓
Generate Embeddings
   ↓
Save Checkpoint
   ↓
Store Embeddings
```

## Technologies Used

* Python
* Pandas
* NumPy
* Sentence Transformers
* asyncio
* tqdm
* JSON

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd 06-embedding-data-pipeline
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the pipeline:

```bash
python app.py
```

## Example Output

```text
Loading CSV...
Rows before cleaning: 500
Rows after cleaning: 430

Processing batches: 100%

Embeddings saved successfully.
```

## Engineering Concepts Demonstrated

* Data Cleaning
* Batch Processing
* Embeddings
* Error Handling
* Retry Logic
* Checkpoint Recovery
* Asynchronous Programming
* Data Persistence

## Future Improvements

* Vector database integration
* OpenAI embedding support
* Gemini embedding support
* CLI configuration options
* Logging system
* Performance monitoring

## Author

**Vishesh Patel**

GitHub: https://github.com/visheshbpatel