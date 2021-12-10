import sys
sys.path.append('C:/Users/cobou/Documents/Python/adventOfCodeMisc/library')
from AoCLibrary import *

a = AdventInput("input10.txt")
inp = a.data


p1_scores = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

p2_scores = {
    ")": 1, 
    "]": 2,
    "}": 3,
    ">": 4 
}
comp = {
    "{":"}",
    "(":")",
    "<":">",
    "[":"]"
}

p1 = 0
scores = []
for line in a.lines:
    stack = []
    closing = "})>]"
    comp |= rev_dict(comp)
    bad = False
    for c in line:
        if c in closing and stack[-1] != comp[c]:
            p1 += p1_scores[c]
            bad = True
            break
        if c in closing:
            if stack[-1] == comp[c]:
                stack.pop()
            else:
                bad = True
                break
        else:
            stack.append(c)

    if not bad:
        x = 0
        while stack:
            cur = stack.pop()
            x *= 5
            x += p2_scores[comp[cur]]
        scores.append(x)
ans(p1)
scores.sort()
ans(scores[len(scores)//2])
