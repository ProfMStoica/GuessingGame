"""Represents a player who participates in the game by guessing numbers"""

import random

import guessinggame as game #NOTE: This import syntax is required to avoid cirular import reference errors

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
        #generate a random number between in the game's range and remember it
        self._guess = random.randint(game.GuessingGame.s_minGuess, game.GuessingGame.s_maxGuess)

        