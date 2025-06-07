# #user input

# # a=input('Did you study python: \n')
# # print(a)
# print('\n ###################################################')


# #Rock Paper scissor game

import random 
import sys 
from enum import Enum

class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSOR = 3

print(RPS(2))
print(RPS.ROCK)
print(type(RPS))
print(RPS.ROCK.value)

playerchoice = input("Print your choice: \n 1 for Rock \n 2 for paper \n 3 for Scissor \n")
print(playerchoice)
print(type(playerchoice))

player = int(playerchoice)
if player < 1 or player > 3:
        sys.exit("ERROR - You must enter 1 or 2 or 3")

computerchoice = random.choice("123")
print(computerchoice)
computer = int(computerchoice)


print("")
print("You Chose " + str(RPS(player)).replace("RPS.","") + " ."+ "Python Choose " + str(RPS(computer)).replace("RPS.","") + ".")
print("")

if player == 1 and computer == 3:
    print ('🎉You Won')
elif player == 1 and computer == 2:
        print ('🎉You Lose')
elif player == 2 and computer == 1:
          print ('🎉You Won')
elif player == 2 and computer == 3:
                 print ('🎉You Lose')
elif player == 3 and computer == 2:
                         print ('🎉You Won')
elif player == 3 and computer == 1:
                         print ('🎉You Lose')
elif player == computer:
                                 print ('🎉Tie')

print("Game End")
               



