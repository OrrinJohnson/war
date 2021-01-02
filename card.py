class Card:
    """
        The Card class is a representation of a playing card.
        Each card has a suit and a numerical value as well as a title.
        The title of the card is strictly based on the integer value of the
        card. The lowest "number" card has an numerical value of 2 and
        therefore, the title of the card is also "2". The highest "number"
        card has a numerical value of 10 with a corresponding title. Any
        cards with a value higher than 10 will be "face cards" or an "Ace"
        respecitvely. In certain circumstances, the Ace card will have a value
        lower than the "2" card, but in this case, the Ace is the highest
        ranking card.
    """
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.title = self.value

    def show(self):
        print(f"{self.title} of {self.suit}")

    def set_face_cards(self):
        """
            Set up the title for the cards. The values of the cards need
            to remain numerical values but, as with most analog card games,
            cards with values higher than 10 are not referred to as 11, 12 etc,
            rather, Jack, Queen, King and Ace, if the Ace card is determined to
            be not the lowest ranking card.
        """
        if self.value <= 10:
            self.title = self.value
        if self.value == 11:
            self.title = "Jack"
        if self.value == 12:
            self.title = "Queen"
        if self.value == 13:
            self.title = "King"
        if self.value == 14:
            self.title = "Ace"
