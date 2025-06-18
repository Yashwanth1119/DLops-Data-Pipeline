from faker import Faker
import pandas as pd 
import random

fake = Faker()
data = []

for i in range(1, 1501):
    record = {
        "id": i,
        "name": fake.name(),
        "age": random.randint(18, 65),
        "city": fake.city()
    }
    # inject some bad data
    if i % 100 == 0:
        record['age'] = "not_a_number"
    if i % 150 == 0:
        record['name'] = ""
    data.append(record)

df = pd.DataFrame(data)
df.to_csv("data/raw_data.csv", index=False)
print("CSV file with 1500 rows saved to data/raw_data.csv")