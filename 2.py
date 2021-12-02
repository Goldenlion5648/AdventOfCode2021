import sys
sys.path.append('C:/Users/cobou/Documents/Python/adventOfCodeMisc/library')
from AoCLibrary import *

a = AdventInput("input2.txt")
inp = a.data


x = 0
y = 0
for line in a.lines:
    n = nums(line)[0]
    if "forward" in line:
        x += n
    elif "down" in line:
        y += n
    elif "up" in line:
        y -= n
ans(y * x)
x = 0
y = 0
aim = 0
for line in a.lines:
    n = nums(line)[0]
    if "forward" in line:
        x += n
        y += n * aim
    elif "down" in line:
        aim += n
    elif "up" in line:
        aim -= n
ans(y * x)