import sys
sys.path.append('C:/Users/cobou/Documents/Python/adventOfCodeMisc/library')
from AoCLibrary import *

a = AdventInput("input15.txt")

inp = a.data


goal = (len(a.lines)-1, len(a.lines[0])-1)


def tile_input(inp):
    start = (inp).strip().splitlines()
    mult1 = [z * 5 for z in start]
    inp = ("\n".join(mult1)+ "\n") * 5 
    inp = inp.strip()
    return inp

def get_board(inp, p2=False):
    size = len(inp.splitlines()) // 5
    board = grid(inp, True)
    for j in board:
        board[j] = int(board[j])

    if not p2:
        return board
    big = {}
    for y, x in board:
        temp = board[y, x] + (y//size) + (x//size)
        if temp >= 10:
            temp = (temp + 1) % 10
        big[y, x] =temp
    board = deepcopy(big)

    return board

# def dijkstra(board, startY, startX, goalY, goalX):
#     goal = (goalY, goalX)
#     # print(goal)
#     fringe = ([(0, (startY, startX))])
#     heapq.heapify(fringe)
#     seen  =dd(lambda : inf)
#     while fringe:
#         steps, (y, x) = heapq.heappop(fringe)
#         if seen[y, x] <= steps:
#             continue
#         seen[y, x] = min(seen[y, x], steps)
#         if (y, x) == goal:
#             # print("stopped")
#             return (steps)
#         for dy, dx in adj:
#             n = (dy+y, dx +x)
#             if n in board:
#                 heapq.heappush(fringe, (board[n] + steps, n))

    # ans(seen[goal])
board = get_board(inp)
ans(dijkstra(board, 0,0,*list(board.keys())[-1]))
board = get_board(tile_input(inp), True)
ans(dijkstra(board, 0,0,*list(board.keys())[-1]))