from fastapi import FastAPI, HTTPException
from bson import ObjectId
from app.database import collection
from app.models import SensorData, UpdateSensorData

app = FastAPI()

# Helper function to convert BSON ObjectId to string
def serialize_doc(doc):
    doc["_id"] = str(doc["_id"])
    return doc

@app.post("/data/", response_model=dict)
def insert_data(data: SensorData):
    """Insert a new sensor data document."""
    result = collection.insert_one(data.dict())
    return {"id": str(result.inserted_id)}

@app.get("/data/{id}", response_model=dict)
def read_data(id: str):
    """Read sensor data by ID."""
    try:
        document = collection.find_one({"_id": ObjectId(id)})
        if not document:
            raise HTTPException(status_code=404, detail="Data not found")
        return serialize_doc(document)
    except Exception as e:
        raise HTTPException(status_code=400, detail="Invalid ID format")

@app.put("/data/{id}", response_model=dict)
def update_data(id: str, update: UpdateSensorData):
    """Update sensor data by ID."""
    try:
        result = collection.update_one({"_id": ObjectId(id)}, {"$set": update.dict()})
        if result.modified_count == 0:
            raise HTTPException(status_code=404, detail="Data not updated or not found")
        return {"message": "Data updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail="Invalid ID format")