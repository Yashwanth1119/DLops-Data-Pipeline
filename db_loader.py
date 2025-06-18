from sqlalchemy import create_engine
import pandas as pd 
import os

def save_to_postgres(df: pd.DataFrame, table_namae: str):
    db_url = os.environ.get("DB_URL")
    if not db_url:
        raise EnvironmentError("DB_URL not found in environment variables")
    engine = create_engine(db_url)
    df.to_sql(table_name, engine, if_exists='replace', index=False)