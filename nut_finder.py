#FINDS THE NUTS
from operator import attrgetter
from hand_checker import HandChecker
SPADE = u"\u2660"
CLUB = u"\u2663"
DIAMOND = u"\u2666"
HEART = u"\u2764"


class MyNuts:
    def __init__(self, board):
        self.board = board

    def find_nuts(self):
        if self.straight_flush():
            return 'Straight Flush is the nuts'
        elif self.four_of_a_kind(self.board):
            return '4 of a kind is the nuts'
        elif self.straight(self.board):
            return 'straight is the nuts'
        else:
            self.last_check(self.board)

    def check_withen_five(self, three_cards):
        three_cards = three_cards.sort(key=attrgetter('value'))
        if abs(three_cards[0] - three_cards[2]) <= 5:
            return True
        else:
            return False

    def straight_flush(self):
        spades = []
        clubs = []
        diamonds = []
        hearts = []
        suits = {SPADE: spades, CLUB: clubs, DIAMOND: diamonds, HEART: hearts}

        for card in self.board:
            if card.suit == SPADE:
                suits[SPADE].append(card)
            if card.suit == CLUB:
                suits[CLUB].append(card)
            if card.suit == DIAMOND:
                suits[DIAMOND].append(diamonds)
            if card.suit == HEART:
                suits[HEART].append(hearts)

        for suit in suits:
            if len(suit) == 3:
                if self.check_withen_five(suit):
                    return 'the nuts is a straight flush'
                else:
                    return False

    @staticmethod
    def four_of_a_kind(board):
        myhandchecker = HandChecker(board)
        if myhandchecker.is_pair():
            return '4 of a kind'

    @staticmethod
    def flush(five_cards):
        myhandchecker = HandChecker(five_cards)
        three_cards = myhandchecker.is_three_of_kind()
        if three_cards:
            if (three_cards[0].suit == three_cards[1].suit) and (three_cards[1].suit == three_cards[2].suit):
                return three_cards
            else:
                return False
        else:
            return False

    @staticmethod
    def straight(cards):
        print(str(cards.sort(key=attrgetter('value'))) + 'shit')
        if (abs(cards[0].value - cards[2].value) <= 5) or (abs(cards[2].value - cards[4].value)):
            return 'straight is the nuts'
        else:
            return False

    @staticmethod
    def last_check(cards):
        #three of a kind of the highest board card is the lowest possible nut hand.
        cards = cards.sort(key=attrgetter('value'))
        if cards[4].value <= 11:
            return 'straight is the nuts'
        else:
            return 'three of a kind' + cards[4].value + 'is the nuts'


def main():
    return 0


if __name__== '__main__':
    main()