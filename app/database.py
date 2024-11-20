from pymongo import MongoClient
import os

# MongoDB Configuration
MONGO_URI = os.environ.get('MONGODB_URI')
DATABASE_NAME = "ship_monitoring"
COLLECTION_NAME = "engine_sensors"

# Initialize the MongoDB client
client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]