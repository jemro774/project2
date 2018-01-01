#Jack Robey 
#12/14/17 
#conwayGameOfLife.py 

from ggame import *

black = Color(0x000000,1)
white = Color(0xFFFFFF,1)

blackOutline = LineStyle(1,black)

whiteSquare = RectangleAsset(40,40,blackOutline,white)
blackSquare = RectangleAsset(40,40,blackOutline,black)

def buildBoard():
    board = ['0'*10,'0'*10,'0'*10,'0'*10,'0'*10,'0'*10,'0'*10,'0'*10,'0'*10,'0'*10]

def redrawAll(): 
    for row in range(0,10): 
        for col in range(0,10): 
            Sprite(whiteSquare,(40*row,40*col))

def mouseClick(event):
    for row in range(0,10): 
        for col in range(0,10):
            if event.x > 40*row and event.x < 40*row+40 and event.y > 40*col and event.y < 40*col+40:
                Sprite(blackSquare,(40*row,40*col))

if __name__ == '__main__':

    buildBoard()
    
    redrawAll()
    
    App().listenMouseEvent('click',mouseClick)
    App().run()