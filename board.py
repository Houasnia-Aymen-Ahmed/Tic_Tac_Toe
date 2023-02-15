import random
global brd
brd = [[1,'x',3],[4,'x',6],[7,'x',9]]

def convertRowToCol(board):
    tempboard = []
    for i in range(3):
        temp = []
        for j in range(3):
            temp.append(board[j][i])
        tempboard.append(temp)
    return tempboard

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
        if i in brd:
            check = True

    return check


def checkGameOver():
    if checkRowsCols() or checkDiagonal():
        return True
    elif not checkDraw():
        print('Draw!!')
        return True
    else:
        return False