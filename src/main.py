# Import required modules
import sys

def main():
    # Display welcome message and available games
    print("Welcome to Card Game App!")
    print("Available Games:")
    print("1. Blackjack")
    print("2. Poker")
    print("3. Solitaire")

    # Get user input for game selection
    while True:
        choice = input("Enter the number of your chosen game: ")
        if choice in ["1", "2", "3"]:
            break
        else:
            print("Invalid choice. Please try again.")

    # Call corresponding game function based on user's choice
    games = {
        "1": blackjack,
        "2": poker,
        "3": solitaire
    }

    chosen_game = games[choice]
    chosen_game()

def blackjack():
    pass  # TO DO: implement Blackjack game logic

def poker():
    pass  # TO DO: implement Poker game logic

def solitaire():
    pass  # TO DO: implement Solitaire game logic

if __name__ == "__main__":
    main()