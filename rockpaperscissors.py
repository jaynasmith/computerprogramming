import random
actions = ["rock" , "paper" , "scissors"]
com_action = random.choice(actions)
user_action = input("Enter a choice (rock , paper, scissors): ")
print(f"You chose {user_action}. The little boy in the digital box chooses {com_action}.")

if user_action == com_action:
    print(f"Both players chose {user_action}. It's a tie!")
elif user_action == "rock":
    if com_action == "scissors":
        print("Rock smashes scissors. You win! Hurray! Maybe your dad will come back now!")
    else:
        print("Paper covers rock. you lose. you absolute loser. your mom must be sp dissapointed in you.")
elif user_action == "paper":
    if com_action == "rock":
        print("Paper covers rock. You win! Hurray! Maybe your dad will come back now!")
    else:
        print("Scissors cut paper. you lose. you absolute loser. your mom must be sp dissapointed in you.")
elif user_action == "scissors":
    if com_action == "paper":
        print("Scissors cut paper. You win! Hurray! Maybe your dad will come back now!")
    else:
        print("Rock smashes scissors. you lose. you absolute loser. your mom must be sp dissapointed in you.")