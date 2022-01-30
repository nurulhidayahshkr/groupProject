import random
from ship  import *

def setupShip():

        words = ['lexus', 'westlife', 'mangosteen', 'thalweg']

        #to generate random word
        randomWord = random.choice(words)

        #to create instance of SinkShip
        ship = SinkShip(0,randomWord)

        instr  = "\n Instruction :\n "
        instr += "\n\n Here are your ship. It is being attacked by the pirates!!!\n"
        instr += "\n\n You must guess the secret word to save it!!!\n"
        instr += "\n\n If you guess a letter incorrectly, the pirates fill up a level of ship with water!!\n"
        instr += "\n\n ENTER \\q to quit the game at any time....\n"

        instr += ship.getSinkShip()

        return (instr,ship,randomWord)


      
#execute shipSink game

def startShipSink(guess,word,ship):

        # Check if the letter guessed is in the word
        if guess in word:
                ship.setWordSolve(guess,word)
                return True

        else: # increase filled level by 1 by water
                ship.incFillLevel()

        return False
