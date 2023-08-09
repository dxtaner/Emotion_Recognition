import cvlib as cv
import cv2
import numpy as np
from keras.models import load_model
from PIL import Image
from tensorflow.keras.preprocessing.image import img_to_array

# Load pre-trained models for gender, race, and age detection
emotion_model = load_model("../emotionModel.h5")
race_model = load_model("../raceModel1.h5")
age_model = load_model("../ageModel1.h5")
gender_model = load_model("../genderModel.h5")

# Define dictionaries for labels
emotion_dict = {
    0: 'Kizgin',
    1: 'Igrenme',
    2: 'Korku',
    3: 'Mutlu',
    4: 'Uzgun',
    5: 'Sasirma',
    6: 'Dogal'
}

gender_dict = {
    0: "Erkek",
    1: "Kadin",
}

race_dict = {
    0: "Beyaz",
    1: "Siyah",
    2: "Asyali",
    3: "Hintli",
    4: "Diğer"
}

age_dict = {
    0: "0-20",
    1: "20-65",
    2: "65++"
}

font = cv2.FONT_HERSHEY_COMPLEX

# Webcam setup
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(3, 1920)
cap.set(4, 1080)

try:
    while cap.isOpened():
        ret, frame = cap.read()
        yuz, _ = cv.detect_face(frame)

        tonlama = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # tonlama ayarı

        for face in yuz:
            (x, y) = face[0], face[1]
            (w, h) = face[2], face[3]

            cv2.rectangle(frame, (x, y), (w, h), (0, 0, 255), 3)
            image_c = np.copy(tonlama[y:h, x:w])

            if (image_c.shape[0]) < 10 or (image_c.shape[1]) < 10:
                continue

            img = cv2.resize(image_c, (64, 64))
            img = img.astype("float") / 255.0
            img = img_to_array(img)
            img = np.expand_dims(img, axis=0)
            a = img

            # Gender detection
            conf_gender = gender_model.predict(a)[0]
            idx = np.argmax(conf_gender)
            gender = gender_dict[idx]
            gender = "{}:{:.2f}%".format(gender, conf_gender[idx] * 100)

            # Race detection
            conf_race = race_model.predict(a)[0]
            idx = np.argmax(conf_race)
            race = race_dict[idx]
            race = "{}:{:.2f}%".format(race, conf_race[idx] * 100)

            # Age detection
            conf_age = age_model.predict(a)[0]
            idx = np.argmax(conf_age)
            age = age_dict[idx]
            age = "{}:{:.2f}%".format(age, conf_age[idx] * 100)

            # Emotion detection
            center_img = np.array(Image.fromarray(image_c).resize([48, 48]))
            face_img = np.array(Image.fromarray(center_img).resize([48, 48]))
            face_gray = cv2.cvtColor(face_img, cv2.COLOR_RGB2GRAY)
            face_gray = np.expand_dims(face_gray, axis=-1)
            results = emotion_model.predict(face_gray.reshape(1, 48, 48, 1))

            # Get the emotion label and confidence percentage
            idx = np.argmax(results)
            emotion_label = emotion_dict[idx]
            confidence_percentage = np.max(results) * 100
            emotion_label = "{}:{:.2f}%".format(emotion_label, confidence_percentage)

            # Display face attributes
            cv2.putText(frame, f"{race}/{age}/{gender}/{emotion_label}", (x, y - 8), font, 0.8, (0, 255, 255), 2,
                        cv2.LINE_AA)

        cv2.imshow('Goruntu Tespiti', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    cap.release()
    cv2.destroyAllWindows()
