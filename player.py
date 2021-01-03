from deck import Deck


deck = Deck()


class Player:
    """
        The Player class is a representation of someone playing the game. In
        the game "War", there are two players only. For this game, one of the
        "player" will be the computer and the other will be someone playing
        against the computer. Each player will start with an even amount of
        cards from the deck (26).
    """
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.cards_played = []
        self.cards_won = []
        self.war_cards = []

    def draw_card(self, deck):
        self.hand.append(deck.draw_card())

    def show_hand(self):
        for card in self.hand:
            card.show()

    def play_card(self):
        """
            This method should simulate a player in the game playing a card
            from their hand against their opponent's card. This card should be
            taken from the top of the player's card stack (beginning of list).
        """
        played_card = self.hand.pop(0)
        print(f"{self.name} played the "), played_card.show()
        self.cards_played.append(played_card)
