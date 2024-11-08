"""Defines the game logic for the guessing game"""

import random
from player import Player


class GuessingGame:
    def __init__(self):
        self._answer = -1
        self._roundCount = 0

        #create the three player objects
        self._larry = Player("Larry")
        self._curly = Player("Curly")
        self._moe = Player("Moe")

    def start(self):
        #pick a number to be guessed between  0 and 9
        self._answer = random.randint(0, 9)

        #repeat asking the user to play for each round of the game until someone wins
        winner = None
        while winner == None:
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
            winner = self.determineWinner()

        #let the user know who won
        print(f"{winner.getName()} won the game in {self._roundCount} rounds with the guess {winner.getGuess()}")

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