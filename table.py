class Table:
    def __init__(self):
        self.cards = []

    def clear(self):
        for card in self.cards:
            self.cards.remove(card)

    def clear_all(self):
        for i in range(len(self.cards)):
            self.clear()
