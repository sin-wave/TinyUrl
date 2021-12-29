from pymongo import MongoClient, collection
from dotenv import dotenv_values

config = dotenv_values(".env")


class Database:
    def Connect():
        try:
            uri = dict(config)["URI"]
            clinet = MongoClient(uri)
            print("Connected Successfully to Database MongoDB")
            # d_b = clinet["myFirstDatabase"]
            # collection = d_b["url"]
            # data = {"code": "jehdy63r", "su": "short", "lu": "long"}
            # collection.insert_one(data)

            return clinet
        except Exception as e:
            print("Database Error", str(e))
