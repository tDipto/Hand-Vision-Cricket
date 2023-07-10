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

def second_innings(total_score,ball_number,check_choice):

    chess_score = 0

    if total_score == 0:
        total_score = 1
    else:
        total_score+=1

    # print(f'You need to {total_score} runs to win. Let\'s play the game!')


    if check_choice == 0:
        flag = True
        print("------------------------------------Target----------------------------------------")
        print(f'You need to {total_score} runs to win. Let\'s play the game!')
        print("!--------------------------Player Batting && Computer Bowling--------------------------------!")

        while ball_number > 0 and flag==True:
            selected_number = int(input("Enter your run number (1-6): "))
            random_number = random.randint(1,6)

            print("Computer's selected ball: ", random_number)

            if random_number == selected_number:
                print("Opps! You're are out!")
                print("Your total score is : ", chess_score)
                flag = False

                if chess_score < total_score:
                   print("You have lost the game!")
                   break
                if chess_score==total_score:
                    print("Match drawn")
                    break
            else:
                chess_score = chess_score + selected_number

                if chess_score > total_score:
                    print("Hurrah! You have won the game!")
                    flag = False
                    break
                print(f'You need {total_score - chess_score} more runs to win from {ball_number - 1} balls')
            ball_number = ball_number - 1

            if chess_score < total_score and ball_number==0:
                print("You have lost the game!")

    else:
        flag = True
        print("------------------------------------Target----------------------------------------")

        print(f'Computer need to {total_score} runs to win. Let\'s play the game!')

        print("!----------------------Player Bowling && Computer Batting----------------------------------!")

        while ball_number > 0 and flag==True:
            selected_number = int(input("Enter your ball number (1-6): "))
            random_number = random.randint(1,6)

            print("Computer's selected run: ", random_number)

            if random_number == selected_number:
                print("Opps! Computer is out!")
                print("Computer total score is : ", chess_score)
                flag = False

                if chess_score < total_score:
                   print("Computer have lost the game!")
                   break
                if chess_score==total_score:
                    print("Match drawn")
                    break
            else:
                chess_score = chess_score + random_number

                if chess_score > total_score:
                    print("Hurrah! Computer have won the game!")
                    flag = False
                    break
                print(f'Computer need {total_score - chess_score} more runs to win from {ball_number - 1} balls')

            ball_number = ball_number - 1

            if chess_score < total_score and ball_number==0:
                print("Computer lost the game!")



def first_innings(ball_number,choice):

    print("Let's start your innings! ")

    computer_score = 0
    flag = True

    if choice==0:
        print("!------------------------------------------Computer Batting--------------------------------!")
        while ball_number > 0:
            selected_number = int(input("Enter your ball number (1-6): "))
            random_number = random.randint(1,6)
            print("Computer's selected run: ", random_number)
            if random_number == selected_number:
                print("Opps! Computers out!")
                print("Computer's total score is : ", computer_score)
                flag = False
                break
            else:
                computer_score = computer_score + random_number
                print("Computer's current score: ", computer_score)
                print("Your balls left: ",ball_number-1)
            ball_number-=1
    else:
        print("!----------------------------------------Player Batting---------------------------------------!")
        while ball_number > 0:
            selected_number = int(input("Enter your run number (1-6): "))
            random_number = random.randint(1,6)
            print("Computer's selected ball: ", random_number)
            if random_number == selected_number:
                print("Opps! You're are out!")
                print("Your total score is : ", computer_score)
                break
            else:
                computer_score = computer_score + selected_number
                print("Your current score: ", computer_score)
                print("Computer's balls left: ",ball_number-1)
            ball_number-=1
    return computer_score




def mainGame(p_run):
    print("Choose 1 if you want to batting first")
    print("Choose 0 if you want to bowling first")


    choice = int(input("Enter Your Choice: "))


    total_ball = int(input("Enter total number of ball (1-12) to play the innings: "))

    batting_score = first_innings(total_ball,choice)

    second_innings(batting_score,total_ball,choice)


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
