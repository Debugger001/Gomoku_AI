import numpy as np
from Gomoku import *
BOARD_SIZE = 15

class Node(object):

    def __init__(self, val=0):
        self.value = val
        self.move = []
        self.board = []
        self.children = []
        self.parent = None

    def Childof(self, nodeP):
        self.parent = nodeP
        nodeP.children.append(self)

    def Printout(self, depth=0):
        s = " " * depth
        print(s + str(self.value))
        for child in self.children:
            child.Printout(depth + 1)


#
# def Game_tree(board):
#     for i in range(BOARD_SIZE):
#         for j in range(BOARD_SIZE):


myvalue_1 = {
"FIVE": 10000000,
"Lv4": 100000,
"Dd4a": 500,
"Dd4b/c": 500,
"Lv3": 300,
"Dd3a0": 20,
"Dd3a1": 20,
"Dd3b": 20,
"Dd3c/d": 20,
"Lv2": 10,
"Dd2a": 1,
}

opvalue_1 = {
"FIVE": 10000000,
"Lv4": 1000000,
"Dd4a": 1000000,
"Dd4b/c": 1000000,
"Lv3": 10000,
"Dd3a0": 100,
"Dd3a1": 100,
"Dd3b": 100,
"Dd3c/d": 100,
"Lv2": 100,
"Dd2a": 10,
}

myvalue = {
"FIVE": 10000000,
"Lv4": 10000,
"Dd4a": 500,
"Dd4b/c": 500,
"Lv3": 300,
"Dd3a0": 50,
"Dd3a1": 50,
"Dd3b": 50,
"Dd3c/d": 50,
"Lv2": 10,
"Dd2a": 1,
}

opvalue = {
"FIVE": 10000000,
"Lv4": 10000,
"Dd4a": 500,
"Dd4b/c": 500,
"Lv3": 300,
"Dd3a0": 50,
"Dd3a1": 50,
"Dd3b": 50,
"Dd3c/d": 50,
"Lv2": 10,
"Dd2a": 1,
}

BOARD_SIZE = 15
EMPTY = 0
ME = 1
OTHER = 2

# nowBoard = [[2,0,2,2,2,1,0,0],
#             [0,1,0,0,1,0,0,0],
#             [0,0,1,0,0,1,0,2],
#             [0,0,1,0,2,0,2,2],
#             [2,0,0,2,2,1,0,2],
#             [0,0,1,0,2,2,2,1],
#             [0,1,0,1,1,2,0,0],
#             [0,0,0,2,0,0,0,0]]


emptyBoard = np.zeros((15, 15))
emptyBoard[7][7] = 1
emptyBoard[7][8] = 2
emptyBoard[6][5] = 2



coord = []
for i in range(BOARD_SIZE):
    temp = []
    for j in range(BOARD_SIZE):
        temp.append([i,j])
    coord.append(temp)
coord = np.array(coord)

def eval(node, maxdepth):
    shapedict = {}
    for r in range(BOARD_SIZE):
        for c in range(BOARD_SIZE):
            shapedict[str(r) + ' ' + str(c)] = []
    myside = ME
    opside = OTHER
    ismyside = True
    nowBoard = node.board
    shapes = []

    # Lv4 _oooo_
    # Dd4 _oooox, _ooo_ox, xoo_oox
    # Lv3 __ooo__
    # Dd3 xooo__, _o_oo_, xo__oox, xo_o_ox
    # Lv2 ___oo___, xoo___, __o_o__, _o__o_

    # Direction: 0: horizontal, 1: vertical, 2: upperright, 3: downright

    # Shapes are stored in format: [eigencoord, type, direction]
    for ii in range(2):
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                # FIVE ooooo
                # FIVE horizontal
                if nowBoard[i][j]==myside and j+4<BOARD_SIZE:
                    if nowBoard[i][j+1]==myside and nowBoard[i][j+2]==myside and nowBoard[i][j+3]==myside and nowBoard[i][j+4]==myside:
                        newshape = [[i,j], "FIVE", 0, ismyside]
                        shapes.append(newshape)
                if nowBoard[i][j]==myside and i+4<BOARD_SIZE:
                    if nowBoard[i+1][j]==myside and nowBoard[i+2][j]==myside and nowBoard[i+3][j]==myside and nowBoard[i+4][j]==myside:
                        newshape = [[i,j], "FIVE", 1, ismyside]
                        shapes.append(newshape)
                if nowBoard[i][j]==myside and i-4>=0 and j+4<BOARD_SIZE:
                    if nowBoard[i-1][j+1]==myside and nowBoard[i-2][j+2]==myside and nowBoard[i-3][j+3]==myside and nowBoard[i-4][j+4]==myside:
                        newshape = [[i,j], "FIVE", 2, ismyside]
                        shapes.append(newshape)
                if nowBoard[i][j]==myside and i+4<BOARD_SIZE and j+4<BOARD_SIZE:
                    if nowBoard[i+1][j+1]==myside and nowBoard[i+2][j+2]==myside and nowBoard[i+3][j+3]==myside and nowBoard[i+4][j+4]==myside:
                        newshape = [[i,j], "FIVE", 3, ismyside]
                        shapes.append(newshape)
                # Lv4, Dd4a _oooo_, _oooox / xoooo_
                # Lv4, Dd4a horizontal
                if j+3 < BOARD_SIZE and nowBoard[i][j] == myside:
                    MEcounter = 0
                    for n in range(3):
                        if nowBoard[i][j+n+1] == myside:
                            MEcounter += 1
                        else:
                            break
                    if MEcounter == 3 and j>0:
                        if nowBoard[i][j-1] == EMPTY and j+4<BOARD_SIZE:
                            if nowBoard[i][j+4] == EMPTY:
                                newshape = [[i, j], "Lv4", 0, ismyside]
                                shapes.append(newshape)
                    if MEcounter == 3:
                        isDd4a = False
                        if j>0 and j+4<BOARD_SIZE:
                            if nowBoard[i][j-1] == EMPTY and nowBoard[i][j+4]==opside:
                                isDd4a = True
                        if j>0 and j+4==BOARD_SIZE:
                            if nowBoard[i][j-1] == EMPTY:
                                isDd4a = True
                        if j+4<BOARD_SIZE and j>0:
                            if nowBoard[i][j+4] == EMPTY and nowBoard[i][j-1]==opside:
                                isDd4a = True
                        if j+4<BOARD_SIZE and j==0:
                            if nowBoard[i][j+4] == EMPTY:
                                isDd4a = True
                        if isDd4a:
                            newshape = [[i, j], "Dd4a", 1, ismyside]
                            shapes.append(newshape)
                # Lv4, Dd4a vertical
                if i+3 < BOARD_SIZE and nowBoard[i][j] == myside:
                    MEcounter = 0
                    for n in range(3):
                        if nowBoard[i+n+1][j] == myside:
                            MEcounter += 1
                        else:
                            break
                    if MEcounter == 3 and i>0 and i+4<BOARD_SIZE:
                        if nowBoard[i-1][j] == EMPTY and nowBoard[i+4][j] == EMPTY:
                            newshape = [[i, j], "Lv4", 1, ismyside]
                            shapes.append(newshape)
                    if MEcounter == 3:
                        isDd4a = False
                        if i>0 and i+4<BOARD_SIZE:
                            if nowBoard[i-1][j] == EMPTY and nowBoard[i+4][j]==opside:
                                isDd4a = True
                        if i>0 and i+4==BOARD_SIZE:
                            if nowBoard[i-1][j] == EMPTY:
                                isDd4a = True
                        if i+4<BOARD_SIZE and i>0:
                            if nowBoard[i+4][j] == EMPTY and nowBoard[i-1][j]==opside:
                                isDd4a = True
                        if i+4<BOARD_SIZE and i==0:
                            if nowBoard[i+4][j] == EMPTY:
                                isDd4a = True
                        if isDd4a:
                            newshape = [[i, j], "Dd4a", 1, ismyside]
                            shapes.append(newshape)
                # Lv4, Dd4a upperright
                if i-3>=0 and j+3<BOARD_SIZE and nowBoard[i][j] == myside:
                    MEcounter = 0
                    for n in range(3):
                        if nowBoard[i-n-1][j+n+1] == myside:
                            MEcounter += 1
                        else:
                            break
                    if MEcounter == 3 and i+1<BOARD_SIZE and j>0 and i>3 and j+4<BOARD_SIZE:
                        if nowBoard[i+1][j-1] == EMPTY and nowBoard[i-4][j+4] == EMPTY:
                            newshape = [[i, j], "Lv4", 2, ismyside]
                            shapes.append(newshape)
                    if MEcounter == 3:
                        isDd4a = False
                        if (i+1==BOARD_SIZE or j==0) and (i==3 or j+4==BOARD_SIZE or (i>3 and j+4<BOARD_SIZE and nowBoard[i-4][j+4]!=myside)):
                            isDd4a = True
                        if (i==3 or j+4==BOARD_SIZE) and (i+1<BOARD_SIZE and j>0 and nowBoard[i+1][j-1]!=myside):
                            isDd4a = True
                        if (i+1<BOARD_SIZE and j>0 and i>3 and j+4<BOARD_SIZE) and ((nowBoard[i+1][j-1]==opside and nowBoard[i-4][j+4]==EMPTY) or (nowBoard[i+1][j-1]==EMPTY and nowBoard[i-4][j+4]==opside)):
                            isDd4a = True
                        if isDd4a:
                            newshape = [[i, j], "Dd4a", 2, ismyside]
                            shapes.append(newshape)
                # Lv4, Dd4a downright
                if i+3<BOARD_SIZE and j+3<BOARD_SIZE and nowBoard[i][j] == myside:
                    MEcounter = 0
                    for n in range(3):
                        if nowBoard[i+n+1][j+n+1] == myside:
                            MEcounter += 1
                        else:
                            break
                    if MEcounter == 3 and i>0 and j>0 and nowBoard[i-1][j-1] == EMPTY and i+4<BOARD_SIZE and j+4<BOARD_SIZE and nowBoard[i+4][j+4] == EMPTY:
                        newshape = [[i,j], "Lv4", 3, ismyside]
                        shapes.append(newshape)
                    if MEcounter == 3:
                        if (nowBoard[i][j] == EMPTY and nowBoard[i+5][j+5] == opside) or (nowBoard[i][j] == opside and nowBoard[i+5][j+5] == EMPTY):
                            newshape = [[i+1, j+1], "Dd4a", 3, ismyside]
                            shapes.append(newshape)
                        isDd4a = False
                        if (i==0 or j==0) and (i+4==BOARD_SIZE or j+4==BOARD_SIZE or (i+4<BOARD_SIZE and j+4<BOARD_SIZE and nowBoard[i+4][j+4]!=myside)):
                            isDd4a = True
                        if (i+4==BOARD_SIZE or j+4==BOARD_SIZE) and (i>0 and j>0 and nowBoard[i-1][j-1]!=myside):
                            isDd4a = True
                        if i>0 and j>0 and i+4<BOARD_SIZE and j+4<BOARD_SIZE and ((nowBoard[i-1][j-1]==opside and nowBoard[i+4][j+4]==EMPTY) or (nowBoard[i-1][j-1]==EMPTY and nowBoard[i+4][j+4]==opside)):
                            isDd4a = True
                        if isDd4a:
                            newshape = [[i, j], "Dd4a", 3, ismyside]
                            shapes.append(newshape)
                # Dd4b,c ?ooo_o？ / ?ooo_o? , ?oo_oo? / ?oo_oo？
                # Dd4b,c horizontal
                if j+4<BOARD_SIZE and nowBoard[i][j] == myside:
                    if nowBoard[i][j+4] == myside:
                        MEcounter = 0
                        for n in range(3):
                            if nowBoard[i][j+n+1] == myside:
                                MEcounter += 1
                            elif nowBoard[i][j+n+1] == EMPTY:
                                continue
                            else:
                                MEcounter = 0
                                break
                        isDd4bc = False
                        if MEcounter == 2:
                            if j+5<BOARD_SIZE:
                                if j==0 and nowBoard[i][j+5]!=myside:
                                    isDd4bc = True
                            if j>0:
                                if j+5==BOARD_SIZE and nowBoard[i][j-1]!=myside:
                                    isDd4bc = True
                            if j>0 and j+5<BOARD_SIZE:
                                if nowBoard[i][j-1]!=myside and nowBoard[i][j+5]!=myside:
                                    isDd4bc = True
                        if isDd4bc:
                            newshape = [[i,j], "Dd4b/c", 0, ismyside]
                            shapes.append(newshape)
                            shapedict[str(i)+' '+str(j)].append("Dd4b/c")
                            if nowBoard[i][j+1] == myside:
                                shapedict[str(i)+' '+str(j+1)].append("Dd4b/c")
                            if nowBoard[i][j+2] == myside:
                                shapedict[str(i)+' '+str(j+2)].append("Dd4b/c")
                            if nowBoard[i][j+3] == myside:
                                shapedict[str(i)+' '+str(j+3)].append("Dd4b/c")
                            if nowBoard[i][j+4] == myside:
                                shapedict[str(i)+' '+str(j+4)].append("Dd4b/c")
                # Dd4b,c vertical
                if i+4<BOARD_SIZE and nowBoard[i][j] == myside:
                    if nowBoard[i+4][j] == myside:
                        MEcounter = 0
                        for n in range(3):
                            if nowBoard[i+n+1][j] == myside:
                                MEcounter += 1
                            elif nowBoard[i+n+1][j] == EMPTY:
                                continue
                            else:
                                MEcounter = 0
                                break
                        isDd4bc = False
                        if MEcounter == 2:
                            if i+5<BOARD_SIZE:
                                if i==0 and nowBoard[i+5][j]!=myside:
                                    isDd4bc = True
                            if i>0:
                                if i+5==BOARD_SIZE and nowBoard[i-1][j]!=myside:
                                    isDd4bc = True
                            if i>0 and i+5<BOARD_SIZE:
                                if nowBoard[i-1][j]!=myside and nowBoard[i+5][j]!=myside:
                                    isDd4bc = True
                        if isDd4bc:
                            newshape = [[i,j], "Dd4b/c", 1, ismyside]
                            shapes.append(newshape)
                            shapedict[str(i)+' '+str(j)].append("Dd4b/c")
                            if nowBoard[i+1][j] == myside:
                                shapedict[str(i+1)+' '+str(j)].append("Dd4b/c")
                            if nowBoard[i+2][j] == myside:
                                shapedict[str(i+2)+' '+str(j)].append("Dd4b/c")
                            if nowBoard[i+3][j] == myside:
                                shapedict[str(i+3)+' '+str(j)].append("Dd4b/c")
                            if nowBoard[i+4][j] == myside:
                                shapedict[str(i+4)+' '+str(j)].append("Dd4b/c")
                # Dd4b,c upperright
                if i-4>=0 and j+4<BOARD_SIZE and nowBoard[i][j] == myside:
                    if nowBoard[i-4][j+4] == myside:
                        MEcounter = 0
                        for n in range(3):
                            if nowBoard[i-n-1][j+n+1] == myside:
                                MEcounter += 1
                            elif nowBoard[i-n-1][j+n+1] == EMPTY:
                                continue
                            else:
                                MEcounter = 0
                                break
                        isDd4bc = False
                        if MEcounter == 2:
                            if (i+1==BOARD_SIZE or j==0) and (i==4 or j+5==BOARD_SIZE):
                                isDd4bc = True
                            if (i+1==BOARD_SIZE or j==0) and i>4 and j+5<BOARD_SIZE:
                                if nowBoard[i-5][j+5]!=myside:
                                    isDd4bc = True
                            if (i==4 or j+5==BOARD_SIZE) and i+1<BOARD_SIZE and j>0:
                                if nowBoard[i+1][j-1]!=myside:
                                    isDd4bc = True
                            if i+1<BOARD_SIZE and j>0 and i>4 and j+5<BOARD_SIZE:
                                if nowBoard[i+1][j-1]!=myside and nowBoard[i-5][j+5]!=myside:
                                    isDd4bc = True
                        if isDd4bc:
                            newshape = [[i,j], "Dd4b/c", 2, ismyside]
                            shapes.append(newshape)
                            shapedict[str(i)+' '+str(j)].append("Dd4b/c")
                            if nowBoard[i-1][j+1] == myside:
                                shapedict[str(i-1)+' '+str(j+1)].append("Dd4b/c")
                            if nowBoard[i-2][j+2] == myside:
                                shapedict[str(i-2)+' '+str(j+2)].append("Dd4b/c")
                            if nowBoard[i-3][j+3] == myside:
                                shapedict[str(i-3)+' '+str(j+3)].append("Dd4b/c")
                            if nowBoard[i-4][j+4] == myside:
                                shapedict[str(i-4)+' '+str(j+4)].append("Dd4b/c")
                # Dd4b,c downright
                if i+4<BOARD_SIZE and j+4<BOARD_SIZE and nowBoard[i][j] == myside:
                    if nowBoard[i+4][j+4] == myside:
                        MEcounter = 0
                        for n in range(3):
                            if nowBoard[i+n+1][j+n+1] == myside:
                                MEcounter += 1
                            elif nowBoard[i+n+1][j+n+1] == EMPTY:
                                continue
                            else:
                                MEcounter = 0
                                break
                        isDd4bc = False
                        if MEcounter == 2:
                            if (i==0 or j==0) and j+5<BOARD_SIZE:
                                if nowBoard[i+5][j+5]!=myside:
                                    isDd4bc = True
                            if (i+5==BOARD_SIZE or j+5==BOARD_SIZE) and i-1>=0 and j-1>=0:
                                if nowBoard[i-1][j-1]!=myside:
                                    isDd4bc = True
                            if i>0 and j>0 and i+5<BOARD_SIZE and j+5<BOARD_SIZE:
                                if nowBoard[i-1][j-1]!=myside and nowBoard[i+5][j+5]!=myside:
                                    isDd4bc = True
                        if isDd4bc:
                            newshape = [[i,j], "Dd4b/c", 3, ismyside]
                            shapes.append(newshape)
                            shapedict[str(i)+' '+str(j)].append("Dd4b/c")
                            if nowBoard[i+1][j+1] == myside:
                                shapedict[str(i+1)+' '+str(j+1)].append("Dd4b/c")
                            if nowBoard[i+2][j+2] == myside:
                                shapedict[str(i+2)+' '+str(j+2)].append("Dd4b/c")
                            if nowBoard[i+3][j+3] == myside:
                                shapedict[str(i+3)+' '+str(j+3)].append("Dd4b/c")
                            if nowBoard[i+4][j+4] == myside:
                                shapedict[str(i+4)+' '+str(j+4)].append("Dd4b/c")
                # Lv3 _ooo_
                # Lv3 horizontal
                if j>0 and j+3<BOARD_SIZE and nowBoard[i][j]==myside:
                    if nowBoard[i][j-1]==EMPTY and nowBoard[i][j+3]==EMPTY and nowBoard[i][j+1]==myside and nowBoard[i][j+2]==myside:
                        newshape = [[i,j], "Lv3", 0, ismyside]
                        shapedict[str(i)+' '+str(j)].append("Lv3")
                        shapedict[str(i)+' '+str(j+1)].append("Lv3")
                        shapedict[str(i)+' '+str(j+2)].append("Lv3")
                        shapes.append(newshape)
                # Lv3 vertical
                if i>0 and i+3<BOARD_SIZE and nowBoard[i][j]==myside:
                    if nowBoard[i-1][j]==EMPTY and nowBoard[i+3][j]==EMPTY and nowBoard[i+1][j]==myside and nowBoard[i+2][j]==myside:
                        newshape = [[i,j], "Lv3", 1, ismyside]
                        if ismyside:
                            shapedict[str(i)+' '+str(j)].append("Lv3")
                            shapedict[str(i+1)+' '+str(j)].append("Lv3")
                            shapedict[str(i+2)+' '+str(j)].append("Lv3")
                        shapes.append(newshape)
                # Lv3 upperright
                if i+1<BOARD_SIZE and j>0 and i>2 and j+3<BOARD_SIZE and nowBoard[i][j]==myside:
                    if nowBoard[i+1][j-1]==EMPTY and nowBoard[i-3][j+3]==EMPTY and nowBoard[i-1][j+1]==myside and nowBoard[i-2][j+2]==myside:
                        newshape = [[i,j], "Lv3", 2, ismyside]
                        if ismyside:
                            shapedict[str(i)+' '+str(j)].append("Lv3")
                            shapedict[str(i-1)+' '+str(j+1)].append("Lv3")
                            shapedict[str(i-2)+' '+str(j+2)].append("Lv3")
                        shapes.append(newshape)
                # Lv3 downright
                if i+3<BOARD_SIZE and j>0 and i>0 and j+3<BOARD_SIZE and nowBoard[i][j]==myside:
                    if nowBoard[i-1][j-1]==EMPTY and nowBoard[i+3][j+3]==EMPTY and nowBoard[i+1][j+1]==myside and nowBoard[i+2][j+2]==myside:
                        newshape = [[i,j], "Lv3", 3, ismyside]
                        if ismyside:
                            shapedict[str(i)+' '+str(j)].append("Lv3")
                            shapedict[str(i+1)+' '+str(j+1)].append("Lv3")
                            shapedict[str(i+2)+' '+str(j+2)].append("Lv3")
                        shapes.append(newshape)
                # Dd3a xooo__? / ?__ooox
                # Dd3a horizontal
                if j+4<BOARD_SIZE and nowBoard[i][j]==myside:
                    if nowBoard[i][j+1]==myside and nowBoard[i][j+2]==myside:
                        if j>0 and nowBoard[i][j+3]==EMPTY and nowBoard[i][j+4]==EMPTY:
                            if nowBoard[i][j-1]==opside:
                                newshape = [[i,j], "Dd3a0", 0, ismyside]
                                if ismyside:
                                    shapedict[str(i)+' '+str(j)].append("Dd3a0")
                                    shapedict[str(i)+' '+str(j+1)].append("Dd3a0")
                                    shapedict[str(i)+' '+str(j+2)].append("Dd3a0")
                                shapes.append(newshape)
                        if j==0 and nowBoard[i][j+3]==EMPTY and nowBoard[i][j+4]==EMPTY:
                            newshape = [[i,j], "Dd3a0", 0, ismyside]
                            if ismyside:
                                shapedict[str(i)+' '+str(j)].append("Dd3a0")
                                shapedict[str(i)+' '+str(j+1)].append("Dd3a0")
                                shapedict[str(i)+' '+str(j+2)].append("Dd3a0")
                            shapes.append(newshape)
                if j+4<BOARD_SIZE and nowBoard[i][j]==EMPTY:
                    if nowBoard[i][j+1]==EMPTY and nowBoard[i][j+2]==myside and nowBoard[i][j+3]==myside and nowBoard[i][j+4]==myside:
                        if j+5==BOARD_SIZE:
                            newshape = [[i,j+2], "Dd3a1", 0, ismyside]
                            if ismyside:
                                shapedict[str(i)+' '+str(j+2)].append("Dd3a1")
                                shapedict[str(i)+' '+str(j+3)].append("Dd3a1")
                                shapedict[str(i)+' '+str(j+4)].append("Dd3a1")
                            shapes.append(newshape)
                        if j+5<BOARD_SIZE:
                            if nowBoard[i][j+5]==opside:
                                newshape = [[i,j+2], "Dd3a1", 0, ismyside]
                                if ismyside:
                                    shapedict[str(i)+' '+str(j+2)].append("Dd3a1")
                                    shapedict[str(i)+' '+str(j+3)].append("Dd3a1")
                                    shapedict[str(i)+' '+str(j+4)].append("Dd3a1")
                                shapes.append(newshape)
                # Dd3a vertical
                if i+4<BOARD_SIZE and nowBoard[i][j]==myside and nowBoard[i+1][j]==myside and nowBoard[i+2][j]==myside:
                    if i>0 and nowBoard[i+3][j]==EMPTY and nowBoard[i+4][j]==EMPTY:
                        if nowBoard[i-1][j]==opside:
                            newshape = [[i,j], "Dd3a0", 1, ismyside]
                            if ismyside:
                                shapedict[str(i)+' '+str(j)].append("Dd3a0")
                                shapedict[str(i+1)+' '+str(j)].append("Dd3a0")
                                shapedict[str(i+2)+' '+str(j)].append("Dd3a0")
                            shapes.append(newshape)
                    if i==0 and nowBoard[i+3][j]==EMPTY and nowBoard[i+4][j]==EMPTY:
                        newshape = [[i,j], "Dd3a0", 1, ismyside]
                        if ismyside:
                            shapedict[str(i)+' '+str(j)].append("Dd3a0")
                            shapedict[str(i+1)+' '+str(j)].append("Dd3a0")
                            shapedict[str(i+2)+' '+str(j)].append("Dd3a0")
                        shapes.append(newshape)
                if i+4<BOARD_SIZE and nowBoard[i][j]==EMPTY:
                    if nowBoard[i+1][j]==EMPTY and nowBoard[i+2][j]==myside and nowBoard[i+3][j]==myside and nowBoard[i+4][j]==myside:
                        if j+5==BOARD_SIZE:
                            newshape = [[i+2,j], "Dd3a1", 1, ismyside]
                            if ismyside:
                                shapedict[str(i+2)+' '+str(j)].append("Dd3a1")
                                shapedict[str(i+3)+' '+str(j)].append("Dd3a1")
                                shapedict[str(i+4)+' '+str(j)].append("Dd3a1")
                            shapes.append(newshape)
                        if i+5<BOARD_SIZE:
                            if nowBoard[i+5][j]==opside:
                                newshape = [[i+2,j], "Dd3a1", 1, ismyside]
                                if ismyside:
                                    shapedict[str(i+2)+' '+str(j)].append("Dd3a1")
                                    shapedict[str(i+3)+' '+str(j)].append("Dd3a1")
                                    shapedict[str(i+4)+' '+str(j)].append("Dd3a1")
                                shapes.append(newshape)
                # Dd3a upperright
                if i-4>=0 and j+4<BOARD_SIZE and nowBoard[i][j]==myside:
                    if nowBoard[i-1][j+1]==myside and nowBoard[i-2][j+2]==myside and nowBoard[i-3][j+3]==EMPTY and nowBoard[i-4][j+4]==EMPTY:
                        if i+1<BOARD_SIZE and j-1>=0:
                            if nowBoard[i+1][j-1]==opside:
                                newshape = [[i,j], "Dd3a0", 2, ismyside]
                                if ismyside:
                                    shapedict[str(i)+' '+str(j)].append("Dd3a0")
                                    shapedict[str(i-1)+' '+str(j+1)].append("Dd3a0")
                                    shapedict[str(i-2)+' '+str(j+2)].append("Dd3a0")
                                shapes.append(newshape)
                        if j-1<0:
                            newshape = [[i,j], "Dd3a0", 2, ismyside]
                            if ismyside:
                                shapedict[str(i)+' '+str(j)].append("Dd3a0")
                                shapedict[str(i-1)+' '+str(j+1)].append("Dd3a0")
                                shapedict[str(i-2)+' '+str(j+2)].append("Dd3a0")
                            shapes.append(newshape)
                        if i+1==BOARD_SIZE:
                            newshape = [[i,j], "Dd3a0", 2, ismyside]
                            if ismyside:
                                shapedict[str(i)+' '+str(j)].append("Dd3a0")
                                shapedict[str(i-1)+' '+str(j+1)].append("Dd3a0")
                                shapedict[str(i-2)+' '+str(j+2)].append("Dd3a0")
                            shapes.append(newshape)
                if i-4>=0 and j+4<BOARD_SIZE and nowBoard[i][j]==EMPTY:
                    if nowBoard[i-1][j+1]==EMPTY and nowBoard[i-2][j+2]==myside and nowBoard[i-3][j+3]==myside and nowBoard[i-4][j+4]==myside:
                        if i-5>=0 and j+5<BOARD_SIZE:
                            if nowBoard[i-5][j+5]==opside:
                                newshape = [[i-2,j+2], "Dd3a1", 2, ismyside]
                                if ismyside:
                                    shapedict[str(i-2)+' '+str(j+2)].append("Dd3a1")
                                    shapedict[str(i-3)+' '+str(j+3)].append("Dd3a1")
                                    shapedict[str(i-4)+' '+str(j+4)].append("Dd3a1")
                                shapes.append(newshape)
                        if i-5<0 or j+5==BOARD_SIZE:
                            newshape = [[i-2,j+2], "Dd3a1", 2, ismyside]
                            if ismyside:
                                shapedict[str(i-2)+' '+str(j+2)].append("Dd3a1")
                                shapedict[str(i-3)+' '+str(j+3)].append("Dd3a1")
                                shapedict[str(i-4)+' '+str(j+4)].append("Dd3a1")
                            shapes.append(newshape)
                # Dd3a downright
                if i+4<BOARD_SIZE and j+4<BOARD_SIZE and nowBoard[i][j]==myside:
                    if nowBoard[i+1][j+1]==myside and nowBoard[i+2][j+2]==myside and nowBoard[i+3][j+3]==EMPTY and nowBoard[i+4][j+4]==EMPTY:
                        if i-1>=0 and j-1>=0:
                            if nowBoard[i-1][j-1]==opside:
                                newshape = [[i,j], "Dd3a0", 3, ismyside]
                                if ismyside:
                                    shapedict[str(i)+' '+str(j)].append("Dd3a0")
                                    shapedict[str(i+1)+' '+str(j+1)].append("Dd3a0")
                                    shapedict[str(i+2)+' '+str(j+2)].append("Dd3a0")
                                shapes.append(newshape)
                        if i-1<0 or j-1<0:
                            newshape = [[i,j], "Dd3a0", 3, ismyside]
                            if ismyside:
                                shapedict[str(i)+' '+str(j)].append("Dd3a0")
                                shapedict[str(i+1)+' '+str(j+1)].append("Dd3a0")
                                shapedict[str(i+2)+' '+str(j+2)].append("Dd3a0")
                            shapes.append(newshape)
                if i+4<BOARD_SIZE and j+4<BOARD_SIZE and nowBoard[i][j]==EMPTY:
                    if nowBoard[i+1][j+1]==EMPTY and nowBoard[i+2][j+2]==myside and nowBoard[i+3][j+3]==myside and nowBoard[i+4][j+4]==myside:
                        if i+5<BOARD_SIZE and j+5<BOARD_SIZE:
                            if nowBoard[i+5][j+5]==opside:
                                newshape = [[i+2,j+2], "Dd3a1", 3, ismyside]
                                if ismyside:
                                    shapedict[str(i+2)+' '+str(j+2)].append("Dd3a1")
                                    shapedict[str(i+3)+' '+str(j+3)].append("Dd3a1")
                                    shapedict[str(i+4)+' '+str(j+4)].append("Dd3a1")
                                shapes.append(newshape)
                        if i+5==BOARD_SIZE or j+5==BOARD_SIZE:
                            newshape = [[i+2,j+2], "Dd3a1", 3, ismyside]
                            if ismyside:
                                shapedict[str(i+2)+' '+str(j+2)].append("Dd3a1")
                                shapedict[str(i+3)+' '+str(j+3)].append("Dd3a1")
                                shapedict[str(i+4)+' '+str(j+4)].append("Dd3a1")
                            shapes.append(newshape)
                # Dd3b _o_oo_ / _oo_o_
                # Dd3b horizontal
                if nowBoard[i][j]==myside and j+3<BOARD_SIZE:
                    if (nowBoard[i][j+1]==myside and nowBoard[i][j+2]==EMPTY) or (nowBoard[i][j+1]==EMPTY and nowBoard[i][j+2]==myside) and nowBoard[i][j+3]==myside:
                        emptycnt = 0
                        isrepeat = False
                        if j-1>=0:
                            if nowBoard[i][j-1]==myside:
                                isrepeat = True
                            if nowBoard[i][j-1]==EMPTY:
                                emptycnt += 1
                        if j+4<BOARD_SIZE:
                            if nowBoard[i][j+4]==myside:
                                isrepeat = True
                            if nowBoard[i][j+4]==EMPTY:
                                emptycnt += 1
                        if emptycnt >= 1 and (not isrepeat):
                            newshape = [[i,j], "Dd3b", 0, ismyside]
                            if ismyside:
                                shapedict[str(i)+' '+str(j)].append("Dd3b")
                                if nowBoard[i][j+1] == myside:
                                    shapedict[str(i)+' '+str(j+1)].append("Dd3b")
                                if nowBoard[i][j+2] == myside:
                                    shapedict[str(i)+' '+str(j+2)].append("Dd3b")
                            shapes.append(newshape)
                # Dd3b vertical
                if nowBoard[i][j]==myside and i+3<BOARD_SIZE:
                    if (nowBoard[i+1][j]==myside and nowBoard[i+2][j]==EMPTY) or (nowBoard[i+1][j]==EMPTY and nowBoard[i+2][j]==myside) and nowBoard[i+3][j]==myside:
                        emptycnt = 0
                        isrepeat = False
                        if i-1>=0:
                            if nowBoard[i-1][j]==myside:
                                isrepeat = True
                            if nowBoard[i-1][j]==EMPTY:
                                emptycnt += 1
                        if i+4<BOARD_SIZE:
                            if nowBoard[i+4][j]==myside:
                                isrepeat = True
                            if nowBoard[i+4][j]==EMPTY:
                                emptycnt += 1
                        if emptycnt >= 1 and (not isrepeat):
                            newshape = [[i,j], "Dd3b", 1, ismyside]
                            if ismyside:
                                shapedict[str(i)+' '+str(j)].append("Dd3b")
                                if nowBoard[i+1][j] == myside:
                                    shapedict[str(i+1)+' '+str(j)].append("Dd3b")
                                if nowBoard[i+2][j] == myside:
                                    shapedict[str(i+2)+' '+str(j)].append("Dd3b")
                            shapes.append(newshape)
                # Dd3b upperright
                if nowBoard[i][j]==myside and i-3>=0 and j+3<BOARD_SIZE:
                    if (nowBoard[i-1][j+1]==myside and nowBoard[i-2][j+2]==EMPTY) or (nowBoard[i-1][j+1]==EMPTY and nowBoard[i-2][j+2]==myside) and nowBoard[i-3][j+3]==myside:
                        emptycnt = 0
                        isrepeat = False
                        if i+1<BOARD_SIZE and j-1>=0:
                            if nowBoard[i+1][j-1]==myside:
                                isrepeat = True
                            if nowBoard[i+1][j-1]==EMPTY:
                                emptycnt += 1
                        if i-4>=0 and j+4<BOARD_SIZE:
                            if nowBoard[i-4][j+4]==myside:
                                isrepeat = True
                            if nowBoard[i-4][j+4]==EMPTY:
                                emptycnt += 1
                        if emptycnt >= 1 and (not isrepeat):
                            newshape = [[i,j], "Dd3b", 2, ismyside]
                            if ismyside:
                                shapedict[str(i)+' '+str(j)].append("Dd3b")
                                if nowBoard[i-1][j+1] == myside:
                                    shapedict[str(i-1)+' '+str(j+1)].append("Dd3b")
                                if nowBoard[i-2][j+2] == myside:
                                    shapedict[str(i-2)+' '+str(j+2)].append("Dd3b")
                            shapes.append(newshape)
                # Dd3b downright
                if nowBoard[i][j]==myside and i+3<BOARD_SIZE and j+3<BOARD_SIZE:
                    print([i,j])
                    print(nowBoard[i+3][j+3])
                    print(myside)
                    if ((nowBoard[i+1][j+1]==myside and nowBoard[i+2][j+2]==EMPTY) or (nowBoard[i+1][j+1]==EMPTY and nowBoard[i+2][j+2]==myside)) and nowBoard[i+3][j+3]==myside:
                        emptycnt = 0
                        isrepeat = False
                        if i-1>=0 and j-1>=0:
                            if nowBoard[i-1][j-1]==myside:
                                isrepeat = True
                            if nowBoard[i-1][j-1]==EMPTY:
                                emptycnt += 1
                        if i+4<BOARD_SIZE and j+4<BOARD_SIZE:
                            if nowBoard[i+4][j+4]==myside:
                                isrepeat = True
                            if nowBoard[i+4][j+4]==EMPTY:
                                emptycnt += 1
                        if emptycnt >= 1 and (not isrepeat):
                            newshape = [[i,j], "Dd3b", 3, ismyside]
                            if ismyside:
                                shapedict[str(i)+' '+str(j)].append("Dd3b")
                                if nowBoard[i+1][j+1] == myside:
                                    shapedict[str(i+1)+' '+str(j+1)].append("Dd3b")
                                if nowBoard[i+2][j+2] == myside:
                                    shapedict[str(i+2)+' '+str(j+2)].append("Dd3b")
                            shapes.append(newshape)
                # Dd3cd xo__oox / xoo__ox / xo_o_ox
                # Dd3cd horizontal
                if nowBoard[i][j]==myside and j+4<BOARD_SIZE:
                    if nowBoard[i][j+4]==myside:
                        mycnt = 0
                        if nowBoard[i][j+1]==myside:
                            mycnt += 1
                        if nowBoard[i][j+2]==myside:
                            mycnt += 1
                        if nowBoard[i][j+3]==myside:
                            mycnt += 1
                        if mycnt == 1 and nowBoard[i][j+1]!=opside and nowBoard[i][j+2]!=opside and nowBoard[i][j+3]!=opside:
                            if j>0 and j+5==BOARD_SIZE:
                                if nowBoard[i][j-1]!=myside:
                                    newshape = [[i,j], "Dd3c/d", 0, ismyside]
                                    if ismyside:
                                        shapedict[str(i)+' '+str(j)].append("Dd3c/d")
                                        if nowBoard[i][j+1] == myside:
                                            shapedict[str(i)+' '+str(j+1)].append("Dd3c/d")
                                        if nowBoard[i][j+2] == myside:
                                            shapedict[str(i)+' '+str(j+2)].append("Dd3c/d")
                                        if nowBoard[i][j+3] == myside:
                                            shapedict[str(i)+' '+str(j+3)].append("Dd3c/d")
                                    shapes.append(newshape)
                            if j>0 and j+5<BOARD_SIZE:
                                if nowBoard[i][j-1]!=myside and nowBoard[i][j+5]!=myside:
                                    newshape = [[i,j], "Dd3c/d", 0, ismyside]
                                    if ismyside:
                                        shapedict[str(i)+' '+str(j)].append("Dd3c/d")
                                        if nowBoard[i][j+1] == myside:
                                            shapedict[str(i)+' '+str(j+1)].append("Dd3c/d")
                                        if nowBoard[i][j+2] == myside:
                                            shapedict[str(i)+' '+str(j+2)].append("Dd3c/d")
                                        if nowBoard[i][j+3] == myside:
                                            shapedict[str(i)+' '+str(j+3)].append("Dd3c/d")
                                    shapes.append(newshape)
                            if j==0 and j+5<BOARD_SIZE:
                                if nowBoard[i][j+5]!=myside:
                                    newshape = [[i,j], "Dd3c/d", 0, ismyside]
                                    if ismyside:
                                        shapedict[str(i)+' '+str(j)].append("Dd3c/d")
                                        if nowBoard[i][j+1] == myside:
                                            shapedict[str(i)+' '+str(j+1)].append("Dd3c/d")
                                        if nowBoard[i][j+2] == myside:
                                            shapedict[str(i)+' '+str(j+2)].append("Dd3c/d")
                                        if nowBoard[i][j+3] == myside:
                                            shapedict[str(i)+' '+str(j+3)].append("Dd3c/d")
                                    shapes.append(newshape)
                            if j==0 and j+5==BOARD_SIZE:
                                newshape = [[i,j], "Dd3c/d", 0, ismyside]
                                if ismyside:
                                    shapedict[str(i)+' '+str(j)].append("Dd3c/d")
                                    if nowBoard[i][j+1] == myside:
                                        shapedict[str(i)+str(j+1)].append("Dd3c/d")
                                    if nowBoard[i][j+2] == myside:
                                        shapedict[str(i)+' '+str(j+2)].append("Dd3c/d")
                                    if nowBoard[i][j+3] == myside:
                                        shapedict[str(i)+' '+str(j+3)].append("Dd3c/d")
                                shapes.append(newshape)
                # Dd3cd vertical
                if nowBoard[i][j]==myside and i+4<BOARD_SIZE:
                    if nowBoard[i+4][j]==myside:
                        mycnt = 0
                        if nowBoard[i+1][j]==myside:
                            mycnt += 1
                        if nowBoard[i+2][j]==myside:
                            mycnt += 1
                        if nowBoard[i+3][j]==myside:
                            mycnt += 1
                        if mycnt == 1 and nowBoard[i+1][j]!=opside and nowBoard[i+2][j]!=opside and nowBoard[i+3][j]!=opside:
                            if i>0 and i+5==BOARD_SIZE:
                                if nowBoard[i-1][j]!=myside:
                                    newshape = [[i,j], "Dd3c/d", 1, ismyside]
                                    if ismyside:
                                        shapedict[str(i)+' '+str(j)].append("Dd3c/d")
                                        if nowBoard[i+1][j] == myside:
                                            shapedict[str(i+1)+' '+str(j)].append("Dd3c/d")
                                        if nowBoard[i+2][j] == myside:
                                            shapedict[str(i+2)+' '+str(j)].append("Dd3c/d")
                                        if nowBoard[i+3][j] == myside:
                                            shapedict[str(i+3)+' '+str(j)].append("Dd3c/d")
                                    shapes.append(newshape)
                            if i>0 and i+5<BOARD_SIZE:
                                if nowBoard[i-1][j]!=myside and nowBoard[i+5][j]!=myside:
                                    newshape = [[i,j], "Dd3c/d", 1, ismyside]
                                    if ismyside:
                                        shapedict[str(i)+' '+str(j)].append("Dd3c/d")
                                        if nowBoard[i+1][j] == myside:
                                            shapedict[str(i+1)+' '+str(j)].append("Dd3c/d")
                                        if nowBoard[i+2][j] == myside:
                                            shapedict[str(i+2)+' '+str(j)].append("Dd3c/d")
                                        if nowBoard[i+3][j] == myside:
                                            shapedict[str(i+3)+' '+str(j)].append("Dd3c/d")
                                    shapes.append(newshape)
                            if i==0 and i+5==BOARD_SIZE:
                                newshape = [[i,j], "Dd3c/d", 1, ismyside]
                                if ismyside:
                                    shapedict[str(i)+' '+str(j)].append("Dd3c/d")
                                    if nowBoard[i+1][j] == myside:
                                        shapedict[str(i+1)+' '+str(j)].append("Dd3c/d")
                                    if nowBoard[i+2][j] == myside:
                                        shapedict[str(i+2)+' '+str(j)].append("Dd3c/d")
                                    if nowBoard[i+3][j] == myside:
                                        shapedict[str(i+3)+' '+str(j)].append("Dd3c/d")
                                shapes.append(newshape)
                # Dd3cd upperright
                if nowBoard[i][j]==myside and i-4>=0 and j+4<BOARD_SIZE:
                    if nowBoard[i-4][j+4]==myside:
                        mycnt = 0
                        if nowBoard[i-1][j+1]==myside:
                            mycnt += 1
                        if nowBoard[i-2][j+2]==myside:
                            mycnt += 1
                        if nowBoard[i-3][j+3]==myside:
                            mycnt += 1
                        if mycnt == 1 and nowBoard[i-1][j+1]!=opside and nowBoard[i-2][j+2]!=opside and nowBoard[i-3][j+3]!=opside:
                            if i+1==BOARD_SIZE or j==0:
                                if i-5>=0 and j+5<BOARD_SIZE:
                                    if nowBoard[i-5][j+5]!=myside:
                                        newshape = [[i,j], "Dd3c/d", 2, ismyside]
                                        if ismyside:
                                            shapedict[str(i)+' '+str(j)].append("Dd3c/d")
                                            if nowBoard[i-1][j+1] == myside:
                                                shapedict[str(i-1)+' '+str(j+1)].append("Dd3c/d")
                                            if nowBoard[i-2][j+2] == myside:
                                                shapedict[str(i-2)+' '+str(j+2)].append("Dd3c/d")
                                            if nowBoard[i-3][j+3] == myside:
                                                shapedict[str(i-3)+' '+str(j+3)].append("Dd3c/d")
                                        shapes.append(newshape)
                                if i-5<0 or j+5==BOARD_SIZE:
                                    newshape = [[i,j], "Dd3c/d", 2, ismyside]
                                    if ismyside:
                                        shapedict[str(i)+' '+str(j)].append("Dd3c/d")
                                        if nowBoard[i-1][j+1] == myside:
                                            shapedict[str(i-1)+' '+str(j+1)].append("Dd3c/d")
                                        if nowBoard[i-2][j+2] == myside:
                                            shapedict[str(i-2)+' '+str(j+2)].append("Dd3c/d")
                                        if nowBoard[i-3][j+3] == myside:
                                            shapedict[str(i-3)+' '+str(j+3)].append("Dd3c/d")
                                    shapes.append(newshape)
                            if i+1<BOARD_SIZE and j>0:
                                if nowBoard[i+1][j-1]!=myside:
                                    if i-5<0 or j+5==BOARD_SIZE:
                                        newshape = [[i,j], "Dd3c/d", 2, ismyside]
                                        if ismyside:
                                            shapedict[str(i)+' '+str(j)].append("Dd3c/d")
                                            if nowBoard[i-1][j+1] == myside:
                                                shapedict[str(i-1)+' '+str(j+1)].append("Dd3c/d")
                                            if nowBoard[i-2][j+2] == myside:
                                                shapedict[str(i-2)+' '+str(j+2)].append("Dd3c/d")
                                            if nowBoard[i-3][j+3] == myside:
                                                shapedict[str(i-3)+' '+str(j+3)].append("Dd3c/d")
                                        shapes.append(newshape)
                                    if i-5>=0 and j+5<BOARD_SIZE:
                                        if nowBoard[i-5][j+5]!=myside:
                                            newshape = [[i,j], "Dd3c/d", 2, ismyside]
                                            if ismyside:
                                                shapedict[str(i)+' '+str(j)].append("Dd3c/d")
                                                if nowBoard[i-1][j+1] == myside:
                                                    shapedict[str(i-1)+' '+str(j+1)].append("Dd3c/d")
                                                if nowBoard[i-2][j+2] == myside:
                                                    shapedict[str(i-2)+' '+str(j+2)].append("Dd3c/d")
                                                if nowBoard[i-3][j+3] == myside:
                                                    shapedict[str(i-3)+' '+str(j+3)].append("Dd3c/d")
                                            shapes.append(newshape)
                # Dd3cd downright
                if nowBoard[i][j]==myside and i+4<BOARD_SIZE and j+4<BOARD_SIZE:
                    if nowBoard[i+4][j+4]==myside:
                        mycnt = 0
                        if nowBoard[i+1][j+1]==myside:
                            mycnt += 1
                        if nowBoard[i+2][j+2]==myside:
                            mycnt += 1
                        if nowBoard[i+3][j+3]==myside:
                            mycnt += 1
                        if mycnt == 1 and nowBoard[i+1][j+1]!=opside and nowBoard[i+2][j+2]!=opside and nowBoard[i+3][j+3]!=opside:
                            if i==0 or j==0:
                                if i+5<BOARD_SIZE and j+5<BOARD_SIZE:
                                    if nowBoard[i+5][j+5]!=myside:
                                        newshape = [[i,j], "Dd3c/d", 3, ismyside]
                                        if ismyside:
                                            shapedict[str(i)+' '+str(j)].append("Dd3c/d")
                                            if nowBoard[i+1][j+1] == myside:
                                                shapedict[str(i+1)+' '+str(j+1)].append("Dd3c/d")
                                            if nowBoard[i+2][j+2] == myside:
                                                shapedict[str(i+2)+' '+str(j+2)].append("Dd3c/d")
                                            if nowBoard[i+3][j+3] == myside:
                                                shapedict[str(i+3)+' '+str(j+3)].append("Dd3c/d")
                                        shapes.append(newshape)
                                if i+5==BOARD_SIZE or j+5==BOARD_SIZE:
                                    newshape = [[i,j], "Dd3c/d", 3, ismyside]
                                    if ismyside:
                                        shapedict[str(i)+' '+str(j)].append("Dd3c/d")
                                        if nowBoard[i+1][j+1] == myside:
                                            shapedict[str(i+1)+' '+str(j+1)].append("Dd3c/d")
                                        if nowBoard[i+2][j+2] == myside:
                                            shapedict[str(i+2)+' '+str(j+2)].append("Dd3c/d")
                                        if nowBoard[i+3][j+3] == myside:
                                            shapedict[str(i+3)+' '+str(j+3)].append("Dd3c/d")
                                    shapes.append(newshape)
                            if i>0 and j>0:
                                if nowBoard[i-1][j-1]!=myside:
                                    if i+5<BOARD_SIZE and j+5<BOARD_SIZE:
                                        if nowBoard[i+5][j+5]!=myside:
                                            newshape = [[i,j], "Dd3c/d", 3, ismyside]
                                            if ismyside:
                                                shapedict[str(i)+' '+str(j)].append("Dd3c/d")
                                                if nowBoard[i+1][j+1] == myside:
                                                    shapedict[str(i+1)+' '+str(j+1)].append("Dd3c/d")
                                                if nowBoard[i+2][j+2] == myside:
                                                    shapedict[str(i+2)+' '+str(j+2)].append("Dd3c/d")
                                                if nowBoard[i+3][j+3] == myside:
                                                    shapedict[str(i+3)+' '+str(j+3)].append("Dd3c/d")
                                            shapes.append(newshape)
                                    if i+5==BOARD_SIZE or j+5==BOARD_SIZE:
                                        newshape = [[i,j], "Dd3c/d", 3, ismyside]
                                        if ismyside:
                                            shapedict[str(i)+' '+str(j)].append("Dd3c/d")
                                            if nowBoard[i+1][j+1] == myside:
                                                shapedict[str(i+1)+' '+str(j+1)].append("Dd3c/d")
                                            if nowBoard[i+2][j+2] == myside:
                                                shapedict[str(i+2)+' '+str(j+2)].append("Dd3c/d")
                                            if nowBoard[i+3][j+3] == myside:
                                                shapedict[str(i+3)+' '+str(j+3)].append("Dd3c/d")
                                        shapes.append(newshape)
                # Lv2, Dd2a ___oo___, xoo___ / ___oox
                # Lv2, Dd2a horizontal
                if nowBoard[i][j]==myside and j+1<BOARD_SIZE:
                    if nowBoard[i][j+1]==myside:
                        # Lv2
                        if j>0 and j+2<BOARD_SIZE:
                            if nowBoard[i][j-1]==EMPTY and nowBoard[i][j+2]==EMPTY:
                                if j+3<BOARD_SIZE:
                                    if nowBoard[i][j+3]==EMPTY:
                                        newshape = [[i,j], "Lv2", 0, ismyside]
                                        shapes.append(newshape)
                                if j-2>=0:
                                    if nowBoard[i][j-2]==EMPTY:
                                        newshape = [[i,j], "Lv2", 0, ismyside]
                                        shapes.append(newshape)
                        # Dd2a
                        isDd2a = False
                        if j==0 and j+4<BOARD_SIZE:
                            if nowBoard[i][j+2]==EMPTY and nowBoard[i][j+3]==EMPTY and nowBoard[i][j+4]==EMPTY:
                                isDd2a = True
                        if j+2==BOARD_SIZE and j-3>=0:
                            if nowBoard[i][j-1]==EMPTY and nowBoard[i][j-2]==EMPTY and nowBoard[i][j-3]==EMPTY:
                                isDd2a = True
                        if j>0 and j+4<BOARD_SIZE:
                            if nowBoard[i][j-1]==opside and nowBoard[i][j+2]==EMPTY and nowBoard[i][j+3]==EMPTY and nowBoard[i][j+4]==EMPTY:
                                isDd2a = True
                        if j+2<BOARD_SIZE and j-3>=0:
                            if nowBoard[i][j+2]==opside and nowBoard[i][j-1]==EMPTY and nowBoard[i][j-2]==EMPTY and nowBoard[i][j-3]==EMPTY:
                                isDd2a = True
                        if isDd2a:
                            newshape = [[i,j], "Dd2a", 0, ismyside]
                            shapes.append(newshape)
                # Lv2, Dd2a vertical
                if nowBoard[i][j]==myside and i+1<BOARD_SIZE:
                    if nowBoard[i+1][j]==myside:
                        # Lv2
                        if i>0 and i+2<BOARD_SIZE:
                            if nowBoard[i-1][j]==EMPTY and nowBoard[i+2][j]==EMPTY:
                                if i+3<BOARD_SIZE:
                                    if nowBoard[i+3][j]==EMPTY:
                                        newshape = [[i,j], "Lv2", 1, ismyside]
                                        shapes.append(newshape)
                                if i-2>=0:
                                    if nowBoard[i-2][j]==EMPTY:
                                        newshape = [[i,j], "Lv2", 1, ismyside]
                                        shapes.append(newshape)
                        # Dd2a
                        isDd2a = False
                        if i==0 and i+4<BOARD_SIZE:
                            if nowBoard[i+2][j]==EMPTY and nowBoard[i+3][j]==EMPTY and nowBoard[i+4][j]==EMPTY:
                                isDd2a = True
                        if i+2==BOARD_SIZE and i-3>=0:
                            if nowBoard[i-1][j]==EMPTY and nowBoard[i-2][j]==EMPTY and nowBoard[i-3][j]==EMPTY:
                                isDd2a = True
                        if i>0 and i+4<BOARD_SIZE:
                            if nowBoard[i-1][j]==opside and nowBoard[i+2][j]==EMPTY and nowBoard[i+3][j]==EMPTY and nowBoard[i+4][j]==EMPTY:
                                isDd2a = True
                        if i+2<BOARD_SIZE and i-3>=0:
                            if nowBoard[i+2][j]==opside and nowBoard[i-1][j]==EMPTY and nowBoard[i-2][j]==EMPTY and nowBoard[i-3][j]==EMPTY:
                                isDd2a = True
                        if isDd2a:
                            newshape = [[i,j], "Dd2a", 1, ismyside]
                            shapes.append(newshape)
                # Lv2, Dd2a upperright
                if nowBoard[i][j]==myside and i-1>=0 and j+1<BOARD_SIZE:
                    if nowBoard[i-1][j+1]==myside:
                        # Lv2
                        if i+1<BOARD_SIZE and j-1>=0 and i-2>=0 and j+2<BOARD_SIZE:
                            if nowBoard[i+1][j-1]==EMPTY and nowBoard[i-2][j+2]==EMPTY:
                                if i-3>=0 and j+3<BOARD_SIZE:
                                    if nowBoard[i-3][j+3]==EMPTY:
                                        newshape = [[i,j], "Lv2", 2, ismyside]
                                        shapes.append(newshape)
                                if i+2<BOARD_SIZE and j-2>=0:
                                    if nowBoard[i+2][j-2]==EMPTY:
                                        newshape = [[i,j], "Lv2", 2, ismyside]
                                        shapes.append(newshape)
                        # Dd2a
                        isDd2a = False
                        if (i+1==BOARD_SIZE or j==0) and i-4>=0 and j+4<BOARD_SIZE:
                            if nowBoard[i-2][j+2]==EMPTY and nowBoard[i-3][j+3]==EMPTY and nowBoard[i-4][j+4]==EMPTY:
                                isDd2a = True
                        if (i==0 or j+1==BOARD_SIZE) and i+3<BOARD_SIZE and j-3>=0:
                            if nowBoard[i+1][j-1]==EMPTY and nowBoard[i+2][j-2]==EMPTY and nowBoard[i+3][j-3]==EMPTY:
                                isDd2a = True
                        if (i+1<BOARD_SIZE and j-1>=0) and i-4>=0 and j+4<BOARD_SIZE:
                            if nowBoard[i+1][j-1]==opside and nowBoard[i-2][j+2]==EMPTY and nowBoard[i-3][j+3]==EMPTY and nowBoard[i-4][j+4]==EMPTY:
                                isDd2a = True
                        if (i-1>=0 and j+1<BOARD_SIZE) and i+3<BOARD_SIZE and j-3>=0:
                            if nowBoard[i-2][i+2]==opside and nowBoard[i+1][j-1]==EMPTY and nowBoard[i+2][j-2]==EMPTY and nowBoard[i+3][j-3]==EMPTY:
                                isDd2a = True
                        if isDd2a:
                            newshape = [[i,j], "Dd2a", 2, ismyside]
                            shapes.append(newshape)
                # Lv2, Dd2a downright
                if nowBoard[i][j]==myside and i+1<BOARD_SIZE and j+1<BOARD_SIZE:
                    if nowBoard[i+1][j+1]==myside:
                        # Lv2
                        if i-1>=0 and j-1>=0 and i+2<BOARD_SIZE and j+2<BOARD_SIZE:
                            if nowBoard[i-1][j-1]==EMPTY and nowBoard[i+2][j+2]==EMPTY:
                                if i+3<BOARD_SIZE and j+3<BOARD_SIZE:
                                    if nowBoard[i+3][j+3]==EMPTY:
                                        newshape = [[i,j], "Lv2", 3, ismyside]
                                        shapes.append(newshape)
                                if i-2>=0 and j-2>=0:
                                    if nowBoard[i-2][j-2]==EMPTY:
                                        newshape = [[i,j], "Lv2", 3, ismyside]
                                        shapes.append(newshape)
                        # Dd2a
                        isDd2a = False
                        if (i==0 or j==0) and i+4<BOARD_SIZE and j+4<BOARD_SIZE:
                            if nowBoard[i+2][j+2]==EMPTY and nowBoard[i+3][j+3]==EMPTY and nowBoard[i+4][j+4]==EMPTY:
                                isDd2a = True
                        if (i+2==BOARD_SIZE or j+2==BOARD_SIZE) and i-3>=0 and j-3>=0 :
                            if nowBoard[i-1][j-1]==EMPTY and nowBoard[i-2][j-2]==EMPTY and nowBoard[i-3][j-3]==EMPTY:
                                isDd2a = True
                        if (i-1>=0 and j-1>=0) and i+4<BOARD_SIZE and j+4<BOARD_SIZE:
                            if nowBoard[i-1][j-1]==opside and nowBoard[i+2][j+2]==EMPTY and nowBoard[i+3][j+3]==EMPTY and nowBoard[i+4][j+4]==EMPTY:
                                isDd2a = True
                        if (i+2<BOARD_SIZE and j+2<BOARD_SIZE) and i-3>=0 and j-3>=0:
                            if nowBoard[i+2][j+2]==opside and nowBoard[i-1][j-2]==EMPTY and nowBoard[i-2][j-2]==EMPTY and nowBoard[i-3][j-3]==EMPTY:
                                isDd2a = True
                        if isDd2a:
                            newshape = [[i,j], "Dd2a", 3, ismyside]
                            shapes.append(newshape)
        myside = OTHER
        opside = ME
        ismyside = False
        eval_value = 0
    # print(shapes)
    # for i in range(BOARD_SIZE):
        # print(nowBoard[i])
    for s in shapes:
        if s[3]:
            if maxdepth == 1:
                eval_value += myvalue_1[s[1]]
            else:
                eval_value += myvalue[s[1]]
        elif not s[3]:
            if maxdepth == 1:
                eval_value -= opvalue_1[s[1]]
            else:
                eval_value -= opvalue[s[1]]
    isForbbiden = False
    for r in range(BOARD_SIZE):
        for c in range(BOARD_SIZE):
            if len(shapedict[str(r)+' '+str(c)]) > 1:
                isForbbiden = True
    if isForbbiden:
        eval_value = -10000000000
    print(shapes)
    return eval_value



def addChildren(node, depth, maxdepth, maxPlayer):
    if depth is 0 or node is None:
        # if node.parent.move[0] == 1:
        node.value = eval(node, maxdepth)
        return node
    # print(emptyPos)
    emptyBoard = np.zeros((BOARD_SIZE, BOARD_SIZE))
    emptyPos = coord[(emptyBoard == node.board)]
    for pos in emptyPos:
        # print(depth)
        # print(pos)
        newNode = Node()
        newNode.move = pos
        nowBoard = np.array(node.board)
        nowBoard[pos[0]][pos[1]] = 2 - maxPlayer
        newNode.board = nowBoard
        newNode.Childof(node)
        if maxPlayer:
            addChildren(newNode, depth - 1, maxdepth, False)
        else:
            addChildren(newNode, depth - 1, maxdepth, True)
    return node

def alphabeta(node, depth, alpha, beta, maxPlayer):
    if depth is 0 or len(node.children) is 0:
        return node.value
    if maxPlayer:
        v = -100000000
        for child in node.children:
            v = max(v, alphabeta(child, depth - 1, alpha, beta, False))
            node.value = v
            alpha = max(alpha, v)
            if alpha >= beta:
                break
        return v
    else:
        v = 100000000
        for child in node.children:
            v = min(v, alphabeta(child, depth - 1, alpha, beta, True))
            node.value = v
            beta = min(beta, v)
            if alpha >= beta:
                break
        return v

def decision(node):
    emptyBoard = np.zeros((BOARD_SIZE, BOARD_SIZE))
    emptyPos = coord[(emptyBoard == node.board)]
    depth = 1
    if len(emptyPos) <= 60:
        depth = 2
    if len(emptyPos) <= 35:
        depth = 3
    node = addChildren(node, depth, depth, True)
    alphabeta(node, depth, -1000000000, 1000000000, True)
    maxmovevalue = max([i.value for i in node.children])
    for child in node.children:
        if child.value == maxmovevalue:
            maxmove = child.move
    print(depth)
    return maxmove

# node1 = Node()
# node2 = Node()
# node2.Childof(node1)
# node3 = Node()
# node3.Childof(node1)
# node4 = Node()
# node4.Childof(node1)
# node5 = Node(5)
# node5.Childof(node2)
# node6 = Node(3)
# node6.Childof(node2)
# node7 = Node(1)
# node7.Childof(node3)
# node8 = Node(7)
# node8.Childof(node3)
# node9 = Node(5)
# node9.Childof(node4)
# node10 = Node(8)
# node10.Childof(node4)
# node11 = Node(2)
# node11.Childof(node4)
# print(alphabeta(node1, 2, -100000000, 100000000, True))

# testboard = np.zeros((BOARD_SIZE, BOARD_SIZE))
# testboard.fill(1)
# for i in range(3):
#     for j in range(2):
#         testboard[i][j] = 0
# testnode = Node()
# testnode.board = testboard
# testnode = addChildren(testnode, 2, True)
# testnode.Printout()
# alphabeta(testnode, 2, -100000000, 100000000, True)
# testnode.Printout()
nowBoard = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,1,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,1,0,1,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,1,0,1,0,0,0,0,0,0],
            [0,0,0,0,0,1,1,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],]

testnode = Node()
# testnode.board = testboard
testnode.board = nowBoard
print(eval(testnode, 1))
# testnode.board = emptyBoard
# eval(testnode)
# print("Best move:" + str(decision(testnode)))
