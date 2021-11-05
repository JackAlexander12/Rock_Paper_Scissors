import random
# disclosure - I watched a youtube video on how to do this ,however, I did expand and make variations from the
# original code.
user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

win_data = []

user_wins_array = []
computer_wins_array = []
tie = []


def streaks():
    wins = 0
    if len(user_wins_array) == 0 or len(user_wins_array) == 1:
        pass
    elif len(computer_wins_array) == 0 or len(computer_wins_array) == 1:
        pass
    elif len(tie) == 0 or len(tie) == 1:
        pass
    else:
        if user_wins_array[-1] != user_wins_array[-2]:
            wins = 0
        if computer_wins_array[-1] != computer_wins_array[-2]:
            wins = 0
        if tie[-1] != tie[-2]:
            wins = 0
        if user_wins_array[-1] == user_wins_array[-2] and user_wins_array[-1] == "w":
            if wins == 0:
                wins += 2
            else:
                wins += 1
            if wins > 3:
                print("You are on an outstanding and  tremendous ", wins, " round win streak!")
            else:
                print("You are on a", wins, " round win streak! Keep it going!")
        if computer_wins_array[-1] == computer_wins_array[-2] and computer_wins_array[-1] == "w":
            if wins == 0:
                wins += 2
            else:
                wins += 1
            if wins > 3:
                print("Holy cow! The computer is on a ", wins, " round win streak! You got this!")
            else:
                print("The computer is on a", wins, " round win streak! No worries!")
        if tie[-1] == tie[-2] and tie[-1] == "w":
            if wins == 0:
                wins += 2
            else:
                wins += 1
            if wins > 3:
                print("You have tied with the computer for ", wins, " rounds in a row! What are the chances?!?")
            else:
                print("You and the computer have tied for ", wins, " wins!")


while True:
    streaks()
    user_input = input("Type Rock/Paper/Scissors or \"q\"  to quit ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        continue
    random_number = random.randint(0, 2)

    # w - win, l = loss
    computer_pick = options[random_number]
    print("Computer picked: ", computer_pick + ".")
    if user_input == "rock" and computer_pick == "scissors":
        print("Congrats! You won this round")
        user_wins_array.append("w")
        computer_wins_array.append("l")
        tie.append("l")
        user_wins += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("User wins this round")
        user_wins_array.append("w")
        computer_wins_array.append("l")
        tie.append("l")
        user_wins += 1
    elif user_input == "scissors" and computer_pick == "paper":
        print("User wins this round")
        user_wins_array.append("w")
        computer_wins_array.append("l")
        tie.append("l")
        user_wins += 1
    elif user_input == computer_pick:
        print("No one won!")
        user_wins_array.append("l")
        computer_wins_array.append("l")
        tie.append("w")
    else:
        print("You lost :(")
        computer_wins_array.append("w")
        user_wins_array.append("l")
        tie.append("l")
        computer_wins += 1

print("You won", user_wins, "times")
print("Computer won", computer_wins, "times")
if computer_wins > user_wins:
    print("Better luck next time!")
elif computer_wins < user_wins:
    print("Good stuff!")
else:
    print("You tied!")