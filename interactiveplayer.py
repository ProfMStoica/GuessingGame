"""Defines the InteractivePlayer class"""

from player import Player

import guessinggame as gm #NOTE: This import syntax is required to avoid cirular import reference errors

class InteractivePlayer(Player): #InteractivePlayer IS-A Player
    def __init__(self, name, game):
        Player.__init__(self, name)

        self._game = game

    def play(self):
        try:
            #repeat asking the user for a guess for as long as their guess is out of range
            isGuessValid = False
            while not isGuessValid:
                #ask the user for a guess within the established range
                userGuess = int(input(f"Please enter a number between {gm.GuessingGame.getMinGuess()} and {gm.GuessingGame.getMaxGuess()}: "))
                            
                #verify that the user guess is within the established range
                if (userGuess >= gm.GuessingGame.getMinGuess() and 
                    userGuess <= gm.GuessingGame.getMaxGuess()):
                    #the user has entered a valid guess
                    self._guess = userGuess
                    isGuessValid = True
                    
            #guess is valid, check if it is too high or too low
            #give the user a hint whether it is too low or too high
            #To complete the code here, it requires access to the game object the player is participating in
            if userGuess < self._game.getAnswer():
                print("Your guess is too low.")
            else:
                print("Your guess is too high.") 

        except ValueError as ex:
            print(f"The user input is invalid. {self._name}'s turn will be skipped.\nError Message: {ex}") 

                

        