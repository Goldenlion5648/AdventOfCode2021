import sys
sys.path.append('C:/Users/cobou/Documents/Python/adventOfCodeMisc/library')
from AoCLibrary import *

a = AdventInput("input4.txt")
inp = a.data

b = '''99,56,7,15,81,26,75,40,87,59,62,24,58,34,78,86,44,65,18,94,20,17,98,29,57,92,14,32,46,79,85,84,35,68,55,22,41,61,90,11,69,96,23,47,43,80,72,50,97,33,53,25,28,51,49,64,12,63,21,48,27,19,67,88,66,45,3,71,16,70,76,13,60,77,73,1,8,10,52,38,36,74,83,2,37,6,31,91,89,54,42,30,5,82,9,95,93,4,0,39'''
# b = '''7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1'''
def scan(z, said):
    for y in range(5):
        if all(x in said for x in z[y]):
            return True
    for j in range(5):
        if all(z[i][j] in said for i in range(5)):
            return True
    return False


boards = list(chunked(list(chunked(nums(a.data), 5)), 5))

said = set()
marked = set()
p1 = 0
for n in nums(b):
    # print(n)
    said.add(n)
    for w, board in enu(boards):
        if scan(board, said):
            if len(marked) == 0:
                ans(sum(set(flatten(board)) - said) * n)
            marked.add(w)
        temp = len(boards) - len(marked) 
        if temp == 0:
            temp = sum(set(flatten(board)) - said)
            ans(temp * n, True)

