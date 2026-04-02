from pymongo import MongoClient

client = MongoClient("mongodb://ashok:12345@localhost:27017/?authSource=admin")

db = client["machin_data"]

print("MongoDB Connected Successfully")