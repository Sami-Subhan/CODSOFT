import random

def play_round():
    # Initialize scores
    user_score = 0
    computer_score = 0

    # Define choices
    choices = ["rock", "paper", "scissors"]

    while True:
        # User input
        user_choice = input("\nChoose rock, paper, or scissors (or 'q' to quit): ").lower()

        # Check if the user wants to quit
        if user_choice == 'q':
            break

        # Validate user input
        if user_choice not in choices:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        # Computer selection
        computer_choice = random.choice(choices)

        # Display choices
        print(f"\nUser chooses: {user_choice}")
        print(f"Computer chooses: {computer_choice}")

        # Determine the winner
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (
            (user_choice == "rock" and computer_choice == "scissors")
            or (user_choice == "scissors" and computer_choice == "paper")
            or (user_choice == "paper" and computer_choice == "rock")
        ):
            print("User wins!")
            user_score += 1
        else:
            print("Computer wins!")
            computer_score += 1

        # Display scores
        print(f"\nUser Score: {user_score}")
        print(f"Computer Score: {computer_score}")

    return user_score, computer_score
while True:
    user_score, computer_score = play_round()

    # Ask the user if they want to play again
    play_again = input("\nDo you want to play another round? (yes/no): ").lower()
    if play_again != 'yes':
        break

# Final scores
print("\nFinal Scores:")
print(f"User Score: {user_score}")
print(f"Computer Score: {computer_score}")
