from player import Player, deck, table
from helpers import clear


def start_game():
    war = False
    name = input("What is your name?  ")
    player = Player(name)
    computer = Player("Computer")
    print("Shuffling deck.....")
    for i in range(1, 5):
        deck.shuffle()
    print("players are drawing their cards.....")
    for i in range(1, 27):
        player.draw_card(deck)
        computer.draw_card(deck)

    def time_for_war():
        table.cards.append(player.hand[0])
        table.cards.append(computer.hand[0])
        player.play_card()
        computer.play_card()
        if player.played_card.value > computer.played_card.value:
            print(f"{player.name} wins the war!")
            for card in table.cards:
                player.cards_won.append(card)
            print("Player won", len(table.cards), "cards")
            table.clear_all()

        elif computer.played_card.value > player.played_card.value:
            print(f"{computer.name} wins the war!")
            for card in table.cards:
                computer.cards_won.append(card)
            print("Computer won", len(table.cards), "cards")
            table.clear_all()

        else:
            time_for_war()

    def round():
        print(f"({player.name}: {len(player.cards_won)}"
              f" {computer.name}: {len(computer.cards_won)})")
        prompt = input("Are you ready to play your card? Y/n? ")
        computer.play_card()
        if prompt != 'n':
            player.play_card()

            if player.played_card.value > computer.played_card.value:
                print(f"{player.name} wins the round!")
                for card in table.cards:
                    player.cards_won.append(card)
                table.clear_all()
                clear()

            elif computer.played_card.value > player.played_card.value:
                print(f"{computer.name} wins the round!")
                for card in table.cards:
                    computer.cards_won.append(card)
                table.clear_all()
                clear()

            else:
                print("WAR!")
                time_for_war()

    while len(player.hand) > 1 and len(computer.hand) > 1 and not war:
        round()

    if computer.hand == 0:
        print(f"{computer.name} is getting new hand...")
        computer.hand = computer.cards_won
    if player.hand == 0:
        print(f"{player.name} is getting a new hand...")
        player.hand = player.cards_won
    if computer.hand == 0 and computer.cards_won == 0:
        print(f"{player.name} wins the game!")
    if player.hand == 0 and player.cards_won == 0:
        print(f"{computer.name} wins the game!")


if __name__ == "__main__":
    start_game()
