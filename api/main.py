from fastapi import FastAPI, File, UploadFile
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf
from fastapi.middleware.cors import CORSMiddleware
import logging

app=FastAPI()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


origins =[
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



MODEL=tf.keras.models.load_model("../Saved_model_version1")
CLASS_NAMES=["Black Spot", "Downy mildew", "Fresh Leaf"]


def read_files_as_image(data, target_size=(512, 512)) -> np.ndarray:
    try:
        with Image.open(BytesIO(data)) as img:
            img = img.convert('RGB')  # Convert image to RGB mode
            original_size = img.size
            img = img.resize(target_size)
            logging.info(f'Image resized from {original_size} to {target_size}')
        return np.array(img, dtype=np.float32)
    except Exception as e:
        logging.error(f'Error processing image: {e}')
        raise
    
    
    
    
@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        image_data = await file.read()
        logging.info(f'Received image: {file.filename}')
        image = read_files_as_image(image_data)
        image_batch = np.expand_dims(image, 0)

        prediction = MODEL.predict(image_batch)
        predicted_class = CLASS_NAMES[np.argmax(prediction)]
        confidence = np.max(prediction)
        logging.info(f'Prediction: {predicted_class} with confidence {confidence}')

        return {"class": predicted_class, "confidence": float(confidence)}
    except Exception as e:
        logging.error(f'Prediction error: {e}')
        return {"error": str(e)}
    