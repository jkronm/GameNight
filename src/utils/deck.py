import random
from utils.card import Card, card_suit, card_value

class Deck:
    def __init__(self):
        self.deck = []
        for num, name in card_value.items():
            for suit in card_suit:
                card = Card(num=num, suit=suit)
                self.deck.append(card)

    def shuffle_deck(self) -> None:
        random.shuffle(self.deck)

    def get_top(self) -> Card:
        return self.deck.pop(0)

    def get_size(self) -> int:
        return len(self.deck)