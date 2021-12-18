import sys
sys.path.append('C:/Users/cobou/Documents/Python/adventOfCodeMisc/library')
from AoCLibrary import *

a = AdventInput("input18.txt")
inp = a.data

def split(line: list, x, match):
    line = line.copy()
    temp = int(match)
    pair = f"[{(temp//2)},{ceil(temp/2)}]"
    line[x:x+len(match)] = list(pair)
    line = string(line)

    return list(line)


def explode(line, x, match):
    line = line.copy()

    lval, rval = nums(match)
    lbound1 = 0
    lbound2 = 0
    for i in range(1, 1000):
        if x - i < 0:
            break
        if line[x-i].isnumeric():
            if lbound2 == 0:
                lbound2 = x-i
                lbound1 = x-i
            else:
                lbound1 -= 1
        elif lbound2 != 0:
            break
    
    rbound1 = 0
    rbound2 = 0
    for i in range(1000):
        if x+len(match) + i >= len(line):
            break
        if line[x+len(match)+i].isnumeric():
            if rbound2 == 0:
                rbound1 = x+len(match)+i
                rbound2 = x+len(match)+i
            else:
                rbound2 += 1
        elif rbound2 != 0:
            break

    lbound2 += 1
    rbound2 += 1

    if string(line[rbound1:rbound2]).isnumeric():
        line[rbound1:rbound2] = list(str(int(string(line[rbound1:rbound2])) + rval))
    for i in range(len(match)):
        line.pop(x)
    line.insert(x, 0)
    if string(line[lbound1:lbound2]).isnumeric():
        line[lbound1:lbound2] = str(int(string(line[lbound1:lbound2])) + lval)

    line = string(line)

    return list(line)

def look_for_explode(line):
    line = list(line)
    depth = 0
    x = 0
    while 0 <= x < len(line):
        if line[x] == "[":
            depth += 1
        elif line[x] == "]":
            depth -= 1
        s = string(line)
        if line[x] == '[' and depth >= 5:
            pot = re.match(r"^\[\d+,\d+\]", string(line[x:]))
            if pot:
                line = explode(line, x, pot.group())
                # show_depth(line)
                x = 0
                depth = 0
                continue
        x += 1
    return line

def look_for_split(line):
    line = list(line)
    x = 0
    while 0 <= x < len(line):
        if line[x].isnumeric():
            pot = re.match(r"^\d{2,}", string(line[x:]))
            if pot:
                line = split(line, x, pot.group())
                # show_depth(line)
                break
        x += 1
    return line

def run(z):
    line = list(z)
    before = line.copy()
    while True:
        line = look_for_explode(line)
        line = look_for_split(line)
        if string(line) == string(before):
            break
        before = line.copy()
    return string(line)

def parse(s):
    s_lines = lines(s)
    if len(s_lines) == 1:
        cur = run(s)
        return cur
    start = "[" + ",".join(s_lines[:2]) +"]"
    cur = run(start)
    for i in range(2, len(s_lines)):
        cur = "[" + cur + "," + s_lines[i] + "]"
        cur = run(cur)
    
    return cur

def show_depth(line):
    depth = 0
    for i in range(len(line)):
        if line[i] == '[':
            depth += 1
        elif line[i] == ']':
            depth -= 1
        print(depth, end='')
    print()

class Pair:
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right
    def get_magnitude(self):
        first = self.left if type(self.left) == int else self.left.get_magnitude()
        second = self.right if type(self.right) == int else self.right.get_magnitude()
        return first * 3 + second * 2
    
def exec_format(s : str):
    s = s.replace("[", "Pair(").replace("]",")")
    return s

def get_mag(lines):
    res = (parse(lines))
    formatted = exec_format(res)
    # print(formatted)
    exec("ob=" + formatted, globals())
    return (ob.get_magnitude())

RAW = '''[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]'''
assert (get_mag(RAW)) == 4140
ans(get_mag(inp))

def part2(lines):
    best = -1
    for x, y in permutations(lines.split("\n"), 2):
        best = max(best, get_mag(x+"\n"+y))
    return best
# assert part2(RAW) == 3993


ans(part2(inp))
