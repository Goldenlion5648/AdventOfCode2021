import sys
sys.path.append('C:/Users/cobou/Documents/Python/adventOfCodeMisc/library')
from AoCLibrary import *

a = AdventInput("input3.txt")
inp = a.data


w = {}
z = {}
for i in range(len(a.lines[0])):
    w[i], z[i] = (x[0] for x in Counter(line[i] for line in a.lines).most_common(2))
    # p(Counter(line[i] for line in a.lines).most_common(1))
# printd(w)
w = int(string(w.values()), 2)
z = int(string(z.values()), 2)
# z = int(z.values(), 2)
# print(w, z)
ans(w * z)

# for line in a.lines:
li = a.lines
for i in range(len(a.lines[0])):
    c = [line[i] for line in li]
    c = string(c)
    more = "1" if c.count("1") >= c.count("0") else "0"
    li = [line for line in li if line[i] == more]
    if len(li) == 1:
        break

q = int(li[0], 2)

li = a.lines
for i in range(len(a.lines[0])):
    c = [line[i] for line in li]
    # print(c)
    c = string(c)
    more = "1" if c.count("1") < c.count("0") else "0"
    li = [line for line in li if line[i] == more]
    if len(li) == 1:
        break

z = int(li[0], 2)
print(q, z)
    # w[i] = (x[0] for x in Counter(line[i] for line in a.lines).most_common(1))
ans(q * z)