from sys import stdin

# 24 rotations for cube faces indices:
# Faces: c1(top), c2(front), c3(right), c4(left), c5(back), c6(bottom)
# We'll generate all orientations by sequences of rotations.

def rotations(c):
    c1,c2,c3,c4,c5,c6 = c
    rots = []
    def rotate_x(c):
        # rotate cube around x-axis: top->front, front->bottom, bottom->back, back->top
        return (c[1], c[6], c[3], c[4], c[0], c[5])
    def rotate_y(c):
        # rotate cube around y-axis: front->right, right->back, back->left, left->front
        return (c[0], c[4], c[1], c[2], c[5], c[3])
    def rotate_z(c):
        # rotate cube around z-axis: right->top, top->left, left->bottom, bottom->right
        return (c[3], c[1], c[0], c[5], c[4], c[2])
    def to_list(t):
        return list(t)
    # Instead of simulating, we hardcode the 24 unique rotations by applying rotation sequences.
    states = set()
    def add_all_rotations(c):
        for i in range(4):
            c = rotate_x(c)
            for j in range(4):
                c = rotate_y(c)
                for k in range(4):
                    c = rotate_z(c)
                    states.add(c)
                c = rotate_z(c)
    # But the above approach repeats states, simpler to generate all 24 unique rotations by known method:
    # Method: For each of 6 faces as "top", 4 rotations
    configs = []
    def roll_X(c):
        c1,c2,c3,c4,c5,c6 = c
        return (c2,c6,c3,c4,c1,c5)
    def roll_Y(c):
        c1,c2,c3,c4,c5,c6 = c
        return (c1,c5,c2,c3,c4,c6)
    def roll_Z(c):
        c1,c2,c3,c4,c5,c6 = c
        return (c4,c2,c1,c6,c5,c3)
    res = []
    tmp = c
    for i in range(6):
        if i == 4:
            tmp = roll_Y(roll_Y(tmp))
        elif i > 0:
            tmp = roll_X(tmp)
        for j in range(4):
            if j > 0:
                tmp = roll_Z(tmp)
            res.append(tmp)
    return res

def canonical(c):
    # Return lex smallest among all rotations
    return min(rotations(c))

lines = stdin.read().strip().split('\n')
idx = 0
while True:
    if idx>=len(lines):
        break
    n = lines[idx].strip()
    idx+=1
    if n == '0':
        break
    n = int(n)
    cubes = []
    for _ in range(n):
        c = tuple(lines[idx].split())
        idx+=1
        cubes.append(c)
    # Find unique canonical forms
    seen = set()
    for c in cubes:
        seen.add(canonical(c))
    # Output how many more needed for unique set
    print(len(cubes)-len(seen))