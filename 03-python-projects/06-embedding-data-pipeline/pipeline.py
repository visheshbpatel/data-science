import pandas as pd

def run_pipeline():
    
    print("Loding CSV...")

    df = pd.read_csv("data/sample.csv")

    print(df.head())
