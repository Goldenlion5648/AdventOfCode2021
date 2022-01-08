debug = False

seen = set()
r = range(9, 0, -1)
works = []
#section 1
def section1(cur, start_z):
    global seen
    if (1, start_z) in seen:
        return
    seen.add((1, start_z))
    for w in r:
        z = start_z
        x = 11
        z = 0
        if x != w:
            z *= 26
            z += w + 6
        if debug: print(f"1 {cur=} {z=}")
        section2(cur * 10 + w, z)
#section 2    
def section2(cur, start_z):
    global seen
    if (2, start_z) in seen:
        return
    seen.add((2, start_z))
    for w in r:
        z = start_z
        x = (z % 26) + 11
        z = int(z / 1)
        if x != w:
            z *= 26
            z += w + 12
        if debug: print(f"2 {cur=} {z=}")
        section3(cur * 10 + w, z)
#section 3    
def section3(cur, start_z):
    global seen
    if (3, start_z) in seen:
        return
    seen.add((3, start_z))
    # print(cur)
    # return
    for w in r:
        z = start_z
        x = (z % 26) + 15
        z = int(z / 1)
        if x != w:
            z *= 26
            z += w + 8
        if debug: print(f"3 {cur=} {z=}")
        section4(cur * 10 + w, z)
#section 4    
def section4(cur, start_z):
    global seen
    if (4, start_z) in seen:
        return
    seen.add((4, start_z))
    for w in r:
        z = start_z
        x = (z % 26) - 11
        z = int(z / 26)
        if x != w:
            z *= 26
            z += w + 7
        if debug: print(f"4 {cur=} {z=}")
        section5(cur * 10 + w, z)
#section 5    
def section5(cur, start_z):
    global seen
    if (5, start_z) in seen:
        return
    seen.add((5, start_z))
    # printe(seen)
    # input()
    # print(f"4 {cur=} {start_z=}")

    # return
    for w in r:
        z = start_z
        x = (z % 26) + 15
        z = int(z / 1)
        if x != w:
            z *= 26
            z += w + 7
        if debug: print(f"5 {cur=} {z=}")
        section6(cur * 10 + w, z)
#section 6    
def section6(cur, start_z):
    global seen
    if (6, start_z) in seen:
        return
    seen.add((6, start_z))
    for w in r:
        z = start_z
        x = (z % 26) + 15
        z = int(z / 1)
        if x != w:
            z *= 26
            z += w + 12
        if debug: print(f"6 {cur=} {z=}")
        section7(cur * 10 + w, z)
#section 7    
def section7(cur, start_z):
    global seen
    if (7, start_z) in seen:
        return  
    seen.add((7, start_z))
    for w in r:
        z = start_z
        x = (z % 26) + 14
        z = int(z / 1)
        if x != w:
            z *= 26
            z += w + 2
        if debug: print(f"7 {cur=} {z=}")
        section8(cur * 10 + w, z)
#section 8    
def section8(cur, start_z):
    global seen
    if (8, start_z) in seen:
        return
    seen.add((8, start_z))
    for w in r:
        z = start_z
        x = (z % 26) - 7
        z = int(z / 26)
        if x != w:
            z *= 26
            z += w + 15
        if debug: print(f"8 {cur=} {z=}")
        section9(cur * 10 + w, z)
#section 9    
def section9(cur, start_z):
    global seen
    if (9, start_z) in seen:
        return
    seen.add((9, start_z))
    for w in r:
        z = start_z
        x = (z % 26) + 12
        z = int(z / 1)
        if x != w:
            z *= 26
            z += w + 4
        if debug: print(f"9 {cur=} {z=}")
        section10(cur * 10 + w, z)
#section 10    
def section10(cur, start_z):
    global seen
    if (10, start_z) in seen:
        return
    seen.add((10, start_z))
    for w in r:
        z = start_z
        x = (z % 26) - 6
        z = int(z / 26)
        if x != w:
            z *= 26
            z += w + 5
        if debug: print(f"10 {cur=} {z=}")
        section11(cur * 10 + w, z)
#section 11    
def section11(cur, start_z):
    global seen
    if (11, start_z) in seen:
        return
    seen.add((11, start_z))
    for w in r:
        z = start_z
        x = (z % 26) - 10
        z = int(z / 26)
        if x != w:
            z *= 26
            z += w + 12
        if debug: print(f"11 {cur=} {z=}")
        section12(cur * 10 + w, z)
#section 12    
def section12(cur, start_z):
    global seen
    if (12, start_z) in seen:
        return
    seen.add((12, start_z))
    for w in r:
        z = start_z
        x = (z % 26) - 15
        z = int(z / 26)
        if x != w:
            z *= 26
            z += w + 11
        if debug: print(f"12 {cur=} {z=}")
        section13(cur * 10 + w, z)
#section 13    
def section13(cur, start_z):
    global seen
    if (13, start_z) in seen:
        return
    seen.add((13, start_z))
    # print(cur)
    for w in r:
        z = start_z
        x = (z % 26) - 9
        z = int(z / 26)
        if x != w:
            z *= 26
            z += w + 13
        if debug: print(f"13 {cur=} {z=}")
        section14(cur * 10 + w, z)
#section 14    
def section14(cur, start_z):
    global seen
    if (14, start_z) in seen:
        return
    seen.add((14, start_z))
    if len(seen) % 100000 == 0:
        print(f"{cur=}")
    for w in r:
        z = start_z
        x = (z % 26) + 0
        z = int(z / 26)
        if x != w:
            z *= 26
            z += w + 7

        if debug: print(f"14 {cur=} {z=}")
        if z == 0:
            print("works", cur * 10 + w)
            works.append(cur * 10 + w)
            assert False

#for part 1
r = range(9, 0, -1)
#for part 2
# r = range(1, 10)
section1(0, 0)
