# Bangladeshi Banknote Detection for the Deaf-Blind Community of Bangladesh


We have trained a machine learning model and used the Python Django framework to create an AI decision-making system for real-time banknote identification. The AI application is deployed across two servers: one for the frontend and another for the backend, which utilizes FastAPI. Our ML model, served through FastAPI, handles the real-time processing of banknote images. The AI application captures real-time images of banknotes and sends them to the FastAPI backend for classification, with the results returned in JSON format. These results are then displayed on the Django frontend interface. The backend processes the results, and an Arduino Uno module uses the data to activate a shaftless vibration motor with a specific pattern. The duration between each vibration corresponding to a detected banknote is set to 1000 milliseconds.

Furthermore, Bangladesh Bank has incorporated unique tactile markers on banknotes for the visually impaired, which our AI program will enhance through vibration patterns. We have implemented a manual vibration pattern for detecting specific banknotes. The setup includes the Arduino Uno module with a shaftless vibration motor, an Arduino camera module, and the AI application. A video demonstration of our prototype in action can be viewed on YouTube at this link: https://youtube.com/shorts/b7nMWwEtNm4?si=LCQZiK8RscSzADCU.






