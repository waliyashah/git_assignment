import random

def main():
    print("Welcome to Rock, Paper, Scissors!")
    print("Rules of the game:")
    print("Rock beats Scissors, Scissors beats Paper, Paper beats Rock.")
    print("If both players select the same one, it's a tie.")

    choices = ["rock", "paper", "scissors"]

    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors): ").strip().lower()
        if user_choice not in choices:
            print("Invalid choice. Please select 'rock', 'paper', or 'scissors'.")
            continue

        computer_choice = random.choice(choices)
        print(f"\nYou selected: {user_choice}")
        print(f"Computer selected: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie! Let's play again.\n")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print("You win!")
            break
        else:
            print("Computer wins!")
            break

if __name__ == "__main__":
    main()
