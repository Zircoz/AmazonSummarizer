import pandas as pd

def cleaningRetailOrderHistDF(df):
    df = df[df["Website"].str.startswith("Amazon")]
    df.fillna(0)
    return df