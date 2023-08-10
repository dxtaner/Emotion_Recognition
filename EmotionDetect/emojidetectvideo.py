import cv2
import cvlib as cv
import numpy as np
import pafy

from keras.models import load_model
from PIL import Image
from tensorflow.keras.preprocessing.image import img_to_array

model_best = load_model("emotionModel.h5")
font = cv2.FONT_HERSHEY_DUPLEX

emotion_dict = {
    0: 'Kizgin',
    1: 'Igrenme',
    2: 'Korku',
    3: 'Mutlu',
    4: 'Uzgun',
    5: 'Sasirma',
    6: 'Dogal'
}

url = 'https://www.youtube.com/watch?v=3fkEk8Qib1M'
vPafy = pafy.new(url)

play = vPafy.getbest(preftype="mp4")
kamera = cv2.VideoCapture(play.url)

while kamera.isOpened():
    ret,frame=kamera.read()

    yuz, confidence = cv.detect_face(frame)

    tonlama = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # tonlama ayarı

    for idx, face in enumerate(yuz):

        (x, y) = face[0], face[1]
        (w, h) = face[2], face[3]

        cv2.rectangle(frame, (x, y), (w, h), (0, 0, 255), 3)

        image_c = np.copy(tonlama[y:h, x:w])

        if (image_c.shape[0]) < 10 or (image_c.shape[1]) < 10:
            continue

        center_img = np.array(Image.fromarray(image_c).resize([48,48]))
        face_img = cv2.cvtColor(center_img,cv2.COLOR_GRAY2RGB)
        face_img = np.array(Image.fromarray(center_img).resize([48,48]))
        results = model_best.predict(face_img.reshape(1,48,48,1))

        cv2.putText(frame, 'Durum:{}({:.2f})'.format(emotion_dict[np.argmax(results)], np.max(results)),
                   (x, y - 10), font, 0.6, (0, 255, 0), 2)


    cv2.imshow("Webcam", frame)

    if (cv2.waitKey(30) & 0xFF == ord('q')):
        break

kamera.release()
cv2.destroyAllWindows()