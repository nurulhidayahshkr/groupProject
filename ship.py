class SinkShip:

#initialize filled levels and assign random word

        def __init__(self, fillLevels,randomWord):
                self.fillLevels = fillLevels
                self.solve = '-' * len(randomWord)

#increase filled level by 1 by water

        def incFillLevel(self):
                self.fillLevels += 1

#return current levels fill in the ship

        def getWaterFill(self):
                return self.fillLevels

#return current state solve word

        def getSolve(self):
                return self.solve

#string representation of the ship visual

        def getSinkShip(self):
                # ("______________________________")
                # ("\\___________________________/")
                # (" \\_________________________/")
                # ("  \\_______________________/")
                # ("   \\_____________________/")
                # ("    \\___________________/")
                # ("     \\_________________/")
                # ("      \\_______________/")
                # ("       \\_____________/")
                # ("wwwwwwww\\___________/wwwwwwwwwwww")
                # ("wwwwwwwww\\_________/wwwwwwwwwwwww")
                # ("wwwwwwwwww\\_______/wwwwwwwwwwwwwww")
                # ("wwwwwwwwwww\\_____/wwwwwwwwwwwwwww")
                # ("wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww")


                # Empty ship array
                shipEmpty = ["_____________________________","\\___________________________/"," \\_________________________/","  \\_______________________/","   \\_____________________/","    \\___________________/","     \\_________________/","      \\_______________/","       \\_____________/","vvvvvvvv\\___________/vvvvvvvvvvvv","vvvvvvvvv\\_________/vvvvvvvvvvvvv","vvvvvvvvvv\\_______/vvvvvvvvvvvvvvv","vvvvvvvvvvv\\_____/vvvvvvvvvvvvvvv","vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv"]


                # Filled ship array
                shipFill = ["_____________________________","\\wwwwwwwwwwwwwwwwwwwwwwwwwww/"," \\wwwwwwwwwwwwwwwwwwwwwwwww/","  \\wwwwwwwwwwwwwwwwwwwwwww/","   \\wwwwwwwwwwwwwwwwwwwww/","    \\wwwwwwwwwwwwwwwwwww/","     \\wwwwwwwwwwwwwwwww/","      \\wwwwwwwwwwwwwww/","       \\wwwwwwwwwwwww/","vvvvvvvv\\wwwwwwwwwww/vvvvvvvvvvvv","vvvvvvvvv\\wwwwwwwww/vvvvvvvvvvvvv","vvvvvvvvvv\\wwwwwww/vvvvvvvvvvvvvvv","vvvvvvvvvvw\\wwwww/vvvvvvvvvvvvvvv","vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv"]

                ship = "\n"


                # String to create visual of a filled ship up to specified level

                for i in range(0,len(shipEmpty)):

                        if i + self.fillLevels < len(shipEmpty) - 1:
                                ship += shipEmpty[i] + "\n"
                        else:
                                ship += shipFill[i] + "\n"

                return ship



#update state of solve word

        def setWordSolve(self,letter,word):

                arr = list(self.solve)
                arrStr = ""

                for i in range(0,len(word)):
                        if letter == word[i]:
                                if arr[i] == '-':
                                        arr[i] = letter

                self.solve = arrStr.join(arr)



#return after the game has been won

        def gameOver(self):
                return "-" not in self.solve

