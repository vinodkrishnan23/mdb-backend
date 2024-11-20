from pymongo import MongoClient

# MongoDB Configuration
MONGO_URI = "mongodb+srv://root:root@practisem10.6awcb.mongodb.net/test"
DATABASE_NAME = "ship_monitoring"
COLLECTION_NAME = "engine_sensors"

# Initialize the MongoDB client
client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]