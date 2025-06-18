def transform_data(df):
    df.columns = [col.lower().replace(" ", "_") for col in df.columns]
    return df
