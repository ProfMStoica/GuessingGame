"""Represents a player who participates in the game by guessing numbers"""

import random
class Player:
    def __init__(self, name):
        self._name = name
        self._guess = -1

    def getName(self):
        return self._name
    
    def setName(self, newName):
        self._name = newName

    def getGuess(self):
        return self._guess
    
    def play(self):
        #generate a random number between 0 and 9 and remember it
        self._guess = random.randint(0, 9)

        