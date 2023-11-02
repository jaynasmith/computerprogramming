def main():
    Q1 = input("What is your first and last name? ")
    Q2 = input("Why do you want this job? ")
    Q3 = int(input("How many years have you been coding? "))
    if Q3 < 3:
        print("I'm Sorry, but we require atleast 3 years of experience. Thank you for your time.")
        exit()
    Q4 = input("What type of coding are you interested in? ")
    Q5 = input("What is your biggist weakness? ")
    Q6 = input("What is your biggist strength? ")
    Q7 = input("How do you handle stress? ")
    Q8 = input("What should we hire you? What makes you unque? ")
    Q9 = input("Do you have any other current jobs? ")
    if Q9 == 'yes' or Q9 == 'Yes':
        Q9_pt2 = input("Are you willing to quit your current job for a full time position here? ")
        if Q9_pt2 == 'no' or Q9_pt2 == "No":
            print("I'm sorry, but this job requires alot of time that a secound or third job will not alllow. Thank you for your time.")
            exit()
        else:
            print("Excellent! That works perfectly!")

    Q10 = int(input("What are your yearly salary expectations? "))
    if Q10 > 75000:
        Q10_pt2 = input("Sorry, but for a new higher thats a bit to high. Are you willing to go lower? ")
        if Q10_pt2 == 'no' or Q10_pt2 == 'No':
            print("Saddly we can't pay you that much. Thank you for your time.")
            exit()
        else:
            print("Great!")
    print(f"That's the end of our interview questions! I want to double check that your information matches what we have writen down.") 
    print(f"Question 1 you said your name was {Q1}.")
    print(f"Question 2 you said you wanted this job because {Q2}.")
    print(f"Question 3 you said you have been coding for {Q3}.")
    print(f"Question 4 you said that you are interested in {Q4} coding.")
    print(f"Question 5 you said your biggest weakness was {Q5}.")
    print(f"Question 6 you said your biggest strenght was {Q6}.")
    print(f"Question 7 you said you handle stress {Q7}.")
    print(f"Question 8 you said what makes you unique was {Q8}.")
    print(f"Question 9 you said {Q9} to having other jobs.")
    print(f"Question 10 you said that your yearly salary expectation was {Q10}")
    Q11 = input("Was this information all correct? ")
    if Q11 == 'no' or Q11 == 'No':
        print("I'm sorry about that. Lets try again.")
        main()
    else:
        print("Amazing! We'll get back to you later. Thank you for your time. Have a great day!")
        exit()

main()