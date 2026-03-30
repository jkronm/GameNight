from games.blackjack import Blackjack
from utils.player import Player

class Games_Handler:
    def __init__(self, player: Player):
        self.player = player
        self.games = {
            "1": "blackjack",
            "2": "poker",
            "3": "solitaire"
        }

    # Get user input for game selection
    def select_game(self) -> str:
        #initial display of options
        print("Please select a game.  Here are your options:")
        for k, v in self.games.items():
            print(f"{k}. {v}")
        choice = input(">>")
        #check choice and redisplay if not valid response.
        while choice not in ["1", "2", "3"]:
            print("That is not a valid response.")
            print("please slect then number of the game you would like to play.")
            for k, v in self.games.items():
                print(f"{k}. {v}")
            choice = input(">>")
        return self.games.get(choice)
    
    def play_selected_game(self, selected_game: str):
        print(f"selecting game: {selected_game}") #debug
        match selected_game:
            case "blackjack":
                print("Playing blackjack") #debug
                return Blackjack(self.player)
            case "_":
                return "not ready"
            case "__":
                return "not ready"
        