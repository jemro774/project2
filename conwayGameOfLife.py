#Jack Robey 
#1/7/18
#conwayGameOfLife.py 

from ggame import *

black = Color(0x000000,1)
white = Color(0xFFFFFF,1)
grey = Color(0xD3D3D3,1)

blackOutline = LineStyle(1,black)

whiteSquare = RectangleAsset(40,40,blackOutline,white)
blackSquare = RectangleAsset(40,40,blackOutline,black)
textBox = RectangleAsset(80,40,blackOutline,grey)
text = TextAsset('New Generation', fill=black, style='bold 12pt Times')

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
    Sprite(textBox,(0,440))
    Sprite(text,(2,442))

def mouseClick(event):
    if event.x > 0 and event.x < 80 and event.y > 440 and event.y < 480:
        nextGeneration()
    else:
        row = event.x//40
        col = event.y//40
        data['board'][row][col] = '1'
        redrawAll()

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
    for row in range(0,10): 
        for col in range(0,10):
            if data['board'][row][col] == '1':
                if numNeighbors(row,col) < 2:
                    newBoard[row][col] = '0'
                if numNeighbors(row,col) == 2 or numNeighbors(row,col) == 3:
                    newBoard[row][col] = '1'
                if numNeighbors(row,col) > 3:
                    newBoard[row][col] = '0'
            if data['board'][row][col] == '0':
                if numNeighbors(row,col) == 3:
                    newBoard[row][col] = '1'
    data['board'] = newBoard
    redrawAll()

if __name__ == '__main__':
    
    data = {}
    data['board'] = buildBoard()
    
    redrawAll()
    
    App().listenMouseEvent('click',mouseClick)
    App().run()