import random
import sys

# Define player choices
valid_outcome = ["spock", "scissor", "rock", "lizard", "paper"]

# Get player outcome
player1 = random.choice(valid_outcome)
player2 = random.choice(valid_outcome)
print("Player 1 is ", player1)
print("Player 2 is ", player2)

# Valid player outcome
if player1 == player2:
    sys.exit("Same player choice, play again")

# Set rule for winning and provide result
if player1 == "spock" and player2 in ["scissor", "rock"]:
    print("Player 1 win")
elif player1 == "lizard" and player2 in ["spock", "paper"]:
    print("Player 1 win")
elif player1 == "rock" and player2 in ["scissor", "lizard"]:
    print("Player 1 win")
elif player1 == "paper" and player2 in ["spock", "rock"]:
    print("Player 1 win")
elif player1 == "scissor" and player2 in ["lizard", "paper"]:
    print("Player 1 win")
else:
    print("Player 2 win")


