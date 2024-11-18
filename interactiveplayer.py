"""Defines the InteractivePlayer class"""

from player import Player

import guessinggame as game #NOTE: This import syntax is required to avoid cirular import reference errors

class InteractivePlayer(Player): #InteractivePlayer IS-A Player
    def __init__(self, name):
        Player.__init__(self, name)

    def play(self):
        #repeat asking the user for a guess for as long as their guess is out of range
        isGuessValid = False
        while not isGuessValid:
            #ask the user for a guess within the established range
            userGuess = int(input(f"Please enter a number between {game.GuessingGame.getMinGuess()} and {game.GuessingGame.getMaxGuess()}: "))

            #verify that the user guess is within the established range
            if (userGuess >= game.GuessingGame.getMinGuess() and 
                userGuess <= game.GuessingGame.getMaxGuess()):
                self._guess = userGuess
                isGuessValid = True

        