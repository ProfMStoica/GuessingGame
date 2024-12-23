"""Defines the game logic for the guessing game"""

import random
from player import Player
from interactiveplayer import InteractivePlayer

class GuessingGame:
    #define static/shared field variables
    s_minGuess = 0
    s_maxGuess = 9

    def __init__(self):
        self._answer = -1
        self._roundCount = 0

        #create the three player objects
        self._larry = Player("Larry")
        self._curly = Player("Curly")
        self._moe = InteractivePlayer("Moe", self)

        #make the game remember the winner
        self._winner = None

    @staticmethod
    def getMinGuess():
        return GuessingGame.s_minGuess

    @staticmethod    
    def getMaxGuess():
        return GuessingGame.s_maxGuess
    
    @staticmethod
    def setGuessRange(minGuess, maxGuess):
        GuessingGame.s_minGuess = minGuess
        GuessingGame.s_maxGuess = maxGuess

    def getWinner(self):
        return self._winner  

    def getRoundCount(self):
        return self._roundCount
    
    def getAnswer(self):
        return self._answer

    def start(self):
        #pick a number to be guessed in the game's guess range
        self._answer = random.randint(GuessingGame.getMinGuess(), GuessingGame.getMaxGuess())

        #repeat asking the user to play for each round of the game until someone wins
        while self._winner == None:
            #increment the round
            self._roundCount += 1

            #ask each player to play and show their guess
            self._larry.play()
            print(f"{self._larry.getName()} guessed {self._larry.getGuess()}")

            self._curly.play()
            print(f"{self._curly.getName()} guessed {self._curly.getGuess()}")

            self._moe.play()
            print(f"{self._moe.getName()} guessed {self._moe.getGuess()}")

            #determine if anybody won
            self._winner = self.determineWinner()

    def determineWinner(self):
        #check each player to see if their guess matched the answer
        if self._larry.getGuess() == self._answer:
            #Larry guessed correctly
            return self._larry        
        elif self._curly.getGuess() == self._answer:
            #Curly guessed correctly
            return self._curly
        elif self._moe.getGuess() == self._answer:
            #Moe guessed correctly
            return self._moe
        else:
            return None