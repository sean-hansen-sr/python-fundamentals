import random

computer_choice = random.choice(['rock', 'paper', 'scissors'])
user_choice = input("Do you want rock, paper, or scissors:\n")

print("Computer choice: " + computer_choice)

if computer_choice == user_choice:
    print("It's a tie!")
elif user_choice == 'rock' and computer_choice == 'scissors':
    print("User wins!")
elif user_choice == 'paper' and computer_choice == 'rock':
    print("User wins!")
elif user_choice == 'scissors' and computer_choice == 'paper':
    print("User wins!")
else:
    print("Computer wins!")