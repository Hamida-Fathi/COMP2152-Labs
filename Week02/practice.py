import random

choices=["Rock, Paper, Scissors"]

userChoice= input("Enter your choice (1=Rock, 2-Paper, 3-Scissors):")
userChoice= int(userChoice)

computerChoice= random.randint(1,3)
userChoiceIndex= choices[userChoice-1]
computerChoiceIndex= choices[computerChoice-1]
if userChoice<1 or userChoice>3:
    print("Invalid choice! please choose btweeb 1 and 3")
elif computerChoiceIndex==0 