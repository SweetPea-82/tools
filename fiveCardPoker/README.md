Five Card Poker Hand project OOP (object oriented programming) Python Requirements:
 
You should build a five-card poker program:
 
You will need several elements. Your program should include a main function, and several classes to include test functions and “card”, “hand”, “dealer” and have a “main” function which executes one game or round of poker.

For Python (install anaconda on your machine you can find it on the network):
Note that each of these should be in a different python file.

1. Create a python unittest class to drive your program. You should write tests as you build up your program.
    a. You should have methods to test each class as you go.

2. For the card class (def class in python):
    a. The list of available cards should be in a list at the top of card.py. This list should be a generated set based on two enums. The two enums should be one enum for suits and the other enum for card (it should have 2, 3, 4, 5….J, Q, K…)
    b. A card should compare itself to another card through an __eq__ method to know which one is higher (also __gt__ and __lt__) must be defined.
    c. An “instance” of each constructed class should have a suit and a number property.
    d. Should have a __str__ method which allows the class to be printed.
    e. Your tests for this one can be simple: can do things like construct and compare two cards and ensure the result for the larger card is asserted.

3. Hand class
    a. Supports random numbers from 0:51 picks out the ordered card which the random number represents. i.e. if initialized using the number 0 you would pull the 2 of clubs.
    b. Should be given a list of up to 5 random numbers to make a hand.
    c. Has the property “cards” which has the list of cards stored.
    d. Should have __eq__ method defined etc as one hand should be able to compare itself to another hand.
    e. Should have a __str__ method which allows the class to be printed.
        i. Declares which poker hand is made when printed and also prints the sequence of cards: I.e., 3 of a kind: A, A, A, 2, 5
    f. Tests in your test class should include constructing and comparing hands to ensure the correct result.

4. Dealer/Deck Class
    a. Contains a list of random numbers representing a shuffled deck from 0:51. Also has a shuffle method which regenerates the random list of numbers
    b. Has a “dealHand” method which outputs a hand of cards of length five
                                                              i.      Ensures no card is dealt twice regardless of how many hands are dealt.
    c. Compares and orders a list of hands as given via a “compare” method.
    d. Should have a __str__ method which allows the class to be printed.
    e. Tests should include dealing up to 5 hands and comparing each of them and ranking them by winning to least hand.

5. Main or “__main__” method:
    a. Dealer class instantiated and a random number of hands is dealt (up to 5)
    b. Uses dealer to compare all hands.
    c. Prints the results of the hands in order using the dealer class