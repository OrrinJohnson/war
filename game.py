from player import Player, deck


def start_game():
    name = input("What is your name?  ")
    player = Player(name)
    computer = Player("Computer")
    print("Shuffling deck.....")
    for i in range(1, 5):
        deck.shuffle()
    print("the deck has", len(deck.cards))
    print("players are drawing their cards.....")
    for i in range(1, 27):
        player.draw_card(deck)
        computer.draw_card(deck)
    print(f"the deck now has {len(deck.cards)} cards")

    def round():
        prompt = input("Are you ready to play your card? Y/n? ")
        if prompt != 'n':
            player.play_card()
            computer.play_card()

            if player.cards_played[-1].value > computer.cards_played[-1].value:
                print(f"{player.name} wins the round!")
                player.cards_won.append(computer.cards_played[-1])
                player.cards_won.append(player.cards_played[-1])

            elif computer.cards_played[-1].value > player.cards_played[-1].value:
                print(f"{computer.name} wins the round!")
                computer.cards_won.append(player.cards_played[-1])
                computer.cards_won.append(computer.cards_played[-1])

            else:
                print("WAR!")

    round()


start_game()
