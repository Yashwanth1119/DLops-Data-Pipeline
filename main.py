from pipeline.data_ingestion import load_csv
from pipeline.data_validation import validate_dataframe
from pipeline.data_transformation import transform_data
from pipeline.mongo_loader import save_to_mongodb
import pandas as pd
import os

def run_pipeline():
    df = load_csv("data/raw_data.csv")
    df_clean = validate_dataframe(df)
    df_transformed = transform_data(df_clean)

    os.makedirs("output", exist_ok=True)
    df_transformed.to_csv("output/cleaned_data.csv", index=False)

    save_to_mongodb(df_transformed)
