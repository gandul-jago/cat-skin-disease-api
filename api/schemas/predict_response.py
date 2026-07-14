from pydantic import BaseModel


class Probability(BaseModel):
    class_name: str
    confidence: float


class PredictionResponse(BaseModel):
    prediction: str
    confidence: float
    probabilities: list[Probability]