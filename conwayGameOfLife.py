#Jack Robey 
#12/14/17 
#conwayGameOfLife.py 

from ggame import *

black = Color(0x000000,1)
white = Color(0xFFFFFF,1)

blackOutline = LineStyle(1,black)

square = RectangleAsset(75,75,blackOutline,white)

buildBoard(): 
    for row in range(0,10): 
        for col in range(0,10): 
            print(board[row][col],' ',end = '') 
        print()

if __name__ == '__main__':

buildBoard()

Sprite(square)
App().run()

