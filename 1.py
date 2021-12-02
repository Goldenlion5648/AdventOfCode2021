import sys
sys.path.append('C:/Users/cobou/Documents/Python/adventOfCodeMisc/library')
from AoCLibrary import *

a = AdventInput("input1.txt")
inp = a.data

t = 0
x = nums(inp)
for i in range(len(x) - 1):
    if x[i+1] > x[i]:
        t += 1
ans(t)

z = 0
prev = sum(x[:3])
for i in range(1, len(x)):
    if sum(x[i:i+3]) > prev:
        z += 1
    prev = sum(x[i:i+3])
ans(z)


