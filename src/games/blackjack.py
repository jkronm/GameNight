from utils.deck import Deck

class Blackjack:
    def __init__(self, player):
        self.player = player
        self.deck = []
        self.player_hand = []

        deck = Deck()
        #todo - stopped here below is for debug
        print(deck.get_size())
        card = deck.get_top()
        print(f"{card.get_card_val()} | {card.get_suit()}")
        deck.shuffle_deck()
        card = deck.get_top()
        print(f"{card.get_card_val()} | {card.get_suit()}")


