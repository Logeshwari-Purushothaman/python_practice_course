import sys
from guess_number_game import guess_game
from rps_command_line_version import rps

def play_game(name = 'PlayerOne'):
    Welcome_back = False

    while True:
        if Welcome_back == True:
            print(f"\n {name} Welcome back to the Arcade Menu:")

        playerchoice = input("\n Please choose a game \n 1 for Rock Paper Scissor Game \n 2 for Guess my number game and x to exit the arcade ")

        if playerchoice not in ["1","2","x"]:
                print(f"\n {name} Please only enter 1 or 2 or x")
                return play_game(name)
            
        Welcome_back = True

        if playerchoice == "1":
             rock_paper_scissor = rps(name)
             rock_paper_scissor()
        elif playerchoice == "2":
            guess_number = guess_game(name)
            guess_number()
        else:
            print("\n See you next time\n")
            sys.exit(f"Bye {name}! 👋")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Provides a Personalized game experience.")

    parser.add_argument('-n', '--name', metavar='name',required=True, help='The name of the person playing game.')

    args = parser.parse_args()
    
    print(f"\n {args.name} Welcome to the Arcade!")
    play_game(args.name)
