import random
import time

global brd
brd = [[1,2,3],[4,5,6],[7,8,9]]

def convertRowToCol(board):
    tempboard = []
    for i in range(3):
        temp = []
        for j in range(3):
            temp.append(board[j][i])
        tempboard.append(temp)
    return tempboard

def DisplayBoard():
    for i in range(3):
        print("-------------")
        for j in range(3):
            if j == 2:
                print('|',brd[i][j],'|')
                continue
            print('|',brd[i][j],end=' ')
    print("-------------")
        

def CheckPosition(cpos):
    if cpos in [1,2,3,4,5,6,7,8,9]:
        if brd[int(cpos/3-(1/30))][cpos%3-1] in ['X','O']:
            print('This position is already filled !!\n')
            return False
        else:
            return True

    else:
        print('Position non Valid !! Please Enter a valid position\n')
        return False

def FillPostion(fpos,fplayer):
    finput = ''

    if fplayer:
        finput = 'x'
    else:
        finput = 'o'

    if(CheckPosition(fpos)):
            if fpos in [1,2,3]:
                brd[int(fpos/3-(1/30))][(fpos%3)-1] = finput

            elif fpos in [4,5,6]:
                brd[int(fpos/3-(1/30))][(fpos%3)-1] = finput

            elif fpos in [7,8,9]:
                brd[int(fpos/3-(1/30))][(fpos%3)-1] = finput

            return True
        
    else:
        return False
"""
def checkWon():
    check = False
    colboard = convertRowToCol(brd)

    for i in range(3):
        if brd[i] == ['X','X','X']:
            print('Player with "X" won !!\n')
            check = True

        elif brd[i] == ['O','O','O']:
            print('Player with "O" won !!\n')
            check = True
    
        elif colboard[i] == ['X','X','X']:
            print('Player with "X" won !!\n')
            check = True

        elif colboard[i] == ['O','O','O']:
            print('Player with "O" won !!\n')
            check = True

    if ((brd[0][0] == brd[1][1] and brd[0][0] == brd[2][2] == 'x' ) or (brd[0][2] == brd[1][1] and brd[1][1] == brd[2][0] )):
        print('Player with "X" won !!\n')
        check = True

    elif  ((brd[0][0] == brd[1][1] and brd[0][0] == brd[2][2] == 'o' ) or (brd[0][2] == brd[1][1] and brd[1][1] == brd[2][0] )):
        print('Player with "O" won !!\n')
        check = True

    return check
 """
def checkRowsCols():
    check = False
    colboard = convertRowToCol(brd)

    for i in range(3):
        if brd[i] == ['X','X','X']:
            print('Player with "X" won !!\n')
            check = True

        elif brd[i] == ['O','O','O']:
            print('Player with "O" won !!\n')
            check = True
    
        elif colboard[i] == ['X','X','X']:
            print('Player with "X" won !!\n')
            check = True

        elif colboard[i] == ['O','O','O']:
            print('Player with "O" won !!\n')
            check = True

        return check

def checkDiagonal():
    check = False
    if ((brd[0][0] == brd[1][1] and brd[0][0] == brd[2][2] == 'x' ) or (brd[0][2] == brd[1][1] and brd[1][1] == brd[2][0] )):
        print('Player with "X" won !!\n')
        check = True

    elif  ((brd[0][0] == brd[1][1] and brd[0][0] == brd[2][2] == 'o' ) or (brd[0][2] == brd[1][1] and brd[1][1] == brd[2][0] )):
        print('Player with "O" won !!\n')
        check = True

    return check

def checkDraw():
    check = False
    for i in range(1,10):
        if (i in brd[0]) or (i in brd[1]) or (i in brd[2]):
            check = True
            break

    return check


def checkGameOver():
    if checkRowsCols() or checkDiagonal():
        return True
    elif not checkDraw():
        print('Draw!!')
        return True
    else:
        return False

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

displayWelcome()

time.sleep(2)

def startPlayer():
    rand = random.randint(1,2)
    if rand == 1:
        return True
    else:
        return False

player = startPlayer()

DisplayBoard()


while True:
    if player:
        print('PLAYER1 is playing...,',end=' ')
        xo = ['X','O']
    else:
        print('PLAYER2 is playing...,',end=' ')
        xo = ['O','X']

    print('Please enter "'+xo[0]+'"',end=' ')
    xpos = int(input('in the position: '))
    if(FillPostion(xpos,player)):
        DisplayBoard()
        if checkGameOver():
            break
    else:
        continue

    player = not player
