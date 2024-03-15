from fastapi import FastAPI, File, UploadFile
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()

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



MODEL=tf.keras.models.load_model("../model_data_augmeneted_version1")
CLASS_NAMES=["Potato___Early_blight","Potato___Late_blight","Potato___healthy"]


def read_files_as_image(data,target_size=(512,512)) -> np.ndarray:
    image= Image.open(BytesIO(data))
    image=image.resize(target_size)
    return(np.array(image))
    
    
    
    
@app.post("/predict")
async def predict(
    file: UploadFile= File(...)
):
    image= read_files_as_image(await file.read())
    image_batch= np.expand_dims(image,0)
    
    prediction= MODEL.predict(image_batch)
    predicted_class = CLASS_NAMES[np.argmax(prediction)]
    confidence = np.max(prediction)
    
    return {
        "class": predicted_class,
        "confidence": float(confidence)
    }
    