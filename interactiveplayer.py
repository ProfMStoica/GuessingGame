"""Defines the InteractivePlayer class"""

from player import Player
from guessinggame import GuessingGame

class InteractivePlayer(Player): #InteractivePlayer IS-A Player
    def __init__(self, name):
        Player.__init__(self, name)

    def play(self):
        #ask the user for a guess between 0 and 9
        self._guess = int(input(f"Please enter a number between {GuessingGame.s_minGuess} and {GuessingGame.s_maxGuess}: "))

        