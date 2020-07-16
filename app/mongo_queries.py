# app/mongo_queries.py

import pymongo
import os
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv("MONGO_USER", default="OOPS")
DB_PASSWORD = os.getenv("MONGO_PASSWORD", default="OOPS")
CLUSTER_NAME = os.getenv("MONGO_CLUSTER_NAME", default="OOPS")

connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority"
print("----------------")
print("URI:", connection_uri)  

client = pymongo.MongoClient(connection_uri)
print("----------------")
print("CLIENT:", type(client), client)
print("DATABASES:", client.list_database_names())

db = client.test_database # "test_database" or whatever you want to call it
print("----------------")
print("DB:", type(db), db)
print("COLLECTIONS:", db.list_collection_names())
# lecture note: the above two lines are
# the min. amount of code to to test in the 
# CLT via breakpoint() if the db connection is working
# breakpoint()

collection = db.pokemon_test # "pokemon_test" or whatever you want to call it
print("----------------")
print("COLLECTION:", type(collection), collection)
print("DOCUMENTS COUNT:", collection.count_documents({}))
# the above line needs an empty dictionary (a.k.a. {}) to run b/c a filter error will appear


print("----------------")
print("COLLECTIONS:")
print(db.list_collection_names())

collection.insert_one({
    "name": "Pikachu",
    "level": 30,
    "exp": 76000000000,
    "hp": 400,
})
#breakpoint()
print("DOCS:", collection.count_documents({}))
print(collection.count_documents({"name": "Pikachu"}))