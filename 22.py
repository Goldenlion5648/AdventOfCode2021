import sys
sys.path.append('C:/Users/cobou/Documents/Python/adventOfCodeMisc/library')
from AoCLibrary import *

a = AdventInput("input22.txt")
inp = a.data

from dataclasses import dataclass

@dataclass
class Side:
    '''the lower side'''
    start : int 
    '''the upper side'''
    stop : int
    def encloses(self, other):
        return (self.start <= other.start <= self.stop) and \
                    (self.start <= other.stop <= self.stop)
    def overlaps(self, other : 'Side'):
        '''returns (does_overlap, self encloses other)'''
        if self.start == other.stop or self.stop == other.start:
            return False
        return \
            (self.start <= other.start <= self.stop) or \
            (other.start <= self.start <= other.stop)


@dataclass
class Cuboid:
    xSide : Side
    ySide : Side
    zSide : Side
    is_on : bool
    def __hash__(self) -> int:
        return hash((self.xSide.start, self.xSide.stop, self.ySide.start, self.ySide.stop, self.zSide.start, self.zSide.stop))
        # return 
    def is_inside_of(self, other : 'Cuboid'):
        return other.xSide.encloses(self.xSide) and\
                other.ySide.encloses(self.ySide) and\
                other.zSide.encloses(self.zSide)
    def volume(self):
        return (self.xSide.stop - self.xSide.start) *\
                (self.ySide.stop - self.ySide.start) *\
                (self.zSide.stop - self.zSide.start) 
    def intersects(self, other : 'Cuboid'):
        return \
            (self.xSide.overlaps(other.xSide)) and \
            (self.ySide.overlaps(other.ySide)) and \
            (self.zSide.overlaps(other.zSide))
    
    def get_bounds(self, self_side : 'Side', other_side : 'Side'):
        '''
                A               A
        ---------------------------------
                        B   B           
        '''
        self_encloses_other = self_side.encloses(other_side)
        if other_side.encloses(self_side):
            return [self_side]
        if self_encloses_other:
            temp = [
                Side(self_side.start, other_side.start),
                Side(other_side.start, other_side.stop),
                Side(other_side.stop, self_side.stop)
            ]
            if not temp:
                print("returning nothing 1")
            return temp
        else:
            temp = [x for x in [other_side.stop, other_side.start] if x > self_side.start]
            if not temp:
                return []
            lowest_after_start = min(temp)
            return [
                Side(self_side.start, lowest_after_start),
                Side(lowest_after_start, self_side.stop),
            ]

    def split(self, other : 'Cuboid'):
        #go bottom to top
        if self.is_inside_of(other):
            return set()
        if not self.intersects(other):
            return {self}
        ret = set()
        for x in self.get_bounds(self.xSide, other.xSide):
            for y in self.get_bounds(self.ySide, other.ySide):
                for z in self.get_bounds(self.zSide, other.zSide):
                    cur = (Cuboid(x, y, z, True))
                    if cur not in ret and not(cur.is_inside_of(other)) :
                        ret.add(cur)

        return ret

    subtract = split
    def __sub__(self, other):
        return self.subtract(other)

all_cubes = []
part1_dict = dd(lambda: False)

for line_num, line in enu(a.lines, 1):
    cur = line.split()
    n = nums(line)
    lo, hi = n[:2]
    if lo < -50 or hi > 50:
        continue
    r1 = irange(lo, hi)
    lo, hi = n[2:4]
    if lo < -50 or hi > 50:
        continue
    r2 = irange(lo, hi)
    lo, hi = n[4:]
    if lo < -50 or hi > 50:
        continue
    r3 = irange(lo, hi)
    on = cur[0] == "on"
    for x in r1:
        for y in r2:
            for z in r3:
                part1_dict[x, y, z] = on

ans(sum(part1_dict.values()))


for line in a.lines:
    cur = line.split()
    n = nums(line)
    lo, hi = n[:2]
    on = cur[0] == "on"
    r1 = (lo, hi + 1)
    lo, hi = n[2:4]
    r2 = (lo, hi + 1)
    lo, hi = n[4:]
    r3 = (lo, hi + 1)
    all_cubes.append(Cuboid(Side(*r1), Side(*r2), Side(*r3), on))

on_cubes : Set['Cuboid'] = set()

def part2(to_add):
    global on_cubes

    for j, new_cube in enu(to_add, 1):
        if j % 50 == 0:
            print(j)
        if not on_cubes:
            on_cubes.add(new_cube)
            continue
        next_on_cubes = set()
        for existing_cube in on_cubes:
            about_to_add = existing_cube - new_cube
            next_on_cubes |= about_to_add
            
        if new_cube.is_on:
            next_on_cubes.add(new_cube)
        on_cubes = (next_on_cubes).copy()

part2(all_cubes)
total = sum(c.volume() for c in on_cubes)
ans(total)
