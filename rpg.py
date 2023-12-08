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

player_health = 100
enemy_health = 75
inventory = []
mob_drops = ['bones' , 'coins' , 'a t-shirt saying "Im your new step-dad"']

def attack_ememy(player_health, enemy_health):
    while True:
        if player_health > 0:
            your_attack = random.randint(10, 100)
            print(f"You attacked the enemy for {your_attack} damage!")
            enemy_health -= your_attack

        if enemy_health > 0:
            your_attack = random.randint(10, 100)
            print(f"The enemy attacked you for {your_attack} damage!")
            enemy_health -= your_attack

        if player_health <= 0:
            print("You die and become an obstical for the next traveler")
            break
        elif enemy_health <= 0:
            print("The villain dies by your hand!")
            print("You have earned 25 health and an item in you inventory!")
            player_health += 25
            inventory.append(random.choice(mob_drops))
            break

def attack_player(enemy_health, player_health):
    while True:
        if enemy_health > 0:
            your_attack = random.randint(10, 100)
            print(f"The enemy attacked you for {your_attack} damage!")
            enemy_health -= your_attack
        
        if player_health > 0:
                    your_attack = random.randint(10, 100)
                    print(f"You attacked the enemy for {your_attack} damage!")
                    enemy_health -= your_attack

        if player_health <= 0:
            print("You die and become an obstical for the next traveler")
            break
        elif enemy_health <= 0:
            print("The villain dies by your hand!")
            print("You have earned 25 health and an item in you inventory!")
            player_health += 25
            inventory.append(random.choice(mob_drops))
            break





while True:
        
    walk_input = input("Press 'w' to walk or 'i' to see inventory. ")
    if walk_input == 'w':

        if random.randint(1, 3) == 1:
            if random.randint(1, 3) == 1:
                print("You've run into a moving skeleton!")
                print("")
                time.sleep(1.5)
                fight_input = input("Would you like to fight or flee? (fight/flee) ")
                if fight_input == "fight":
                    attack_ememy(player_health, enemy_health)
                elif fight_input == "flee":
                    if random.randint(1,2) == 1:
                        print("Oh no! You couldnt run fast enough!")
                        attack_player(enemy_health, player_health)
                    else:
                        print("You ran like a coward.")
            elif random.randint(1, 3) == 2:
                print("You've ran into a walinhg shark!")
                print("")
                time.sleep(1.5)
                fight_input = input("Would you like to fight or flee? (fight/flee) ")
                if fight_input == "fight":
                    attack_ememy(player_health, enemy_health)
                elif fight_input == "flee":
                    if random.randint(1,2) == 1:
                        print("Oh no! You couldnt run fast enough!")
                        attack_player(enemy_health, player_health)
                    else:
                        print("You ran like a coward.")
            else:
                print("You've run into your dissapointed dad!") 
                print("")
                time.sleep(1.5)
                fight_input = input("Would you like to fight or flee? (fight/flee) ")
                if fight_input == "fight":
                    attack_ememy(player_health, enemy_health)
                elif fight_input == "flee":
                    if random.randint(1,2) == 1:
                        print("Oh no! You couldnt run fast enough!")
                        attack_player(enemy_health, player_health)
                    else:
                        print("You ran like a coward.")
        else:
            print("Just keep walking! You'll get there!")
            print("")
    elif walk_input == 'i':
        print(f"Your have {player_health} health and {inventory} in your inventory.")