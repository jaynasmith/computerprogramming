import time
import random
print("Welcome traveler to the MAZE!")
print("Lets start with your name: ")
name = input()
print("Hello " +name+ " and welcome to the game.")
time.sleep(3)
print("")
print("Our story starts many many years ago with a young man.")
time.sleep(3)
print("")
print("A smart mischievievous young man who spread a rumor about a maze with the most amazing tresure.")
time.sleep(3)
print("")
print("A tresure that was never real.")
time.sleep(3)
print("")
print("Now the maze was real, of course. It would never be as funny if people realized that the rumor was a lie.")
time.sleep(3)
print("")
print("People sought out this maze and its tresure and many people found the maze.")
time.sleep(3)
print("")
print("Anyone who entered the maze never came back.")
time.sleep(3)
print("")
print(" ...")
print("")
time.sleep(3)
print("Not as funny now, in retrospect.")
time.sleep(4)
print("")
print("You heard this rumor and tried to find this maze.")
time.sleep(3)
print("")
print("You did.")
time.sleep(3)
print("")
print("Now you're stuck in the middle and can't find your way out. ")
print("")

hp = 100
inventory = []
inputs = ['w' , 'i']

def attack_ememy(player_health, enemy health):
    




while True:
        
    walk_input = input("Press 'w' to walk or 'i' to see inventory. ")
    if walk_input == 'w':

        if random.randint(1, 3) == 1:
            if random.randint(1, 3) == 1:
                print("You've run into a moving skeleton!")
                time.sleep(1.5)
                print("")
            elif random.randint(1, 3) == 2:
                print("You've ran into a walinhg shark!")
                time.sleep(1.5)
                print("")
            else:
                print("You've run into your dissapointed dad!") 
                time.sleep(1.5)
                print("")
        else:
            print("Just keep walking! You'll get there!")
            time.sleep(1.5)
            print("")
    elif walk_input == 'i':
        print(f"Your have {hp} health and {inventory} in your inventory.")
    