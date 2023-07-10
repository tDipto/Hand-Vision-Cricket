import cv2
import time
import os
import handTrackingModule as htm
import random


wCam, hCam = 640, 480
cap = cv2.VideoCapture(0)
# address ='http://192.168.0.101:8080/video'
# cap.open(address)
cap.set(3, wCam)
cap.set(4, hCam)

fingerPath = 'finger'
myList = os.listdir(fingerPath)
# print(myList)

overlayList = []
for i in myList:
    image = cv2.imread(f'{fingerPath}/{i}')
    # print(f'{fingerPath}/{i}')
    overlayList.append(image)
# print(len(overlayList))

detector = htm.handDetector(detectionCon=0.75)

tipIds = [4, 8, 12, 16, 20]
pTime = 0
flag = False
totalFingers = 0
CountFinger = False

totalRun = 0
pc_run = 0
def mainGame(p_run):
    global  totalRun,pc_run
    pc_run = random.randint(1,6)
    if p_run != pc_run:
        totalRun = totalRun + p_run
    else:
        totalRun = 0
    return totalRun


while True:
    imgBG = cv2.imread('bg/main.jpg')
    imgBG = cv2.resize(imgBG,(1000,500))

    success, img = cap.read()
    img = cv2.flip(img, 1)
    # img = cv2.resize(img,(400,200))
    img = cv2.resize(img,(0,0),None,.61,.61)
    img = img[20:240,:]

    imgBG[136:356,70:460] = img

    img = detector.findHands(img,"*")
    lmList = detector.findPosition(img, draw=True)
    # print(lmList)

    if len(lmList):
        fingers = []

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
            getRun= mainGame(totalFingers)
            print(getRun)



    h, w, c = overlayList[pc_run-1].shape
    imgBG[54:314, 680:840] = overlayList[pc_run-1]

    cv2.rectangle(img, (35, 320), (110, 425), (0, 255, 0), cv2.FILLED)
    cv2.putText(img, str(totalFingers), (45, 400), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 5)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (400, 70), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)


    # cv2.imshow("Image", img)
    cv2.imshow('bg',imgBG)
    key = cv2.waitKey(1)


    imgBG[136:356,70:460] = img
    if key == ord('s'):
        CountFinger = True
        # cv2.destroyAllWindows()

    elif key == ord('b'):
        break
    # if flag:
    #     break
