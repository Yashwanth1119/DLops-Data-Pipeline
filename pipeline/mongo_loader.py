import pymongo

def save_to_mongodb(df, db_name="dlopsdb", collection_name="cleaned_data"):
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client[db_name]
    collection = db[collection_name]
    collection.delete_many({})
    collection.insert_many(df.to_dict("records"))
