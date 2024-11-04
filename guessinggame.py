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
        #pick a number to be guessed between  0 and 9

        #repeat asking the user to play for each round of the game until someone wins
        pass

    def determineWinner(self):
        #check if larry's guess matched the answer

        #check if curly's guess matched the answer

        #checxk if moe's guess matched the answer

        #return the winning player if one guessed correctly or None
        return "TBD"