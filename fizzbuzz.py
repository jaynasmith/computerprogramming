user_number = int(input("Pick a number_"))

for i in range(1,100):
    if (i % user_number == 0):
        print("Hug")
    elif (i % 3 == 0) and (i % 5 == 0):
        print("FizzBuzz")
    elif (i % 3 == 0):
        print("Fizz")
    elif (i % 5 == 0):
        print("Buzz")
    else:
        print(i)