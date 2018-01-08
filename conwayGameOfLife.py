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
    return [['0']*10,['0']*10,['0']*10,['0']*10,['0']*10,['0']*10,['0']*10,['0']*10,['0']*10,['0']*10]

def redrawAll():
    for item in App().spritelist[:]:
        item.destroy()
    for row in range(0,10): 
        for col in range(0,10):
            if data['board'][row][col] == '0':
                Sprite(whiteSquare,(40*row,40*col))
            if data['board'][row][col] == '1':
                Sprite(blackSquare,(40*row,40*col))
    Sprite(blackSquare,(0,400))

def mouseClick(event):
    row = event.x//40
    col = event.y//40
    data['board'][row][col] = '1'
    redrawAll()
    if event.x > 0 and event.x < 40 and event.y > 400 and event.y < 440:
        nextGeneration()

def numNeighbors(row,col):
    num = 0
    if col < 9 and data['board'][row][col+1] == '1':
        num = num + 1
    if row < 9 and col < 9 and data['board'][row+1][col+1] == '1':
        num = num + 1
    if row < 9 and data['board'][row+1][col] == '1':
        num = num + 1
    if row > 0 and data['board'][row-1][col] == '1':
        num = num + 1
    if row > 0 and col < 9 and data['board'][row-1][col+1] == '1':
        num = num + 1
    if row > 0 and col > 0 and data['board'][row-1][col-1] == '1':
        num = num + 1
    if col > 0 and data['board'][row][col-1] == '1':
        num = num + 1
    if row < 9 and col > 0 and data['board'][row+1][col-1] == '1':
        num = num + 1
    return num

def nextGeneration():
    newBoard = [['0']*10,['0']*10,['0']*10,['0']*10,['0']*10,['0']*10,['0']*10,['0']*10,['0']*10,['0']*10]
    if data['board'][row][col] == '1':
        if numNeighbors(row,col) < 2:
            newBoard[row][col] == '0'
        if numNeighbors(row,col) == 2 or 3:
            newBoard[row][col] == '1'
        if numNeighbors(row,col) > 3:
            newBoard[row][col] == '0'
    if data['board'][row][col] == '0':
        if numNeighbors(row,col) == 3:
            newBoard[row][col] == '1'
    newBoard = data['board']

if __name__ == '__main__':
    
    data = {}
    data['board'] = buildBoard()
    
    redrawAll()
    
    App().listenMouseEvent('click',mouseClick)
    App().run()