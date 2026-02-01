import os
import time
"""
Project3
Student: Israel Jose Betancourt

MY EXPERIENCE IN THIS PROGRAMM :
It wasn't easy; at first, I didn't understand much. 
I was completely lost trying to organize my ideas and translate them into Python code. 
I improved my code by doing a lot of research. I'm very sorry I didn't deliver this project on time, but I'm very happy with what I did.
At first, it wouldn't compile. I did everything, and when I saw a bunch of errors, I got frustrated. 
I thought I wouldn't finish it on time, but here it is. Thank you so much for everything. 

I showed it to my wife and sister and they loved it; they gave me great feedback. 
Even though it's all in English, they enjoyed playing it.

"""

# name of the game

title = r"""
  ____  _   _ ____ _____ _____ ____  ____  ___    _    
 / ___|| | | | __ )_   _| ____|  _ \|  _ \|_ _|  / \   
 \___ \| | | |  _ \ | | |  _| | |_) | |_) || |  / _ \  
  ___) | |_| | |_) || | | |___|  _ <|  _ < | | / ___ \ 
 |____/ \___/|____/ |_| |_____|_| \_\_| \_\___/_/   \_\ 
                                                       
"""
print(f"\033[1;32m{title}\033[0m")

# intro of game and welcome to the game.

print("Welcome to Subterria!")
print("Prepare for a new adventure in the depths of the Neon Caves.")
print("Theses caves were designed so that whoever enters can never leave.")
print("Your goal on this Journey is to escape alive. One wrong decision nd you'll lose the game.")

input("\033[5m\n[ PRESIONA ENTER PARA COMENZAR ]\033[0m")
os.system('cls' if os.name == 'nt' else 'clear')

#Started

name_player = str(input("\nWhat is the name of your character? "))
name_player = name_player.capitalize()

# level 1
print(f"\n{name_player}, you face three fearsome and dark caves.") 
choice_1 = input("Where would you like to go? (LEFT / CENTER / RIGHT) ").lower()

# path left
if choice_1 == "left":
    print("\nYou arrive at an acid river with an old BRIDGE and a rusty RAFT")
    left_path_2 = input("What do you choose? (BRIDGE OR RAFT) ").lower()
     # level 2
    if left_path_2 == "bridge":
        print("\nThe bridge creaks... You see a gap you can jump through or keep walking.")
        left_path_3 = input("What will you do? (JUMP OR WALKING) ").lower()
        if left_path_3 == "jump":
            print(f"\n{name_player} managed to cross before it collapsed! But there's no way out.")
        else:
            print(f"\nThe bridge broke beneath your feet. GAME OVER.")
    elif left_path_2 == "raft":
        choice_raft = input(f"\nThe acid is rising, will you JUMP oR STAY put? ").lower()
        if choice_raft == "jump":
            print(f"\nThe acid consumed you. You have lost.")
        else: 
            print("\nYou lost, better luck next time.")

# path right
elif choice_1 == "right":
    print("\nA guardian robot is blocking the way. Are you going to fight it or hack it?")
    right_path_2 = input("The choice is yours (FIGHT OR HACK): ").lower()
    # level 2
    if right_path_2 == "hack":
        print("\nThe system asks you for a code: 1234 or 0000?")
        right_path_3 = input("Introduce el codigo: ")
        
        if right_path_3 == "0000":
            print("\nIt is correct! The robot will guide you to the exit. You win!")
        # level 3
        elif right_path_3 == "1234": 
            print("\nIncorrect code. The robot activated its laser. GAME OVER.")
        else:
            print("\nInvalid code. The robot self-destructed with you inside.")
    else:
        print("\nYou tried to fight a metal giant? Bad idea. GAME OVER.")

# path center
elif choice_1 == "center":
    print("\nYou find a large room full of treasures and see a locked door.")
    center_path_2 = input("Will you find the KEY, or BREAK down the door? ").lower()
     # level 2
    if center_path_2 == "key":
        print("\nYou found the key! But it triggered an arrow trap.")
        center_path_3 = input("What is your reaction? (RUN OR DUCK) ").lower()
         # level 3
        if center_path_3 == "duck":
            print("\nThe arrows flew past you. The door opens. YOU WON!")
        else:
            print("\nYou were too slow. GAME OVER.")
    else:
        print("\nThe door was made of neon steel. Your arm broke. You've lost.")

else:
    print("\nThat's not a valid option. The shadow monsters have you.")