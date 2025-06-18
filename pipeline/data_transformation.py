import pandas as pd 

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    df['name'] = df['name'].str.title()
    df['city'] = df['city'].str.upper()
    return df
    