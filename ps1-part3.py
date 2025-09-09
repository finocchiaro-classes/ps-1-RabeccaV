
def heart_rate(age, goal):
    max_HR=220-int(age)
    print("Yor maximum heart rate is:",max_HR)
    if goal=="S":
        print(f"Your target heart rate is between {0.8*max_HR} and {max_HR}")

    else:
        print(f"Your target heart rate is between {0.6*max_HR} and {max_HR*0.8}")

user_age=input("What is your age? ")
user_goal=input("Is your goal speed (S) or endurance (E)? ")

heart_rate(user_age,user_goal)
                
