from pydantic import BaseModel, ValidationError
import pandas as pd 

class Record(BaseModel):
    id: int 
    name: str 
    age: int
    city: str

def validate_dataframe(df: pd.DataFrame -> pd.DataFrame:
    valid = []
    for _, row in df.iterrows():
        try:
             Record(**row.to_dict())
            valid.append(row)
        except ValidationError:
            continue
    return pd.DataFrame(valid)