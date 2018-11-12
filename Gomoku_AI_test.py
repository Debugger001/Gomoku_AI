import numpy as np
from wuzi import *
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


value = {
"lv4": 10000,
"Dd4a": 500,
"Dd4b/c": 500,
}



coord = []
for i in range(BOARD_SIZE):
    temp = []
    for j in range(BOARD_SIZE):
        temp.append([i,j])
    coord.append(temp)
coord = np.array(coord)

def eval(node):
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
    for i in range(2):
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                # Lv4, Dd4a _oooo_, _oooox / xoooo_
                # Lv4, Dd4a horizontal
                if j+3 < BOARD_SIZE and nowBoard[i][j] == myside:
                    MEcounter = 0
                    for n in range(3):
                        if nowBoard[i][j+n+1] == myside:
                            MEcounter += 1
                        else:
                            break
                    if MEcounter == 3 and j>0 and nowBoard[i][j-1] == EMPTY and j+4<BOARD_SIZE and nowBoard[i][j+4] == EMPTY:
                        newshape = [[i, j], "Lv4", 0, ismyside]
                        shapes.append(newshape)
                    if MEcounter == 3:
                        isDb4a = False
                        if j>0 and nowBoard[i][j-1] == EMPTY and ((j+4<BOARD_SIZE and nowBoard[i][j+4]==opside) or (j+4==BOARD_SIZE)):
                            isDb4a = True
                        if j+4<BOARD_SIZE and nowBoard[i][j+4] == EMPTY and ((j>0 and nowBoard[i][j-1]==opside) or (j==0)):
                            isDb4a = True
                        if isDb4a:
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
                    if MEcounter == 3 and i>0 and nowBoard[i-1][j] == EMPTY and i+4<BOARD_SIZE and nowBoard[i+4][j] == EMPTY:
                        newshape = [[i, j], "Lv4", 1, ismyside]
                        shapes.append(newshape)
                    if MEcounter == 3:
                        isDb4a = False
                        if i>0 and nowBoard[i-1][j] == EMPTY and ((i+4<BOARD_SIZE and nowBoard[i+4][j]==opside) or (i+4==BOARD_SIZE)):
                            isDb4a = True
                        if i+4<BOARD_SIZE and nowBoard[i+4][j] == EMPTY and ((i>0 and nowBoard[i-1][j]==opside) or (i==0)):
                            isDb4a = True
                        if isDb4a:
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
                    if MEcounter == 3 and i+1<BOARD_SIZE and j>0 and nowBoard[i+1][j-1] == EMPTY and i>3 and j+4<BOARD_SIZE and nowBoard[i-4][j+4] == EMPTY:
                        newshape = [[i, j], "Lv4", 2, ismyside]
                        shapes.append(newshape)
                    if MEcounter == 3:
                        isDb4a = False
                        if (i+1==BOARD_SIZE or j==0) and (i==3 or j+4==BOARD_SIZE or (i>3 and j+4<BOARD_SIZE and nowBoard[i-4][j+4]!=myside)):
                            isDb4a = True
                        if (i==3 or j+4==BOARD_SIZE) and (i+1<BOARD_SIZE and j>0 and nowBoard[i+1][j-1]!=myside):
                            isDb4a = True
                        if (i+1<BOARD_SIZE and j>0 and i>3 and j+4<BOARD_SIZE) and ((nowBoard[i+1][j-1]==opside and nowBoard[i-4][j+4]==EMPTY) or (nowBoard[i+1][j-1]==EMPTY and nowBoard[i-4][j+4]==opside)):
                            isDb4a = True
                        if isDb4a:
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
                        isDb4a = False
                        if (i==0 or j==0) and (i+4==BOARD_SIZE or j+4==BOARD_SIZE or (i+4<BOARD_SIZE and j+4<BOARD_SIZE and nowBoard[i+4][j+4]!=myside)):
                            isDb4a = True
                        if (i+4==BOARD_SIZE or j+4==BOARD_SIZE) and (i>0 and j>0 and nowBoard[i-1][j-1]!=myside):
                            isDb4a = True
                        if i>0 and j>0 and i+4<BOARD_SIZE and j+4<BOARD_SIZE and ((nowBoard[i-1][j-1]==opside and nowBoard[i+4][j+4]==EMPTY) or (nowBoard[i-1][j-1]==EMPTY and nowBoard[i+4][j+4]==opside)):
                            isDb4a = True
                        if isDb4a:
                            newshape = [[i, j], "Dd4a", 3, ismyside]
                            shapes.append(newshape)
                # Dd4b,c ?ooo_ox / xooo_o? , xoo_oo? / ?oo_oox
                # Dd4b,c horizontal
                if j+4<BOARD_SIZE and nowBoard[i][j] == myside and nowBoard[i][j+4] == myside:
                    MEcounter = 0
                    for n in range(3):
                        if nowBoard[i][j+n+1] == myside:
                            MEcounter += 1
                        elif nowBoard[i][j+n+1] == EMPTY:
                            continue
                        else:
                            MEcounter = 0
                            break
                    isDb4bc = False
                    if MEcounter == 2:
                        if (j==0 and nowBoard[i][j+5]!=myside) or (j+5==BOARD_SIZE and nowBoard[i][j-1]!=myside):
                            isDb4bc = True
                        if (j>0 and j+5<BOARD_SIZE and ((nowBoard[i][j-1]==opside and nowBoard[i][j+5]!=myside) or (nowBoard[i][j-1]!=myside and nowBoard[i][j+5]==opside))):
                            isDb4bc = True
                    if isDb4bc:
                        newshape = [[i,j], "Db4b/c", 0, ismyside]
                        shapes.append(newshape)
                # Dd4b,c vertical
                if i+4<BOARD_SIZE and nowBoard[i][j] == myside and nowBoard[i+4][j] == myside:
                    MEcounter = 0
                    for n in range(3):
                        if nowBoard[i+n+1][j] == myside:
                            MEcounter += 1
                        elif nowBoard[i+n+1][j] == EMPTY:
                            continue
                        else:
                            MEcounter = 0
                            break
                    isDb4bc = False
                    if MEcounter == 2:
                        if (i==0 and nowBoard[i+5][j]==opside) or (i+5==BOARD_SIZE and nowBoard[i-1][j]==opside):
                            isDb4bc = True
                        if (i>0 and i+5<BOARD_SIZE and ((nowBoard[i-1][j]==opside and nowBoard[i+5][j]!=myside) or (nowBoard[i-1][j]!=myside and nowBoard[i+5][j]==opside))):
                            isDb4bc = True
                    if isDb4bc:
                        newshape = [[i,j], "Db4b/c", 1, ismyside]
                        shapes.append(newshape)
                # Dd4b,c upperright
                if i-4>=0 and j+4<BOARD_SIZE and nowBoard[i][j] == myside and nowBoard[i-4][j+4] == myside:
                    MEcounter = 0
                    for n in range(3):
                        if nowBoard[i-n-1][j+n+1] == myside:
                            MEcounter += 1
                        elif nowBoard[i-n-1][j+n+1] == EMPTY:
                            continue
                        else:
                            MEcounter = 0
                            break
                    isDb4bc = False
                    if MEcounter == 2:
                        if (i+1==BOARD_SIZE or j==0) and (i==4 or j+5==BOARD_SIZE or (i>4 and j+5<BOARD_SIZE and nowBoard[i-5][j+5]!=myside)):
                            isDb4bc = True
                        if (i==4 or j+5==BOARD_SIZE) and (i+1<BOARD_SIZE and j>0 and nowBoard[i+1][j-1]!=myside):
                            isDb4bc = True
                        if (i+1<BOARD_SIZE and j>0 and i>4 and j+5<BOARD_SIZE) and ((nowBoard[i+1][j-1]==opside and nowBoard[i-5][j+5]!=myside) or (nowBoard[i+1][j-1]!=myside and nowBoard[i-5][j+5]==opside)):
                            isDb4bc = True
                    if isDb4bc:
                        newshape = [[i,j], "Db4b/c", 2, ismyside]
                        shapes.append(newshape)
                # Dd4b,c downright
                if i+4<BOARD_SIZE and j+4<BOARD_SIZE and nowBoard[i][j] == myside and nowBoard[i+4][j+4] == myside:
                    MEcounter = 0
                    for n in range(3):
                        if nowBoard[i+n+1][j+n+1] == myside:
                            MEcounter += 1
                        elif nowBoard[i+n+1][j+n+1] == EMPTY:
                            continue
                        else:
                            MEcounter = 0
                            break
                    isDb4bc = False
                    if MEcounter == 2:
                        if ((i==0 or j==0) and j+5<BOARD_SIZE and nowBoard[i-5][j+5]==opside) or ((i-4==0 or j+5==BOARD_SIZE) and i+1<BOARD_SIZE and j-1>=0 and nowBoard[i+1][j-1]==opside):
                            isDb4bc = True
                        if i+1<BOARD_SIZE and j>0 and i>4 and j+5<BOARD_SIZE and ((nowBoard[i+1][j-1]==opside and nowBoard[i-5][j+5]!=myside) or (nowBoard[i+1][j-1]!=myside and nowBoard[i-5][j+5]==opside)):
                            isDb4bc = True
                    if isDb4bc:
                        newshape = [[i,j], "Db4b/c", 2, ismyside]
                        shapes.append(newshape)


        myside = OTHER
        opside = ME
        ismyside = False
        eval_value = 0
        for s in shapes:
            if s[3]:
                eval_value += value[s[1]]
            elif not s[3]:
                eval_value -= value[s[1]]
        return eval_value




























def addChildren(node, depth, maxPlayer):
    if depth is 0 or node is None:
        # if node.parent.move[0] == 1:
        node.value = eval(node)
        return node
    emptyBoard = np.zeros((BOARD_SIZE, BOARD_SIZE))
    emptyPos = coord[(emptyBoard == node.board)]
    # print(emptyPos)
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
            addChildren(newNode, depth - 1, False)
        else:
            addChildren(newNode, depth - 1, True)
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

testboard = np.zeros((BOARD_SIZE, BOARD_SIZE))
testboard.fill(1)
for i in range(3):
    for j in range(2):
        testboard[i][j] = 0
testnode = Node()
testnode.board = testboard
testnode = addChildren(testnode, 2, True)
testnode.Printout()
alphabeta(testnode, 2, -100000000, 100000000, True)
testnode.Printout()
