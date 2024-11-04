"""Represents a player who participates in the game by guessing numbers"""

class Player:
    def __init__(self):
        self._name = ""
        self._guess = -1

    def getName(self):
        return self._name
    
    def setName(self, newName):
        self._name = newName

    def getGuess(self):
        return self._guess
    
    def play(self):
        pass