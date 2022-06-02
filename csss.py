import random
import deck_and_cheez
import bot

colors = ['○', '●']

deck = deck_and_cheez.Deck(random.choice(colors))
checker_pos = deck_and_cheez.CurrentChecker()

ALLIES = None
ENEMY = None

while True:

    print(f'Your color is: {deck.color}')
    deck.print_current_deck()

    if ALLIES is None:

        ALLIES = deck.color

    elif ENEMY is None:

        ENEMY = deck.color

        bott = bot.Bot(deck.deck, ENEMY)

    if deck.color == ALLIES:

        while True:

            checker = input('Choose you checker').upper()

            if deck.check_position(checker):

                if deck.check_checker_pos(checker):

                    current_checker = checker_pos.coord(checker)

                    move_coordinates = input('Enter coordinates').upper()

                    if deck.move(move_coordinates, current_checker):

                        deck.change_color()

                        break

                    elif not deck.move(move_coordinates, current_checker):

                        continue

    elif deck.color == ENEMY:

        bott.move_bot()

        deck.deck = bott.deck
        deck.change_color()
        continue