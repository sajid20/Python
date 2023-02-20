import random

user_wins = 0
computer_wins = 0
user_name = input("What's your Name? ")

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissor or Q to quit: ").lower()
    if user_input == "q":
        break
    
    if user_input not in options:
        continue

    random_number = random.randint (0, 2)
    computer_pick = options[random_number]
    print ("computer picked " + computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print(user_name +" won")
        user_wins += 1
      
    elif user_input == "paper" and computer_pick == "rock":
        print(user_name +" won")
        user_wins += 1
      
    elif user_input == "scissors" and computer_pick == "paper":
        print(user_name +" won")
        user_wins += 1

    else:
        print (user_name +" lost")
        computer_wins += 1
print(user_name + "won" + str(user_wins) + " times.")
print("Computer won " + str(computer_wins) +" times.")
print("GoodBye! " + user_name) 