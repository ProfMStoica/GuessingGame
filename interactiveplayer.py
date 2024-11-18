"""Defines the InteractivePlayer class"""

from player import Player

import guessinggame as game #NOTE: This import syntax is required to avoid cirular import reference errors

class InteractivePlayer(Player): #InteractivePlayer IS-A Player
    def __init__(self, name):
        Player.__init__(self, name)

    def play(self):
        #ask the user for a guess between 0 and 9
        self._guess = int(input(f"Please enter a number between {game.GuessingGame.s_minGuess} and {game.GuessingGame.s_maxGuess}: "))

        