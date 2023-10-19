from pydantic import BaseModel
class HealthCheckResponse(BaseModel):
    msg: str