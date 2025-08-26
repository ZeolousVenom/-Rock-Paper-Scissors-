import random

def play_game():
    choices = ["rock", "paper", "scissors"]
    
    while True:
        # Get user input
        user_choice = input("Choose rock, paper, or scissors (or 'quit' to exit): ").lower()
        
        if user_choice == 'quit':
            print("Thanks for playing! Goodbye!")
            break
        
        if user_choice not in choices:
            print("Invalid choice! Please try again.")
            continue
        
        # Computer makes a random choice
        computer_choice = random.choice(choices)
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        # Determine the winner
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (
            (user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "paper" and computer_choice == "rock") or
            (user_choice == "scissors" and computer_choice == "paper")
        ):
            print("You win! 🎉")
        else:
            print("Computer wins! 😢")
        
        print("\n------------------------\n")

# Start the game
print("Welcome to Rock, Paper, Scissors!")
play_game()