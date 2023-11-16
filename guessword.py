import random

words = ['yellow', 'computer', 'guess', 'programming',
         'python', 'math', 'athlete', 'conditioner',
         'weather', 'water', 'board', 'mother']

word = random.choice(words)

guesses = []

turns = 10

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
    guess = input("Guess a Letter!")
    guesses += guess

    if guess not in word:
        turns -= 1
        print("wrong. try again idiot.")

    if turns == 0:
        print("you lose. imagine losing so hard. no wonder your dad left.")