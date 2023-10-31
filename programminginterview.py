Q1 = input("What is your first and last name?")
Q2 = input("Why do you want this job?")
Q3 = int(input("How many years have you been coding?"))

if Q3 < 3:
    print("I'm Sorry, but we require atleast 3 years of experience. Thank you for your time.")
    exit()


Q4 = input("What type of coding are you interested in?")
Q5 = input("What is your biggist weaknesses?")
Q6 = input("What are your biggist strengths?")
Q7 = input("How do you handle stress?")
Q8 = input("What should we hire you? What makes you unque?")
Q9 = input("Do you have any other current jobs?")
if Q9 == 'yes' or Q9 == 'Yes':
    Q9_pt2 = input("Are you willing to quit your current job for a full time position here? ")
    if Q9_pt2 == 'no' or Q9_pt2 == "No":
        print("I'm sorry, but this job requires alot of time that a secound or third job will not alllow. Thank you for your time.")
        exit()
    else:
        print("Excellent! That works perfectly!")

Q10 = int(input("What are you salary expectations?"))

