import cv2
import time
import os

from fingerCountModule import fingerCount
from gamePlayModule import gamePlayModule

count = fingerCount()
game = gamePlayModule()

def take_input():
    print("Enter your run number (1-6): ")
    run_taken = count.count()
    print(run_taken)
    return run_taken

def next_ball():
    # selected_number = input("Enter s : ")
    # if selected_number == "s":
    #     return True
    return True

def main():

    gamePlay = gamePlayModule()
    print("Choose 1 if you want to batting first")
    print("Choose 0 if you want to bowling first")


    choice = int(input("Enter Your Choice: "))

    total_ball = int(input("Enter total number of ball (1-12) to play the innings: "))
    # gamePlay.get_total_ball(total_ball)

    batting_score = gamePlay.first_innings(total_ball,choice,take_input,next_ball)

    gamePlay.second_innings(batting_score,total_ball,choice,take_input,next_ball)



if __name__ == "__main__":
    main()
