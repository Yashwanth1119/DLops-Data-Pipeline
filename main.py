from pipeline.data_ingestion import load_csv
from pipeline.data_validation import validate_dataframe
from pipeline.data_transformation import transform_data
from pipeline.data_loader import save_to_csv
from pipeline.db_loader import save_to_postgres

def run_pipeline():
    df = load_csv("data/raw_data.csv")
    df = validate_dataframe(df)
    df = transform_data(df)
    save_to_csv(df, "output/cleaned_data.csv")
    save_to_postgres(df, "cleaned_users")

if __name__ == "__main__":
    run_pipeline()
