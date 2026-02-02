from pymongo import MongoClient
from pprint import pprint
 
MONGO_URI = (
    "mongodb://root:password123@localhost:27017/"
    "?replicaSet=rs0"
    "&authSource=admin"
    "&directConnection=true"
)
 
def main():
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
 
    client.admin.command("ping")
    print("✅ Connected to MongoDB (direct primary)")
 
    db = client["test"]
    collection = db["users"]
 
    result = collection.insert_one({
        "name": "test",
        "role": "MongoDB Test",
        "status": "active"
    })
    print(f"📥 Inserted ID: {result.inserted_id}")
 
    doc = collection.find_one({"_id": result.inserted_id})
    print("📤 Retrieved:")
    pprint(doc)
 
if __name__ == "__main__":
    main()
 
