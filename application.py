"""Represents the guessing game application responsible for user interaction and for creating
and running the guessin game.
"""
from guessinggame import GuessingGame

class Application:
   def run(self):
      #create the game
      game = GuessingGame()

      #ask the user to determine the guess range
      userMinGuess, userMaxGuess = self.askForGuessRange()
      GuessingGame.setGuessRange(userMinGuess, userMaxGuess)

      #repeat playing the game for as long as the user wants to play
      playAgain = True
      while playAgain:      
         #start the game 
         game.start()

         #let the user know who won
         print(f"{game.getWinner().getName()} won the game in {game.getRoundCount()} rounds with the guess {game.getWinner().getGuess()}")


         #check if the user wants to play again
         playAgain = self.checkPlayAgain()

   def askForGuessRange(self):      
      while True:
         try:
            #ask the user for the range TODO: if invalid ask the users to try again
            userMinGuess = int(input("Please enter the minimum guess for players: "))
            userMaxGuess = int(input("Please enter the maximum guess for players: "))
            
            #return the range of valid guesses
            return (userMinGuess, userMaxGuess)
         except ValueError as ex:
            #the input is incorrect, let the user know
            print("Please enter a valid number")
   
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

       