"""Represents the guessing game application responsible for user interaction and for creating
and running the guessin game.
"""
from exceptions import InvalidGuessRange, OperationCancelled
from guessinggame import GuessingGame
from interactiveplayer import InteractivePlayer
from player import Player

class Application:
   def __init__(self):
      #create the game
      self._game = GuessingGame()

   def run(self):
      #ask the user to determine the guess range
      userMinGuess, userMaxGuess = self.askForGuessRange()
      GuessingGame.setGuessRange(userMinGuess, userMaxGuess)

      #configure the game with its players
      self.setupGame()

      #repeat playing the game for as long as the user wants to play
      playAgain = True
      while playAgain:      
         #start the game 
         self._game.start()

         #let the user know who won
         print(f"{self._game.getWinner().getName()} won the game in {self._game.getRoundCount()} rounds with the guess {self._game.getWinner().getGuess()}")


         #check if the user wants to play again
         playAgain = self.checkPlayAgain()

   def setupGame(self):
      """Interact with the user to determine the number of players and their information (name and type)
         #configure the game so that it is played in the confirmation determined by the user"""
      #repeat asking for player and their characteristics until the user is done configuring the game
      morePlayers = True
      while morePlayers:
         #ask the user for the player's name
         playerName = input("Please enter the name of the player [ENTER to exit]")
         if len(playerName) == 0:
             #the user does not want anymore players, they  pressed ENTER
             morePlayers = False
         else:            
            #ask the user for the player's type, AI or Interactive
            playerType = input("Please enter the type of player (A for AI, H for Human)")

            #create a player with the given name and 
            player = None #optional in Python
            if playerType.upper() == "A":
               player = Player(playerName)
            elif playerType.upper() == "H":
               player = InteractivePlayer(playerName, self._game)
               
            #add the player to the game
            self._game.addPlayer(player)

   def askForGuessRange(self):      
      while True:
         try:
            #ask the user for the range TODO: if invalid ask the users to try again
            userMinGuessInput = input("Please enter the minimum guess for players: [press ENTER to cancel]")
            if len(userMinGuessInput) == 0:
               raise OperationCancelled("Setting the minimum guess was cancelled by the user")

            userMaxGuessInput = input("Please enter the maximum guess for players: [press ENTER to cancel]")
            if len(userMaxGuessInput) == 0:
               raise OperationCancelled("Setting the maximumg guess was cancelled by the user ")

            #transform the user input
            userMinGuess = int(userMinGuessInput)
            userMaxGuess = int(userMaxGuessInput)
            if userMinGuess > userMaxGuess:
               raise InvalidGuessRange(f"The range entered is not valid because the maximum guess is lower than the mininmum guess.")
            
            #return the range of valid guesses
            return (userMinGuess, userMaxGuess)
         except OperationCancelled as ex:
            print(f"{ex}\nThe game will continue with the default range of 0 and 9")
            return (0, 9)
         except InvalidGuessRange as ex:            
            #let the user know whta the error was
            print(ex)
            print("The program will use the reversed range instead.")
            
            #exchange the values of userMinGuess and userMaxGuess to handle this error
            tempGuess = userMinGuess
            userMinGuess = userMaxGuess
            userMaxGuess = tempGuess

            #return the corrected range to the caller
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

       