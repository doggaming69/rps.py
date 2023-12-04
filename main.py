import random #thx chatgpt for cleaning up my code

while True:
    rps = input("Enter your choice (rock/paper/scissors): ").lower()
    if rps in ["rock", "paper", "scissors"]:
        break
    else:
        print("Invalid choice. Please enter rock, paper, or scissors.")

if rps == "rock":
    print("You have chosen rock")
elif rps == "paper":
    print("You have chosen paper")
elif rps == "scissors":
    print("You have chosen scissors")

def play_computer():
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    print("Computer chose:", computer_choice)

play_computer()
