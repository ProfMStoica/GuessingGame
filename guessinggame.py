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

        #define a dictionary of players that organizes players by their names
        #name --> Player instances
        self._playerStore = {}

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

    def addPlayer(self, player):
        """Adds a player to the list of players"""
        self._playerStore[player.getName()] = player

    def start(self):
        #pick a number to be guessed in the game's guess range
        self._answer = random.randint(GuessingGame.getMinGuess(), GuessingGame.getMaxGuess())

        #repeat asking the user to play for each round of the game until someone wins
        self._roundCount = 0
        self._winner = None
        while self._winner == None:
            #increment the round
            self._roundCount += 1

            #ask each player to play and show their guess
            for playerName in self._playerStore:                
                #search for the player with the given name (key)
                player = self._playerStore[playerName]
                
                #ask the current player to play in the round
                player.play()
                print(f"{player.getName()} guessed {player.getGuess()}")

            #determine if anybody won
            self._winner = self.determineWinner()

    def determineWinner(self):
        #TODO: replace the for loop with a for-each loop
        for playerName in self._playerStore:
            #search for the player with this name
            player = self._playerStore[playerName]
            
            #check the current player to see if their guess matched the answer            
            if player.getGuess() == self._answer:
                #current player guessed correctly
                return player

        #none of the players have guessed so there is no winner yet
        return None