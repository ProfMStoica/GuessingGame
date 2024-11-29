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
        self._playerList = []
        self._playerList.append(Player("Larry"))
        self._playerList.append(Player("Curly"))
        self._playerList.append(InteractivePlayer("Moe", self))

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
            for iPlayer in range(len(self._playerList)):
                #access the current element in the list
                crtPlayer = self._playerList[iPlayer]
                
                #ask the current player to play in the round
                crtPlayer.play()
                print(f"{crtPlayer.getName()} guessed {crtPlayer.getGuess()}")

            #determine if anybody won
            self._winner = self.determineWinner()

    def determineWinner(self):
        for iPlayer in range(len(self._playerList)):
            #check the current player to see if their guess matched the answer
            crtPlayer = self._playerList[iPlayer]
            if crtPlayer.getGuess() == self._answer:
                #current player guessed correctly
                return crtPlayer

        #none of the players have guessed so there is no winner yet
        return None