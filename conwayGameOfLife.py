#Jack Robey 
#12/14/17 
#conwayGameOfLife.py 

buildBoard(): 
    for row in range(0,10): 
        for col in range(0,10): 
            print(board[row][col],' ',end = '') 
        print() 

buildBoard() 

if __name__ == '__main__':
