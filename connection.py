from pymongo import MongoClient

MONGODB_URL = "mongodb+srv://<Username>:<Password>@<dbName>.egqdcrt.mongodb.net/?retryWrites=true&w=majority&appName=<dbName>"

client = MongoClient(MONGODB_URL)

for db_name in client.list_database_names():
    print(db_name)


