class Player:
    def __init__(self, player_name: str, money: int):
        self.player_name = player_name
        self.money = money
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def remove_card(self, card):
        if card in self.hand:
            self.hand.remove(card)

    def get_hand_value(self):
        # TO DO: implement logic to calculate hand value
        pass

    def __str__(self):
        return f"Player '{self.player_name}' has ${self.money} and a hand of {len(self.hand)} cards"