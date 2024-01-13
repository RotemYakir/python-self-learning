import random

while True:
    choices = ["Rock", "Paper", "Scissors"]
    computer = random.choice(choices)
    player = None
    while player not in choices:
        player = input("Rock / Paper / Scissors ? :").capitalize()

    if player == computer:
        print("Computer: " + computer)
        print("Player: " + player)
        print("It's a tie!!")
    elif player == "Scissors":
        if computer == "Rock":
            print("Computer: " + computer)
            print("Player: " + player)
            print("You lose!")
        else:
            print("Computer: " + computer)
            print("Player: " + player)
            print("You win!")
    elif player == "Rock":
        if computer == "Paper":
            print("Computer: " + computer)
            print("Player: " + player)
            print("You lose!")
        else:
            print("Computer: " + computer)
            print("Player: " + player)
            print("You win!")
    elif player == "Paper":
        if computer == "Scissors":
            print("Computer: " + computer)
            print("Player: " + player)
            print("You lose!")
        else:
            print("Computer: " + computer)
            print("Player: " + player)
            print("You win!")

    play_again = input("\nWould you like to play again?(yes/no)").lower()
    if play_again != "yes":
        break
print("Bye!")

