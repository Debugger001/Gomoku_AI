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



coord = []
for i in range(BOARD_SIZE):
    temp = []
    for j in range(BOARD_SIZE):
        temp.append([i,j])
    coord.append(temp)
coord = np.array(coord)

def eval(node):
    nowBoard = node.board
    shapes = []

    # for i in range(BOARD_SIZE):
        # for j in range(BOARD_SIZE):

    # Lv4 _oooo_
    # Dd4 _oooox, _ooo_ox, xoo_oox
    # Lv3 __ooo__
    # Dd3 xooo__, _o_oo_, xo__oox, xo_o_ox
    # Lv2 ___oo___, xoo___, __o_o__, _o__o_

    # Direction: 0: horizontal, 1: vertical, 2: upperright, 3: downright

    # Shapes are stored in format: [eigencoord, type, direction]

    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            # Lv4 horizontal
            if (nowBoard[i][j] == EMPTY and j+5 < BOARD_SIZE):
                for n in range(4):
                    if (nowBoard[i][j+n+1] == ME):
                        continue
                    else:
                        break
                if (n == 3 and nowBoard[i][j+5] == EMPTY):
                    newshape = [[i, j+1], "Lv4", 0]
                    shapes.append(newshape)
            # Lv4 vertical
            if (nowBoard[i][j] == EMPTY and i+5 < BOARD_SIZE):
                for n in range(4):
                    if (nowBoard[i+n+1][j] == ME):
                        continue
                    else:
                        break
                if (n == 3 and nowBoard[i][j+5] == EMPTY):
                    newshape = [[i+1, j], "Lv4", 1]
                    shapes.append(newshape)


























def addChildren(node, depth, maxPlayer):
    if depth is 0 or node is None:
        if node.parent.move[0] == 1:
            node.value = 2
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
testnode = addChildren(testnode, 4, True)
testnode.Printout()
alphabeta(testnode, 4, -100000000, 100000000, True)
testnode.Printout()
