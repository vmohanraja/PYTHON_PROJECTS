from random import randint
def intro():
    logo="""       ___                       _   _                __                 _               
      / _ \_   _  ___  ___ ___  | |_| |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
     / /_\/ | | |/ _ \/ __/ __| | __| '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
    / /_\\| |_| |  __/\__ \__ \ | |_| | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
    \____/ \__,_|\___||___/___/  \__|_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|                                                                   
    """
    game=("  Welcome to the number guessing game!\n"
          "  I'm thinking of a number between 1 to 100 ")
    print(logo)
    print(game)
intro()
def game_start():
    if difficulty_level == "easy":
        level=9
        print("You will be given 10 attempts ")
    elif difficulty_level=="hard":
        level=4
        print("You will be given 5 attempts in this level")
    my_guess = (randint(1,100))
    game = False
    while game is False:
        guess=int(input("Make a guess: "))
        levels = f"You have {level} attempts left"
        if level==0:
            print(f"You lost there were no attempts left:(  the number was {my_guess}.")
            break

        if guess==my_guess:
            print("You won!!")
            print(f"The number is {my_guess}.")
            game = True
            break
        elif guess> my_guess:
            print("Too High!?")
            level -= 1
        elif guess< my_guess:
            print("Too Low!?")
            level -= 1
        print(levels)
difficulty_level= input("  Choose the difficulty: type 'easy' or 'hard': ")
if difficulty_level== "easy" or difficulty_level=="hard":
    game_start()
else:
    print("choose the difficulty correctly!!! ")
