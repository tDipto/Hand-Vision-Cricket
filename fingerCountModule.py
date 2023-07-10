import cv2
import time
import os
import handTrackingModule as htm

class fingerCount():
    def __init__(self):
        self.detector = htm.handDetector(detectionCon=0.75)
        self.wCam, self.hCam = 640, 480
        self.cap = cv2.VideoCapture(0)
        self.cap.set(3, self.wCam)
        self.cap.set(4, self.hCam)
        self.tipIds = [4, 8, 12, 16, 20]
        self.pTime = 0
        self.fingerPath = 'finger'
        self.myList = os.listdir(self.fingerPath)
        # print(myList)
        self.overlayList = []

    def count(self):
        CountFinger=False
        totalFingers=0
        for i in self.myList:
            image = cv2.imread(f'{self.fingerPath}/{i}')
            # print(f'{fingerPath}/{i}')
            self.overlayList.append(image)
        # print(len(overlayList))
        flag = False
        while True:
            success, img = self.cap.read()
            img = cv2.flip(img, 1)

            img = self.detector.findHands(img)
            lmList = self.detector.findPosition(img, draw=False)
            # print(lmList)


            if len(lmList):
                fingers = []

                # thumb
                if lmList[self.tipIds[0]][1] < lmList[self.tipIds[0] - 2][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)
                # except thumb
                for i in range(1,5):
                    if lmList[self.tipIds[i]][2] < lmList[self.tipIds[i] - 2][2]:
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
                # print(totalFingers)
                h, w, c = self.overlayList[totalFingers-1].shape
                img[0:h, 0:w] = self.overlayList[totalFingers-1]

                cv2.rectangle(img, (35, 320), (110, 425), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, str(totalFingers), (45, 400), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 5)



            # cTime = time.time()
            # pTime = cTime
            # fps = 0
            # if cTime - pTime:
            #     fps = 1 / (cTime - pTime)
            #
            # cv2.putText(img, f'FPS: {int(fps)}', (400, 70), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

            cv2.imshow("Image", img)
            # cv2.waitKey(1)
            # wait_time = 5
            # cv2.waitKey(wait_time * 1)
            key = cv2.waitKey(1)
            if key == ord('s'):
                CountFinger = True
            if flag:
                break
        wait_time = 2
        start_time = time.time()

        # Hold the screen until the specified amount of time has passed
        while True:
            if (time.time() - start_time) > wait_time:
                break


        # cv2.destroyAllWindows()
        return totalFingers





def main():

    finger = fingerCount()
    print("HI")
    print(finger.count())
    # print(number)



if __name__ == "__main__":
    main()
