import cv2
import mediapipe as mp
import time
import streamlit as st
FRAME_WINDOW = st.image([])
import handTrackingModule as htm
global submit_button

tipIds = [4, 8, 12, 16, 20]
totalFingers = 0

startGame = True

if startGame:
    submit_button = False
    submit_button = st.button('Next')
    cap = cv2.VideoCapture(0)
    detector = htm.handDetector()
    pTime = 0

    while True:
        success, img = cap.read()
        img = cv2.flip(img, 1)
        # img = detector.findHands(img, '*')
        img = detector.findHands(img)
        lmList = detector.findPosition(img,draw=False)

        fingers = []
        CountFinger = False
        # global submit_button
        if submit_button:
            CountFinger = True


        if len(lmList) != 0:
            print(lmList[8])
                # thumb
            if lmList[tipIds[0]][1] < lmList[tipIds[0] - 2][1]:
                fingers.append(1)
            else:
                fingers.append(0)
            # except thumb
            for i in range(1,5):
                if lmList[tipIds[i]][2] < lmList[tipIds[i] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)
            # print(fingers)

            if CountFinger:
                if fingers[0] and fingers[1]==0:
                   totalFingers = 6
                   flag = True
                else:
                    totalFingers = fingers.count(1)
                    flag = True
                print(totalFingers)
                CountFinger = False
                submit_button = False
                # with col2:
                st.write(totalFingers)


        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, str(int(fps)), (1, 70), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)

        # cv2.imshow("Image", img)
        # with col3:

        # with col1:
        FRAME_WINDOW.image(img)
        cv2.waitKey(1)

#
# if __name__ == "__main__":
#     main()
