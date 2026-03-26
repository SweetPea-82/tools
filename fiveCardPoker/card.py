# For the card class (def class in python):
    # a. The list of available cards should be in a list at the top of card.py. This list should be a generated set based on two enums. 
    #   the two enums should be one enum for suits and the other enum for card (it should have 2, 3, 4, 5….J, Q, K…)
    # b. A card should compare itself to another card through an __eq__ method to know which one is higher (also __gt__ and __lt__) 
    #   must be defined.
    # c. An “instance” of each constructed class should have a suit and a number property.
    # d. Should have a __str__ method which allows the class to be printed.
    # e. Your tests for this one can be simple: can do things like construct and compare two cards and ensure the result for 
    #   the larger card is asserted.
from enum import Enum

class Suit(Enum):
    SPADE = 1
    HEART = 2
    DIAMOND = 3
    CLUB = 4

class Number(Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
class card:
    def __init__(self):
        