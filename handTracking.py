import cv2
import mediapipe as mp
import time
import streamlit as st
st.title('HI')

cap = cv2.VideoCapture(0)
FRAME_WINDOW = st.image([])
mpHands = mp.solutions.hands
handss = mpHands.Hands()
# mpHands = mp.solutions.hands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = handss.process(imgRGB)
    # print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLM in results.multi_hand_landmarks:
            for id, lm in enumerate(handLM.landmark):
                # print(id,lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                # print(id, cx, cy)
                if id == 0:
                    cv2.circle(img, (cx, cy), 35, (255, 0, 255), cv2.FILLED)
            mpDraw.draw_landmarks(img, handLM, mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (1, 70), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)

    # cv2.imshow("Image", img)
    FRAME_WINDOW.image(img)

    cv2.waitKey(1)
