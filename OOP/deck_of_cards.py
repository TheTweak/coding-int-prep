'''
Design data structures for a generic deck of cards. Describe how would you subclass these data structures
to implement a blackjack.
'''

from enum import Enum, auto
from random import shuffle


class Suit(Enum):
    HEARTS = auto(),
    DIAMONDS = auto(),
    SPADES = auto(),
    CLUBS = auto()


class Value(Enum):
    TWO = 2,
    THREE = 3,
    FOUR = 4,
    FIVE = 5,
    SIX = 6,
    SEVEN = 7,
    EIGHT = 8,
    NINE = 9,
    TEN = 10,
    JACK = auto(),
    QUEEN = auto(),
    KING = auto(),
    ACE = auto()


class Card:
    def __init__(self, suit: Suit, value: Value):
        self.suit = suit
        self.value = value
        self.is_face_card = value in set([Value.JACK, Value.QUEEN, Value.KING])

    def __str__(self) -> str:
        return f'{self.value.name}_{self.suit.name}'


class Deck:
    def __init__(self):
        self.__cards = []
        for suit in Suit:
            for value in Value:
                self.__cards.append(Card(suit, value))
        shuffle(self.__cards)

    def fetch_card(self) -> Card:
        return self.__cards.pop()


class BlackJack:
    def __init__(self):
        self.deck = Deck()

    def get_card_score(self, card: Card, count_ace_as_one: bool = False) -> int:
        if not card.is_face_card:
            return card.value.value

        if card.value is Value.ACE:
            return 1 if count_ace_as_one else 11

        return 10


if __name__ == '__main__':
    blackjack = BlackJack()
    print(blackjack.deck.fetch_card())
