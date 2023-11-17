import random
words = []
with open('sowpods.txt','r') as f:
    line = f.readline()
    words.append(line)
    while line:
        line = f.readline()
        words.append(line)

word = random.choice(words)

guesses = []

turns = 6

while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print('__')
            failed += 1

    if failed == 0:
        print("You win! Good job! Maybe your mom will stop regretting you now!")
        print("the word was: " , word)
        exit()
        
    print()
    guess = input("Guess a Letter! ").upper()
    guesses.append(guess)

    if guess not in word:
        turns -= 1
        print("wrong. try again idiot.")
        print("You have ", turns ,"turns left")
   
    if turns == 0:
        print("you lose. imagine losing so hard. no wonder your dad left.")
        print("the word was: " , word)

