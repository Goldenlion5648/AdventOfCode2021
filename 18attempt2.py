import sys
sys.path.append('C:/Users/cobou/Documents/Python/adventOfCodeMisc/library')
from AoCLibrary import *
a = AdventInput('input18.txt')
inp = a.data

class Pair:
    def __init__(self, left, right, depth=0) -> None:
        self.left = left
        self.depth = depth
        self.right = right
        if isinstance(self.left, Pair):
            self.left.depth += 1
        if isinstance(self.right, Pair):
            self.right.depth += 1
    def __repr__(self) -> str:
        return f"{self.left},{self.right},{self.depth}\n"
    def get_leftmost(self):
        if isinstance(self.left,int):
            return self.left
        return self.left.get_leftmost()
    def get_rightmost(self):
        if isinstance(self.right,int):
            return self.right
        return self.right.get_rightmost()
        # if isinstance(left, int):
        # else:
            # self.rig
        # if isinstance(left, int):

def parse(s):
    s = s.replace("[", "Pair(").replace("]",")")
    # s = 'a=s' 
    
    return s
RAW = '''[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]],[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]'''
RAW = '''[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]'''
s = (parse(RAW))
exec('w='+s)
print(w)