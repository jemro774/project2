#Jack Robey 
#12/14/17 
#conwayGameOfLife.py 

from ggame import *

black = Color(0x000000,1)
white = Color(0xFFFFFF,1)

blackOutline = LineStyle(1,black)

square = RectangleAsset(40,40,blackOutline,white)

def buildBoard():
    board = [0*10,0*10,0*10,0*10,0*10,0*10,0*10,0*10,0*10,0*10]

def redrawAll(): 
    for row in range(0,10): 
        for col in range(0,10): 
            Sprite(square,(40*row+100,40*col+64))

if __name__ == '__main__':

    redrawAll()
    
    App().run()

