import random

def get_user_choice():
    while True:
        user_choice = input("Enter Rock, Paper, or Scissors: ").lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice. Please enter Rock, Paper, or Scissors.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!", 0
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'scissors' and computer_choice == 'paper')
    ):
        return "You win!", 1
    else:
        return "Computer wins!", -1

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        print("\nLet's play Rock, Paper, Scissors!")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose {user_choice}. Computer chose {computer_choice}.")
        
        result, score_change = determine_winner(user_choice, computer_choice)
        print(result)

        user_score += score_change
        computer_score -= score_change

        print(f"Score - You: {user_score}, Computer: {computer_score}")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

# Run the game
play_game()