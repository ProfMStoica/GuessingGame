"""Represents the guessing game application responsible for user interaction and for creating
and running the guessin game.
"""
from guessinggame import GuessingGame

class Application:
   def run(self):
      #create the game
      game = GuessingGame()

      #start the game 
      game.start()
       