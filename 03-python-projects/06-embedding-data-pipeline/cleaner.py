import pandas as pd

def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:

    df = df.copy()

    df.dropna(subset=['text'], inplace=True)

    df.drop_duplicates(subset=['text'], inplace=True)

    df['text'] = df['text'].str.strip()

    return df

    