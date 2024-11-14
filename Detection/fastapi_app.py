from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf
import serial.tools.list_ports
import serial

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

MODEL = tf.keras.models.load_model("D:/cnn/taka1.keras")

CLASS_NAMES = ['10', '100', '1000', '2', '20', '200', '5', '50', '500']

@app.get("/ping")
async def ping():
    return "Hello, I am alive"

def read_file_as_image(data) -> np.ndarray:
    image = Image.open(BytesIO(data))
    resized_image = image.resize((224, 224))
    image_array = np.array(resized_image)
    return image_array

@app.post("/predict")
async def predict(
    file: UploadFile = File(...)
):
    try:
        image = read_file_as_image(await file.read())
        img_batch = np.expand_dims(image, 0)
        predictions = MODEL.predict(img_batch)
        predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
        return predicted_class
    except Exception as e:
        print(e)

if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8001)

    # Serial communication with Arduino
    ports = serial.tools.list_ports.comports()
    serialInst = serial.Serial()
    portsList = []

    for one in ports:
        portsList.append(str(one))
        print(str(one))

    com = input("Select Com Port for Arduino #: ")

    for i in range(len(portsList)):
        if portsList[i].startswith("COM" + str(com)):
            use = "COM" + str(com)
            print(use)

    serialInst.baudrate = 9600
    serialInst.port = use
    serialInst.open()

    while True:
        predicted_class = predict()  # Call predict function to get the predicted class
        command = predicted_class  # Assign the predicted class to the command
        serialInst.write(command.encode('utf-8'))

        if command == 'exit':
            exit()
