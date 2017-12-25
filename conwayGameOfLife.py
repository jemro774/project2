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
    if event.x > 0 and event.x < 40 and event.y > 0 and event.y < 40:
        Sprite(blackSquare,(0,0))
    elif event.x > 0 and event.x < 40 and event.y > 40 and event.y < 80:
        Sprite(blackSquare,(0,40))
    elif event.x > 0 and event.x < 40 and event.y > 80 and event.y < 120:
        Sprite(blackSquare,(0,80))
    elif event.x > 0 and event.x < 40 and event.y > 120 and event.y < 160:
        Sprite(blackSquare,(0,120))
    elif event.x > 0 and event.x < 40 and event.y > 160 and event.y < 200:
        Sprite(blackSquare,(0,160))
    elif event.x > 0 and event.x < 40 and event.y > 200 and event.y < 240:
        Sprite(blackSquare,(0,200))
    elif event.x > 0 and event.x < 40 and event.y > 240 and event.y < 280:
        Sprite(blackSquare,(0,240))
    elif event.x > 0 and event.x < 40 and event.y > 280 and event.y < 320:
        Sprite(blackSquare,(0,280))

if __name__ == '__main__':

    buildBoard()
    
    redrawAll()
    
    App().listenMouseEvent('click',mouseClick)
    App().run()