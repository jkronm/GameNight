card_value = {
    1: "ACE",
    2: "TWO",
    3: "THREE",
    4: "FOUR",
    5: "FIVE",
    6: "SIX",
    7: "SEVEN",
    8: "EIGHT",
    9: "NINE",
    10: "TEN",
    11: "JACK",
    12: "QUEEN",
    13: "KING"
}

card_suit = (
    "♣"
    "♦"
    "♥"
    "♠"
)

class Card():
    def __init__(self, num, suit):
        self.num = num
        self.suit = suit
        
    def get_card_num(self) -> int:
        return self.num
    
    def get_card_val(self) -> str:
        return card_value[self.num]
    
    def get_suit(self) -> str:
        return self.suit
    

    