import random
# disclosure - I watched a youtube video on how to do this ,however, I did expand and make variations from the
# original code.
user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

win_data = []
user_winstf = False
computer_winstf = False

while True:
    user_input = input("Type Rock/Paper/Scissors or \"q\"  to quit ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        continue
    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("Computer picked: ", computer_pick + ".")
    if user_input == "rock" and computer_pick == "scissors":
        print("Congrats! You won this round")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("User wins this round")
        user_wins += 1
    elif user_input == "scissors" and computer_pick == "paper":
        print("User wins this round")
        user_wins += 1
    elif user_input == computer_pick:
        print("No one won!")
        user_wins+= 1
        continue
    else:
        print("You lost :(")
        computer_wins +=1

print("You won", user_wins, "times")
print("Computer won", computer_wins, "times")
if computer_wins > user_wins:
    print("Better luck next time!")
elif computer_wins < user_wins:
    print("Good stuff!")
else:
    print("You tied!")