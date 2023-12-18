import random #Fixed code made it better

while True:
    rps = input("Please select rock, paper, or scissors: ").lower()
    if rps in ["rock", "paper", "scissors"]:
        break

print("You have chosen " + rps)

def computer_choice():
    return random.choice(["rock", "paper", "scissors"])

computer_pick = computer_choice()
print("Computer chose " + computer_pick)

if computer_pick == rps:
    print("You tied")
elif (rps == "rock" and computer_pick == "scissors") or \
        (rps == "paper" and computer_pick == "rock") or \
        (rps == "scissors" and computer_pick == "paper"):
    print("You win!")
else:
    print("You lose!")
