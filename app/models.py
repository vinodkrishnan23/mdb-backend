from pydantic import BaseModel, Field
from typing import Dict, Any

class SensorData(BaseModel):
    timestamp: str
    ship_id: str
    engine_id: str
    system: str
    sensors: Dict[str, Dict[str, Any]]

class UpdateSensorData(BaseModel):
    sensors: Dict[str, Dict[str, Any]] = Field()
