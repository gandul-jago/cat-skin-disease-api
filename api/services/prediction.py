import numpy as np
import tensorflow as tf
from pathlib import Path
from PIL import Image

MODEL_PATH = "../artifacts/cat_skin_efficientnetb0.keras"

CLASS_NAMES = [
    "Flea Allergy",
    "Health",
    "Ringworm",
    "Scabies"
]


BASE_DIR = Path(__file__).resolve().parent.parent.parent

MODEL_PATH = BASE_DIR / "artifacts" / "cat_skin_efficientnetb0.keras"

model = tf.keras.models.load_model(MODEL_PATH)


def preprocess(image: Image.Image):

    image = image.convert("RGB")
    image = image.resize((224, 224))

    img = np.array(image, dtype=np.float32)

    img = tf.keras.applications.efficientnet.preprocess_input(img)

    img = np.expand_dims(img, axis=0)

    return img


def predict(image: Image.Image):

    img = preprocess(image)

    pred = model.predict(img, verbose=0)[0]

    idx = np.argmax(pred)

    probs = []

    for i in range(len(CLASS_NAMES)):
        probs.append({
            "class_name": CLASS_NAMES[i],
            "confidence": round(float(pred[i] * 100), 2)
        })

    probs.sort(
        key=lambda x: x["confidence"],
        reverse=True
    )

    return {
        "prediction": CLASS_NAMES[idx],
        "confidence": round(float(pred[idx] * 100), 2),
        "probabilities": probs
    }