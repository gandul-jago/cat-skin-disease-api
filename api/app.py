from io import BytesIO

from fastapi import FastAPI, UploadFile, File
from PIL import Image
from api.core.security import validate_image
from api.core.database import SessionLocal
from api.models_api.prediction_history import PredictionHistory
from api.services.prediction import predict
from api.schemas.predict_response import PredictionResponse
from api.core.database import engine
from api.models_api.prediction_history import Base
from sqlalchemy import desc


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Cat Disease API",
    version="1.0.0"
)


@app.get("/")
def root():

    return {
        "message": "Cat Disease API is running"
    }


@app.post("/predict")
async def predict_image(
    image: UploadFile = File(...)
):

    img = await validate_image(image)

    result = predict(img)

    db = SessionLocal()

    try:
        history = PredictionHistory(
            image=image.filename,
            prediction=result["prediction"],
            confidence=result["confidence"]
        )

        db.add(history)
        db.commit()

    finally:
        db.close()

    return result

@app.get("/history")
def get_history():

    db = SessionLocal()

    try:
        history = (
            db.query(PredictionHistory)
            .order_by(desc(PredictionHistory.created_at))
            .all()
        )

        return [
            {
                "id": item.id,
                "image": item.image,
                "prediction": item.prediction,
                "confidence": float(item.confidence),
                "created_at": item.created_at
            }
            for item in history
        ]

    finally:
        db.close()