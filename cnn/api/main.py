from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8000",
    'http://127.0.0.1:8000'
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MODEL = tf.keras.models.load_model("../../cnn/taka1.keras")

CLASS_NAMES = ['10',
 '100',
 '1000',
 '2',
 '20',
 '200',
 '5',
 '50',
 '500']

@app.get("/ping")
async def ping():
    return "Hello, I am alive"

def read_file_as_image(data) -> np.ndarray:
    image = Image.open(BytesIO(data))
    # Resize the image to match the expected input shape of the model
    resized_image = image.resize((224, 224))
    image_array = np.array(resized_image)
   
    return image_array

@app.post("/predict")
async def predict(
    file: UploadFile = File(...)
):
    try:
        print(file)
        image = read_file_as_image(await file.read())
        img_batch = np.expand_dims(image, 0)
        
        predictions = MODEL.predict(img_batch)

        predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
        confidence = np.max(predictions[0])
        print(predicted_class)
        return {
            'class': predicted_class,
            'confidence': float(confidence)
        }
    except Exception as e:
        print(e)

if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8001)
