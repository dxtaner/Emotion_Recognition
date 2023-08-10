import cv2
import cvlib as cv
import numpy as np
from keras.models import load_model
from PIL import Image
from tensorflow.keras.preprocessing.image import img_to_array

font = cv2.FONT_HERSHEY_DUPLEX

# Load emotion detection model
model_best = load_model("emotionModel.h5")
emotion_dict = {
    0: 'Kizgin',
    1: 'Igrenme',
    2: 'Korku',
    3: 'Mutlu',
    4: 'Uzgun',
    5: 'Sasirma',
    6: 'Dogal'
}

# Load the emoji images
emoji_images = {}
for emotion_label in emotion_dict.values():
    emoji_images[emotion_label] = cv2.imread(f"./emoji/{emotion_label.lower()}.png", cv2.IMREAD_UNCHANGED)

# Initialize the webcam feed
kamera = cv2.VideoCapture(0)
kamera.set(3, 1920)
kamera.set(4, 1080)

# ... (previous code) ...

while kamera.isOpened():
    ret, frame = kamera.read()

    # Convert the frame to grayscale for emotion detection
    tonlama = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Perform face detection
    yuz, confidence = cv.detect_face(frame)

    for idx, face in enumerate(yuz):
        (x, y) = face[0], face[1]
        (w, h) = face[2], face[3]

        # Emotion detection
        image_c = np.copy(tonlama[y:h, x:w])

        if (image_c.shape[0]) < 10 or (image_c.shape[1]) < 10:
            continue

        center_img = np.array(Image.fromarray(image_c).resize([48, 48]))
        face_img = cv2.cvtColor(center_img, cv2.COLOR_GRAY2RGB)
        face_img = np.array(Image.fromarray(center_img).resize([48, 48]))
        results = model_best.predict(face_img.reshape(1, 48, 48, 1))

        # Draw emotion label on the frame
        cv2.putText(frame, 'Durum:{}({:.2f})'.format(emotion_dict[np.argmax(results)], np.max(results)),
                    (x, y - 10), font, 0.6, (0, 255, 0), 2)

        # Add the corresponding emoji based on the detected emotion
        emotion_label = emotion_dict[np.argmax(results)]
        emoji_img = emoji_images.get(emotion_label)
        if emoji_img is not None:
            # Resize the emoji image to match the size of the ROI
            emoji_img_resized = cv2.resize(emoji_img, (w, h))

            overlay = np.zeros_like(frame)
            overlay[y:y + h, x:x + w] = emoji_img_resized

            # Combine the frame and overlay using alpha blending
            frame = cv2.addWeighted(frame, 1, overlay, 0.6, 0)

    # Display the modified frame with emojis and face attributes
    cv2.imshow('Goruntu Tespiti', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

kamera.release()
cv2.destroyAllWindows()

