import cv2
import time
import os
import streamlit as st
FRAME_WINDOW = st.image([])

from fingerCountModule import fingerCount
from gamePlayModule import gamePlayModule

count = fingerCount()
game = gamePlayModule()

def take_input():
    # print("Enter your run number (1-6): ")
    st.write('Enter your run number (1-6): ')
    run_taken = count.count()
    print(run_taken)
    return run_taken

widget_id = (id for id in range(1, 100_00))
def next_ball():
    try_ball = st.button("Enter",key=widget_id)
    if try_ball:
        return True

def main():

    gamePlay = gamePlayModule()
    # print("Choose 1 if you want to batting first")
    # print("Choose 0 if you want to bowling first")
    option = st.selectbox(
    'Choose 1 if you want to batting first '
    'Choose 0 if you want to bowling first',
    ('0', '1'))

    # choice = int(input("Enter Your Choice: "))
    choice = int(option)

    # total_ball = int(input("Enter total number of ball (1-12) to play the innings: "))
    option2 = st.selectbox(
    'Enter total number of ball (1-12) to play the innings: ',
    ('0', '1','2','3','4','5','6'))
    total_ball = int(option2)

    batting_score = gamePlay.first_innings(total_ball,choice,take_input,next_ball)

    gamePlay.second_innings(batting_score,total_ball,choice,take_input,next_ball)



if __name__ == "__main__":
    main()
