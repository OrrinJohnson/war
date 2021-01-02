import random
from card import Card


class Deck:
    """
        The Deck class is a representation of a single deck of playing cards.
        The deck consists of 52 cards of the 4 suits: Spades, Diamonds, Clubs
        and Hearts. The values of the cards range from 2 - 14 and cards with
        values in the range 2 - 10 also have a title that is the same as their
        value. For cards with values greater than 10 (11 - 14), these are
        assigned a different title. The "Jack" card has a value of 11. The
        "Queen" card, a value of 12. The "King" card has a value of 13 and the
        "Ace" card (which in some games could also be the lowest rank) has the
        value of 14.
    """
    def __init__(self):
        self.cards = []
        self.create()

    def create(self):
        for s in ["♠", "♣", "♥", "♦"]:
            for v in range(2, 15):
                card = Card(s, v)
                card.set_face_cards()
                self.cards.append(card)

    def show(self):
        for card in self.cards:
            card.show()

    def shuffle(self):
        """
            Using the random.shuffle method, this function should a deck of
            52 Cards that have been randomly assorted.
        """
        return random.shuffle(self.cards)

    def draw_card(self):
        """
            In order to simulate drawing a card from a deck of cards, which
            is almost always done by selecting the next card on the top of the
            deck, the method should employ "pop" to remove the card from the
            beginning of the cards list.
        """
        return self.cards.pop(0)
