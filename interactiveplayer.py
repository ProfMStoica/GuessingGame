"""Defines the InteractivePlayer class"""

from player import Player

import guessinggame as game #NOTE: This import syntax is required to avoid cirular import reference errors

class InteractivePlayer(Player): #InteractivePlayer IS-A Player
    def __init__(self, name):
        Player.__init__(self, name)

    def play(self):
        #TODO: add error handling to ensure the user types a number in the required range by repeat ask

        #TODO: provide game hints to tell the user if their guess is too low or too high.

        #ask the user for a guess between 0 and 9
        self._guess = int(input(f"Please enter a number between {game.GuessingGame.getMinGuess()} and {game.GuessingGame.getMaxGuess()}: "))

        