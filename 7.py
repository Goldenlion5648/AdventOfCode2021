import sys
sys.path.append('C:/Users/cobou/Documents/Python/adventOfCodeMisc/library')
from AoCLibrary import *

a = AdventInput("input7.txt")
inp = a.data

x = nums(inp)
print(max(x))
def z(c):
    return c * (c+1) // 2
p1 = inf
p2 = inf
for i in range(max(x)):
    p1 = min(p1, sum(abs(x[j]-i) for j in range(len(x))))
    p2 = min(p2, sum(z(abs(x[j]-i)) for j in range(len(x))))
ans(p1)
ans(p2)