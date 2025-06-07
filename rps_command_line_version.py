# #Rock Paper scissor game

import random 
import sys 
from enum import Enum

#game_count = 0 #global variable

def rps(name = 'PlayerOne'):
    game_count = 0
    python_wins = 0
    player_wins = 0

    def game_function():
            nonlocal name
            nonlocal player_wins ##closure
            nonlocal python_wins ##closure
            
            class RPS(Enum):
                ROCK = 1
                PAPER = 2
                SCISSOR = 3
                
            print(RPS(2))
            print(RPS.ROCK)
            print(type(RPS))
            print(RPS.ROCK.value)
            playerchoice = input(f"\n{name},Please nter...\n Print your choice: \n 1 for Rock \n 2 for paper \n 3 for Scissor \n")
            print(playerchoice)
            print(type(playerchoice))

            if playerchoice not in ["1","2","3"]:
                print("You must enter 1 or 2 or 3")
                return game_function
            player = int(playerchoice)
            if player < 1 or player > 3:
                sys.exit("ERROR - You must enter 1 or 2 or 3")

            computerchoice = random.choice("123")
            print(computerchoice)
            computer = int(computerchoice)


            print("")
            print(f"\n {name} Chose {str(RPS(player)).replace('RPS.','').title()}")
            print(f" Python Choose {str(RPS(computer)).replace('RPS.','')}")
            print("")

            def game_players(player,computer):
                nonlocal name
                nonlocal player_wins ##closure
                nonlocal python_wins ##closure

                if player == 1 and computer == 3:
                    player_wins += 1
                    return f"🎉{name} Won"
                elif player == 1 and computer == 2:
                        python_wins += 1
                        return f"😒{name} Lost"
                elif player == 2 and computer == 1:
                        player_wins += 1
                        return f"🎉{name} Won"
                elif player == 2 and computer == 3:
                        python_wins += 1
                        return f"😒{name} Lost"
                elif player == 3 and computer == 2:
                        player_wins += 1
                        return f"🎉{name} Won"
                elif player == 3 and computer == 1:
                        python_wins += 1
                        return f"😒{name} Lost"
                elif player == computer:
                        return "😊Tie"
                return "Game End"
            
            game_result = game_players(player,computer) 
            print(game_result)
            nonlocal game_count #closure
            game_count += 1
            print(f"\nPlayer Wins: {str(player_wins)}")
            print(f"Python Wins: {str(python_wins)}")
            print(f"Game_Count: {game_count}")

            while True:
                    play_again = input("\n Play again? \n Y for Yes or \n Q to Quit \n\n")
                    if play_again.lower() not in ["y","q"]:
                          continue
                    else:
                          break
            if play_again.lower() == "y":
                return game_function()
            else:
                    print("\n 🎉🎉🎉🎉 ")
                    print("Thank you for playing! \n")
                    if __name__ == "__main__":
                          sys.exit("Bye! 👋👋")
                    else:
                          return
                    
    return game_function

#play= rps()

#play()

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Provides a Personalized game")

    parser.add_argument("-n", "--name", metavar="name",required=True, help="The name of the person to greet")

    args = parser.parse_args()
    rock_paper_scissor= rps(args.name)
    rock_paper_scissor()


