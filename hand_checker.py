from operator import attrgetter
from collections import Counter
SPADE = u"\u2660"
CLUB = u"\u2663"
DIAMOND = u"\u2666"
HEART = u"\u2764"

### DOES NOT PRINT THE WINNING HAND FOR ALL CARDS AND IS NOT TESTED ON RANDOMLY GENERATED HANDS ###

def print_cards(all_7):
    print(str(all_7[0].value) + ',' + str(all_7[1].value))


def hand_printer(winning_hand):
    for card in winning_hand:
        print(str(card.value) + card.suit, end='')


class HandChecker:
    def __init__(self, all_7):
        self.all_7 = all_7
        self.all_7.sort(key=attrgetter('value'))# sort cards by value
        self.spades = 0
        self.clubs = 0
        self.diamonds = 0
        self.hearts = 0

    def print_board(self):
        hand = self.all_7[0].name + \
               self.all_7[0].suit + \
               self.all_7[1].name + \
               self.all_7[1].suit

        board = self.all_7[2].name + \
                self.all_7[2].suit + \
                self.all_7[3].name + \
                self.all_7[3].suit + \
                self.all_7[4].name + \
                self.all_7[4].suit + \
                self.all_7[5].name + \
                self.all_7[5].suit + \
                self.all_7[6].name + \
                self.all_7[6].suit

        print('You have ' + hand + ', and the board is ' + board)

    def is_straight(self):
        straight_list = [] # straight counter
        for i in range(6): # check the first 6 cards
            if self.all_7[i].value == self.all_7[i+1].value - 1:
                straight_list.append(self.all_7[i])
                if len(straight_list) == 5:
                    return straight_list
                else:
                    continue
        return False

    def best_hand(self):
        straight = False
        flush = False
        fullhouse = False
        three_of_kind = False
        pair = False
        four_of_kind = False
        two_pair = False
        high_card = False

        if self.is_flush():
            flush = True
            winning_hand = self.is_flush()
            hand_printer(winning_hand)
            winning_hand = []

        if self.is_4_of_kind():
            winning_hand = self.is_4_of_kind()
            hand_printer(winning_hand)
            four_of_kind = True

        cards = self.is_straight()
        if cards:
            print('straight')
            straight = True
        if self.is_fullhouse():
            fullhouse = True
            hand_printer(self.is_fullhouse())

        elif self.is_three_of_kind():
            winning_hand = self.is_three_of_kind()
            hand_printer(winning_hand)
            three_of_kind = True

        if self.is_2_pair():
            two_pair = True
        if self.is_pair():
             pair = True
        else:
            high_card = True

        if flush and straight:
            return 'straight flush'
        if flush:
            return 'flush'
        if four_of_kind:
            return 'four of a kind '
        if fullhouse:
            return 'full house'
        if straight:
            return 'straight'
        if three_of_kind:
            return 'three of a kind'
        if two_pair:
            return '2 pair'
        if pair:
            return 'pair'
        if high_card:
            return 'high_card'

    def is_flush(self):
        winning_hand = []
        for card in self.all_7:

            if card.suit == SPADE:
                self.spades += 1
            elif card.suit == CLUB:
                self.clubs += 1
            elif card.suit == DIAMOND:
                self.diamonds += 1
            elif card.suit == HEART:
                self.hearts += 1

        if self.spades >= 5:
            for card in self.all_7:
                if card.suit == SPADE:
                    winning_hand.append(card)
            return winning_hand

        if self.clubs >= 5:
            for card in self.all_7:
                if card.suit == CLUB:
                    winning_hand.append(card)
            return winning_hand

        if self.diamonds >= 5:
            for card in self.all_7:
                if card.suit == DIAMOND:
                    winning_hand.append(card)
            return winning_hand

        if self.hearts >= 5:
            for card in self.all_7:
                if card.suit == HEART:
                    winning_hand.append(card)
            return winning_hand

        else:
            return False

    def is_ace_straight(self, ace_index):
        # if we see an ace we need to change the value of ace to 1 resort the list and look for a straight
        ace_list = self.all_7
        ace_list[ace_index].value = 0
        ace_list.sort(key=attrgetter('value'))
        # check for straight in ace_list
        for i in range(6):
            if ace_list[i].value != ace_list[i + 1].value:
                return False
            else:
                continue
        return True

    def count_card_suits(self):
        counts = [0] * 4
        for card in self.all_7:
            counts[card.suit] = counts[card.suit] + 1
        return counts

    def count_card_values(self):
        counts = [0] * 14
        for card in self.all_7:
            counts[card.value] = counts[card.value] + 1
        return counts

    def is_fullhouse(self):
        winning_hand = []
        three = 0
        counts = self.count_card_values()
        if 3 in counts:
            for count in counts:
                if count == 3:
                    three += 1
            if (three > 1) or ((2 in counts) and (3 in counts)):
                if ((2 in counts) and (3 in counts)) and (three < 2):# 1 type of full house need indexes
                    for card in self.all_7:
                        if card.value == counts.index(2) or card.value == counts.index(3):
                            winning_hand.append(card)
                return winning_hand
            else:
                return False

    def is_three_of_kind(self):
        winning_hand = []
        counts = self.count_card_values()
        if 3 in counts:
            for card in self.all_7:
                if card.value == counts.index(3):
                    winning_hand.append(card)
            return winning_hand

    def is_4_of_kind(self):
        winning_hand = []
        counts = self.count_card_values()
        if 4 in counts:
            for card in self.all_7:
                if card.value == counts.index(4):
                    winning_hand.append(card)
            return winning_hand

    def is_2_pair(self):
        pair = 0
        counts = self.count_card_values()
        for number in counts:
            if number == 2:
                pair += 1
            if pair == 2:
                return True
            else:
                continue

    def is_pair(self):
        counts = self.count_card_values()
        if 2 in counts:

            return True

    def high_card(self):
        return self.all_7[6]


