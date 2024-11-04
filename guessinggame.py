"""Defines the game logic for the guessing game"""

from player import Player

class GuessingGame:
    def __init__(self):
        self._answer = -1
        self._roundCount = 0

        #create the three player objects
        self._larry = Player("Larry")
        self._curly = Player("Curly")
        self.moe = Player("Moe")

    def start(self):
        pass

    def determineWinner(self):
        return "TBD"