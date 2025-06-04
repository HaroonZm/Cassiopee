import sys

moves = [(-1,0),(1,0),(0,-1),(0,1)]

def can_draw(s):
    if any(s[i] == s[i+1] for i in range(len(s)-1)):
        return False
    pos = {}
    for r in range(3):
        for c in range(3):
            pos[chr(ord('A')+r*3+c)] = (r,c)
    for i in range(len(s)-1):
        if s[i] not in pos or s[i+1] not in pos:
            return False
        r1,c1 = pos[s[i]]
        r2,c2 = pos[s[i+1]]
        if abs(r1 - r2) + abs(c1 - c2) != 1:
            return False
    return True

for line in sys.stdin:
    pw = line.strip()
    if pw and can_draw(pw):
        print(pw)