import sys
sys.path.append('C:/Users/cobou/Documents/Python/adventOfCodeMisc/library')
from AoCLibrary import *

a = AdventInput("input13.txt")
inp = a.data
#gets adjusted later
size = 2000 
def foldX(board, foldx):
    for y in range(size):
        for x in range(size):
            if x < foldx and board[x, y] != "#":
                board[x, y] = board[foldx + (foldx -x), y]
            if x >= foldx:
                board[x, y] = '.'
        # else:
def foldY(board, foldy):
    for y in range(size):
        for x in range(size):
            if y < foldy and board[x, y] != "#":
                board[x, y] = board[(x), foldy +(foldy - y)]
            if y > foldy:
                board[x, y] = '.'

def draw2(board):
    for y in range(20):
        for x in range(50):
            print(board[x, y], end='')
        print()
board = dd(lambda :".")
for line in a.lines:
    if "fold" in line:
        print("folding")
        size = max(max(board.keys(), key=lambda x: max(x)))
        if "x" in line:
            foldX(board, num(line))
        if "y" in line:
            foldY(board, num(line))
    elif line:
        x, y = nums(line)
        board[x, y] = "#"

draw2(board)