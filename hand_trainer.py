#!/usr/bin/python
"""
Usage:
    hand_trainer [options]
    hand_trainer --debug
    hand_trainer --besthand <numhands>

Options:
    --debug     runs through test hands
    --besthand  prints quiz hands
    --thenuts   returns the nuts from a hand
"""

from docopt import docopt
import random
from hand_checker import HandChecker
from nut_finder import MyNuts
SPADE = u"\u2660"
CLUB = u"\u2663"
DIAMOND = u"\u2666"
HEART = u"\u2764"

suits = [SPADE, CLUB, DIAMOND, HEART]
high_cards = {14: 'A', 11: 'J', 12: 'Q', 13: 'K'}


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        if value > 10:
            self.name = high_cards[value]
        else:
            self.name = str(value)

    def card_printer(self):
            print("|-------|")
            print("| %s     |" % self.name)
            print("|       |")
            print("|   %s   |" % self.suit)
            print("|       |")
            print("|    %s  |" % self.name)
            print("|-------|")


class TestHand:

    def straight_flush(self):
        self.card1 = Card(4, SPADE)
        self.card2 = Card(2, SPADE)
        self.card3 = Card(3, SPADE)
        self.card4 = Card(5, DIAMOND)
        self.card5 = Card(6, SPADE)
        self.card6 = Card(7, CLUB)
        self.card7 = Card(8, SPADE)
        return ([self.card1, self.card2, self.card3, self.card4, self.card5, self.card6, self.card7])

    def flush(self):
        self.card1 = Card(4, SPADE)
        self.card2 = Card(2, SPADE)
        self.card3 = Card(3, SPADE)
        self.card4 = Card(5, DIAMOND)
        self.card5 = Card(10, SPADE)
        self.card6 = Card(7, CLUB)
        self.card7 = Card(8, SPADE)
        return ([self.card1, self.card2, self.card3, self.card4, self.card5, self.card6, self.card7])

    def full_house(self):
        self.card1 = Card(5, SPADE)
        self.card2 = Card(5, CLUB)
        self.card3 = Card(5, SPADE)
        self.card4 = Card(10, DIAMOND)
        self.card5 = Card(6, HEART)
        self.card6 = Card(10, CLUB)
        self.card7 = Card(8, SPADE)
        return ([self.card1, self.card2, self.card3, self.card4, self.card5, self.card6, self.card7])

    def straight(self):
        self.card1 = Card(7, SPADE)
        self.card2 = Card(8, CLUB)
        self.card3 = Card(9, SPADE)
        self.card4 = Card(10, DIAMOND)
        self.card5 = Card(11, HEART)
        self.card6 = Card(12, CLUB)
        self.card7 = Card(8, SPADE)
        return ([self.card1, self.card2, self.card3, self.card4, self.card5, self.card6, self.card7])

    def three_of_a_kind(self):
        self.card1 = Card(8, SPADE)
        self.card2 = Card(8, CLUB)
        self.card3 = Card(8, HEART)
        self.card4 = Card(7, DIAMOND)
        self.card5 = Card(11, HEART)
        self.card6 = Card(2, CLUB)
        self.card7 = Card(5, SPADE)
        return ([self.card1, self.card2, self.card3, self.card4, self.card5, self.card6, self.card7])

    def four_of_a_kind(self):
        self.card1 = Card(8, SPADE)
        self.card2 = Card(8, CLUB)
        self.card3 = Card(8, HEART)
        self.card4 = Card(8, DIAMOND)
        self.card5 = Card(11, HEART)
        self.card6 = Card(12, CLUB)
        self.card7 = Card(5, SPADE)
        return ([self.card1, self.card2, self.card3, self.card4, self.card5, self.card6, self.card7])

    def pair(self):
        self.card1 = Card(8, SPADE)
        self.card2 = Card(8, CLUB)
        self.card3 = Card(6, HEART)
        self.card4 = Card(2, DIAMOND)
        self.card5 = Card(11, HEART)
        self.card6 = Card(12, CLUB)
        self.card7 = Card(5, SPADE)
        return ([self.card1, self.card2, self.card3, self.card4, self.card5, self.card6, self.card7])

    def two_pair(self):
        self.card1 = Card(8, SPADE)
        self.card2 = Card(8, CLUB)
        self.card3 = Card(10, HEART)
        self.card4 = Card(2, DIAMOND)
        self.card5 = Card(6, HEART)
        self.card6 = Card(6, CLUB)
        self.card7 = Card(5, SPADE)
        return ([self.card1, self.card2, self.card3, self.card4, self.card5, self.card6, self.card7])

    def high_card(self):
        self.card1 = Card(10, SPADE)
        self.card2 = Card(11, CLUB)
        self.card3 = Card(4, HEART)
        self.card4 = Card(5, DIAMOND)
        self.card5 = Card(7, HEART)
        self.card6 = Card(13, CLUB)
        self.card7 = Card(9, SPADE)
        return ([self.card1, self.card2, self.card3, self.card4, self.card5, self.card6, self.card7])


class Deck:
    def __init__(self):
        self.cards = []

    def print_deck(self):
        for playing_card in self.cards:
            print(playing_card.name + ':' + playing_card.suit)

    def shuffle(self):
        random.shuffle(self.cards)

    def is_valid(self):
        if len(self.cards) == 52:
            return True
        else:
            return False

class Dealer:
    def __init__(self, players):
        self.players = players
        self.deck = build_deck()
        #shuffle the deck 7 times
        for i in range(7):
            self.deck.shuffle()

# rember this function is for testing and is bad
    def test_hand(self):
        hand = self.deck.cards[0].name + \
               self.deck.cards[0].suit + \
               self.deck.cards[1].name + \
               self.deck.cards[1].suit

        board = self.deck.cards[2].name + \
            self.deck.cards[2].suit + \
            self.deck.cards[3].name + \
            self.deck.cards[3].suit + \
            self.deck.cards[4].name + \
            self.deck.cards[4].suit + \
            self.deck.cards[5].name + \
            self.deck.cards[5].suit + \
            self.deck.cards[6].name + \
            self.deck.cards[6].suit

        print('You have ' + hand + ', and the board is ' + board)

        all_7 = []
        for i in range(7):
            all_7.append(self.deck.cards[i])

        return all_7


def build_deck():
    my_deck = Deck()
    num_cards = 0
    for suit in suits:
        for value in range(1, 14):
            my_card = Card(value, suit)
            my_deck.cards.append(my_card)
            num_cards += 1

    return my_deck


def get_5(all_7):
    return all_7[2:6]

def print_7cards(all_7):
    print(str(all_7[0].value) + ',' + str(all_7[1].value))


def hand_debuger(test_hand):
    my_handchecker = HandChecker(test_hand)
    #my_handchecker.print_board()
    print('The best hand is:' + my_handchecker.best_hand() + '\n')


def debug_hands():
    testhand = TestHand()
    print('This should be a straight flush \n\n')
    hand_debuger(testhand.straight_flush())
    print('this should be 4 of a kind')
    hand_debuger(testhand.four_of_a_kind())
    print('This should be a flush')
    hand_debuger(testhand.flush())
    print('this should be a full house')
    hand_debuger(testhand.full_house())
    print('this should be a straight')
    hand_debuger(testhand.straight())
    print ('this should be a pair')
    hand_debuger(testhand.pair())
    print('this should be 2 pair')
    hand_debuger(testhand.two_pair())
    print('this should be high card')
    hand_debuger(testhand.high_card())
    print('this should be three of a kind')
    hand_debuger(testhand.three_of_a_kind())


def main():
    args = docopt(__doc__, version='hand_trainer 1.0')
    players = ['player1']
    if args['--debug']:
        debug_hands()

    if args['--besthand']:
        for i in range(int(args['<numhands>'])):
            mydealer = Dealer(players)
            hand_debuger(mydealer.test_hand())

    if args['--thenuts']:
        mydealer = Dealer(players)
        test_hand = mydealer.test_hand()
        board = test_hand[2:6]
        nuts = MyNuts(board)
        print(nuts.find_nuts())





if __name__ == '__main__':

    main()