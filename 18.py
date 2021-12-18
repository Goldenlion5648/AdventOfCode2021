import sys
sys.path.append('C:/Users/cobou/Documents/Python/adventOfCodeMisc/library')
from AoCLibrary import *

a = AdventInput("input18.txt")
inp = a.data


def split(line: list, x, match):
    # length = 0
    print("got")
    print(string(line))
    print("match", match)
    # while line[x + length].isnumeric():
    #     length += 1
    line = line.copy()
    temp = int(match)
    # for i in range(len(match)):
    #     line.pop(x)
    # temp = int(string(line[x:x+length]))
    # for i in range(length):
    #     line.pop(x)
    # line = string(line)
    # print("after pop\n", line)
    # line = list(line)
    pair = f"[{(temp//2)},{ceil(temp/2)}]"
    line[x:x+len(match)] = list(pair)
    # line = list(flatten(line))
    # print("flattened", line)
    line = string(line)
    print("after split")
    print(line)
    # input()

    return list(line)


def explode(line, x, match):
    line = line.copy()
    print(line[x])
    print("match", match)
    lval, rval = nums(match)
    # rval = 0
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
            # line[x-i] = str(int(line[x-i]) + int(line[x]))
            # break
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
            # line[right+i] = str(int(line[right+i]) + int(line[right]))
    
    # # line[x] = '0'
    # right = x + 1
    # while right < len(line) and not line[right].isnumeric():
    #     right += 1
    # print("right", right)
    
    # print(lbound1, lbound2)
    # print(rbound1, rbound2)
    lbound2 += 1
    rbound2 += 1
    print("before")
    # print(line)
    print(string(line))
    if string(line[rbound1:rbound2]).isnumeric():
        line[rbound1:rbound2] = list(str(int(string(line[rbound1:rbound2])) + rval))
    for i in range(len(match)):
        line.pop(x)
    line.insert(x, 0)
    if string(line[lbound1:lbound2]).isnumeric():
        line[lbound1:lbound2] = str(int(string(line[lbound1:lbound2])) + lval)
    # line[right] = '0'
    print("ended with")
    # print(line)
    line = string(line)
    print(line)
    # line = re.sub(r"\[0,0\],(\d)", r"0,\1", line)
    # line = re.sub(r"(\d),\[0,0\]", r"\1,0", line)
    # line = list(line)
    # line.pop(x-1)
    # for i in range(3):
    #     line.pop(x)
    # line = string(line)
    # print('after')
    # pritn(line)
    return list(line)

# formula = ",".join(a.lines)
# print(a.lines)


# for z in a.lines:
def run(z, start_depth=0):
    line = list(z)
    depth = start_depth
    # for x in line:
    changed = True
    while changed:
        x = 0
        before = line.copy()
        potential_stop = -1
        while 0 <= x < len(line):
            if line[x] == "[":
                depth += 1
            elif line[x] == "]":
                depth -= 1
            s = string(line)
            print("cur", line[x])
            print("depth", depth)
            # match =re.search(r"\d\d", s)
            # print("match", match) 
            if line[x] == '[' and depth >= 5:
                pot = re.match(r"^\[\d+,\d+\]", string(line[x:]))
                if pot:
                    line = explode(line, x, pot.group())
                    show_depth(line)
                    # x = 0
                    # depth -= 1
                    # print(line)
                    input()
                    # continue
            if line[x].isnumeric():
                pot = re.match(r"^\d{2,}", string(line[x:]))
                if pot:
                    potential_stop = x
                    line = split(line, x, pot.group())
                    show_depth(line)
                    x -= 1
                    # depth += 1
                    # print(line)
                    input()
                    # continue
                
            x += 1
        changed = before != line

        # print(line)
    print(string(line))
    return string(line)


formula = '[[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]],[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]]'
formula = '[[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]'
formula = "[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]"
# run(inp)
# assert run("[[[[[9,8],1],2],3],4]") == "[[[[0,9],2],3],4]"
# assert run("[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]") == "[[3,[2,[8,0]]],[9,[5,[7,0]]]]"
# assert run("[[6,[5,[4,[3,2]]]],1]") == "[[6,[5,[7,0]]],3]"
# assert run("[7,[6,[5,[4,[3,2]]]]]") == "[7,[6,[5,[7,0]]]]"
# assert run("[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]")

def parse(s):
    s_lines = lines(s)
    start = "[" + (",".join(s_lines[:2])) +"]"
    print("start")
    print(start)
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

RAW ='''[1,1]
[2,2]
[3,3]
[4,4]'''
# assert (parse(RAW)) == "[[[[1,1],[2,2]],[3,3]],[4,4]]"
RAW = '''[1,1]
[2,2]
[3,3]
[4,4]
[5,5]'''
# assert (parse(RAW)) == "[[[[3,0],[5,3]],[4,4]],[5,5]]"
RAW = '''[1,1]
[2,2]
[3,3]
[4,4]
[5,5]
[6,6]'''
# assert (parse(RAW)) == "[[[[5,0],[7,4]],[5,5]],[6,6]]"
# assert run("") == ""
# assert run("") == ""
RAW = '''[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
[7,[5,[[3,8],[1,4]]]]
[[2,[2,2]],[8,[8,1]]]
[2,9]
[1,[[[9,3],9],[[9,0],[0,7]]]]
[[[5,[7,4]],7],1]
[[[[4,2],2],6],[8,7]]'''
RAW = '''[[[[7,7],[7,8]],[[9,5],[8,7]]],[[[6,8],[0,8]],[[9,9],[9,0]]]]
[[2,[2,2]],[8,[8,1]]]'''
RAW = '''[[[[7,7],[7,7]],[[8,7],[8,7]]],[[[7,0],[7,7]],9]]
[[[[4,2],2],6],[8,7]]'''
RAW = '''[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]'''
# RAW = '''[[[[4,3],4],4],[7,[[8,4],9]]]
# [1,1]'''

print(parse(RAW))