import random

def take_input():
    selected_number = int(input("Enter your run number (1-6): "))
    return selected_number

def next_ball():
    selected_number = input("Enter s : ")
    if selected_number == "s":
        return True

class gamePlayModule():
    def __init__(self):
        self.total_ball = 0
        self.choice = 0
        self.run_input = 0
        self.selected_number = 0

    # def get_total_ball(self,total_ball):
    #     self.total_ball = total_ball
    # def take_input(self,func):
    #     selected_number = func
    #     return func



    def second_innings(self,total_score,ball_number,check_choice,take_input,next_ball):

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
                # selected_number = int(input("Enter your run number (1-6): "))
                if next_ball():
                    selected_number = take_input()

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
                # selected_number = int(input("Enter your run number (1-6): "))
                if next_ball():
                    selected_number = take_input()
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

    def first_innings(self,ball_number,choice,take_input,next_ball):

        print("Let's start your innings! ")

        computer_score = 0
        flag = True

        if choice==0:
            print("!------------------------------------------Computer Batting--------------------------------!")
            while ball_number > 0:
                global selected_number
                # selected_number = int(input("Enter your run number (1-6): "))
                if next_ball():
                    selected_number = take_input()
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
                # selected_number = int(input("Enter your run number (1-6): "))
                if next_ball():
                    selected_number = take_input()
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
