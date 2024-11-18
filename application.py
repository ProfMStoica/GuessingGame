"""Represents the guessing game application responsible for user interaction and for creating
and running the guessin game.
"""
from guessinggame import GuessingGame

class Application:
   def run(self):
      #create the game
      game = GuessingGame()

      #repeat playing the game for as long as the user wants to play
      playAgain = True
      while playAgain:      
         #start the game 
         game.start()

         #let the user know who won
         print(f"{game.getWinner().getName()} won the game in {game.getRoundCount()} rounds with the guess {game.getWinner().getGuess()}")


         #check if the user wants to play again
         playAgain = self.checkPlayAgain()

   def checkPlayAgain(self):
      """Asks the user if they want to play again and returns true/false depending on the answer"""
      #ask the user if the want to play the game
      playAgainInput = input("Would you like to play again? [y/n]: ")

      #determine if they do or not and return True/False accordingly
      return playAgainInput.upper() == "Y"
      # if playAgainInput.upper() == "Y":
      #    return True
      # else:
      #    return False

       