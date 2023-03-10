import sys
import random
import time

board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def displayWelcome():
    print('','='*30+" WELCOME! "+'='*30,)
    print('|                                                                      |')
    print('|                             TIC TAC TOE                              |')
    print('|                                                                      |')
    print('|                        This is a 1 vs 1 Game                         |')
    print('|                                                                      |')
    print('|     Note: <PLAYER1> plays with "X" and <PLAYER2> plays with "O"      |')
    print('|                                                                      |')
    print('|           Note: The first player will be chosen randomly.            |')
    print('|                                                                      |')
    print('|                (: (: (: Have fun playing it :) :) :)                 |')
    print('|                                                                      |')
    print('','='*70)

def displayBoard(board):
    for i in range(3):
        print("-------------")
        for j in range(3):
            if j == 2:
                print('|',board[i][j],'|')
                continue
            print('|',board[i][j],end=' ')
    print("-------------")

def checkPosition(pos):
    if pos in [1,2,3,4,5,6,7,8,9]:
        if board[int(pos/3-(1/30))][pos%3-1] in ['X','O']:
            print('This position is already filled !!\n')
            return False
        else:
            return True

    else:
        print('Position non Valid !! Please Enter a valid position\n')
        return False

def getRowCol(pos):
    if pos == 1:
        return(0,0)
    elif pos == 2:
        return(0,1)
    elif pos == 3:
        return(0,2)
    elif pos == 4:
        return(1,0)
    elif pos == 5:
        return(1,1)
    elif pos == 6:
        return(1,2)
    elif pos == 7:
        return(2,0)
    elif pos == 8:
        return(2,1)
    elif pos == 9:
        return(2,2)
    else:
        print('Invalid Position, try again')
        return 0

def checkWin(xo):
    for row in board:
        if row.count(xo) == 3:
            return True

    for i in range(3):
        column = [board[j][i] for j in range(3)]
        if column.count(xo) == 3:
            return True

    diagonal1 = [board[i][i] for i in range(3)]
    diagonal2 = [board[i][2-i] for i in range(3)]

    if diagonal1.count(xo) == 3 or diagonal2.count(xo) == 3:
        return True

    return False

def checkDraw(board):
    for row in board:
        for i in range(1,10):
            if i in row: return False
    return True

def startPlayer():
    rand = random.randint(1,2)
    if rand == 1:
        return True
    else:
        return False

player = startPlayer()

def play(board):

    displayWelcome()
    time.sleep(2)
    player = startPlayer()
    
    while True:
        displayBoard(board)

        if player:
            print('PLAYER1 is playing...,',end=' ')
            xo = 'X'
        else:
            print('PLAYER2 is playing...,',end=' ')

            xo = 'O'

        print('Please enter "'+ xo +'"',end=' ')
        value_pos = int(input('in the position: '))

        if value_pos not in [1,2,3,4,5,6,7,8,9]:
            print('Please enter a valid position')
            continue

        row,col = getRowCol(value_pos)

        if board[row][col] != 'X' and board[row][col] != 'O':
            board[row][col] = xo

        else:
            print("That spot is already taken.")
            continue

        if checkWin(xo):
            displayBoard(board)
            print("Player 1 Wins !" if player == True else "Player 2 Wins !")
            sys.exit(0)

        if checkDraw(board):
            displayBoard(board)
            print("It's a tie!")
            sys.exit(0)
        
        player =  not player

play(board)
