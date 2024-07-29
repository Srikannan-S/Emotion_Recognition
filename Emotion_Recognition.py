
from facial_emotion_recognition import EmotionRecognition
import cv2

er=EmotionRecognition(device='cpu')

cam=cv2.VideoCapture(0)

while True:
    _,img=cam.read()

    img=er.recognise_emotion(img,return_type='BGR')

    cv2.imshow("Frame",img)

    key=cv2.waitKey(1)
    if key==27:
        break

cam.release()
cv2.destroyAllWindows()
