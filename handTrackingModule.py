import cv2
import mediapipe as mp
import time
# import streamlit as st
# FRAME_WINDOW = st.image([])



class handDetector():
    def __init__(self, mode=False, maxHands=2, modelComplexity=1, detectionCon=0.5, tractCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.modelComplex = modelComplexity
        self.detectionCon = detectionCon
        self.tractCon = tractCon

        self.mpHands = mp.solutions.hands
        self.handss = self.mpHands.Hands(self.mode, self.maxHands, self.modelComplex, self.detectionCon, self.tractCon)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.handss.process(imgRGB)
        # print(results.multi_hand_landmarks)

        if self.results.multi_hand_landmarks:
            for handLM in self.results.multi_hand_landmarks:
                if draw:
                    # print('o')
                    self.mpDraw.draw_landmarks(img, handLM, self.mpHands.HAND_CONNECTIONS)
        return img

    def findPosition(self, img, handNo=0, draw=False):
        lmList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                # print(id,lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                # print(id, cx, cy)
                lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)
        return lmList


def main():
    cap = cv2.VideoCapture(0)
    detector = handDetector()
    pTime = 0
    while True:
        success, img = cap.read()
        img = cv2.flip(img, 1)
        # img = detector.findHands(img, '*')
        img = detector.findHands(img,'*')
        lmList = detector.findPosition(img,draw=False)
        if len(lmList) != 0:
            print(lmList[8])

        # cTime = time.time()
        # fps = 1 / (cTime - pTime)
        # pTime = cTime
        # cv2.putText(img, str(int(fps)), (1, 70), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)

        cv2.imshow("Image", img)
        # FRAME_WINDOW.image(img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
