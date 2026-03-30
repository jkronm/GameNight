import sys

from utils.player import Player
from utils.games_handler import Games_Handler

def main():

    # Player build
    print(type(Player))
    print("Thank you for playing Game Night!")
    print("What is your player name?")
    player_name = input(">>")
    print(f"Hello {player_name}, how much money would you like to play with?")
    money_seed = int(input(">>"))
    player = Player(player_name=player_name, money=money_seed)

    # Select Game:
    print(f"Welcome {player}!  Which game would you like to play")
    print("Available Games:")
    game = Games_Handler(player)
    game_selected = game.select_game() #could probably refactor to handle all game stuff internally to Games class
    print(f"Okay, let us play{game_selected}!")
    game.play_selected_game(game_selected)

    # use game_selected to start game

if __name__ == "__main__":
    main()