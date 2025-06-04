from sys import stdin

# Face order: [top, front, right, back, left, bottom]
# We'll represent cubes as tuples of 6 colors.

# 24 rotations of the cube:
# Each rotation returns a new orientation of the cube faces in the order [top, front, right, back, left, bottom].
# Reference: https://stackoverflow.com/questions/33177115/how-to-get-all-the-24-orientations-of-a-cube
def rotations(c):
    t,f,r,b,l,d = c
    # The 24 orientations are obtained by orienting the cube in 6 directions (top face), and rotating it 4 times around vertical axis.

    def roll(cube): # rotate cube to get new top
        t,f,r,b,l,d = cube
        return (f, d, r, t, l, b)
    def turn(cube): # rotate cube 90° around vertical axis
        t,f,r,b,l,d = cube
        return (t, l, f, r, b, d)
    rots = []
    cur = c
    for _ in range(6):
        for _ in range(4):
            rots.append(cur)
            cur = turn(cur)
        if _%2==0:
            cur = roll(cur)
        else:
            # for 2nd and 4th rolls, do roll thrice (roll^-1)
            cur = roll(roll(roll(cur)))
    # unique orientations only (should be 24)
    uniq = []
    seen = set()
    for r in rots:
        if r not in seen:
            seen.add(r)
            uniq.append(r)
    return uniq

def min_repaints(cubes):
    n = len(cubes)
    all_rots = [rotations(cube) for cube in cubes]  # list of list of 24 tuples
    min_cost = float('inf')
    # Choose for each cube an orientation (24^n <= 24^4 = 331,776 manageable)
    # For each orientation combination, compute minimal repaint cost:
    # Find for each face position the most common color, repaint other faces
    from collections import Counter
    import itertools
    for orientation_indices in itertools.product(range(24), repeat=n):
        faces = [all_rots[i][orientation_indices[i]] for i in range(n)]
        cost = 0
        for face_pos in range(6):
            colors = [faces[i][face_pos] for i in range(n)]
            cnt = Counter(colors)
            most_common = cnt.most_common(1)[0][1]
            cost += n - most_common
            if cost >= min_cost:
                break
        if cost < min_cost:
            min_cost = cost
    return min_cost

def main():
    lines = stdin.read().strip('\n ').split('\n')
    idx = 0
    while True:
        if idx >= len(lines):
            break
        n = lines[idx].strip()
        idx += 1
        if n == '0':
            break
        n = int(n)
        cubes = []
        for _ in range(n):
            cube_colors = lines[idx].strip().split()
            idx += 1
            cubes.append(tuple(cube_colors))
        print(min_repaints(cubes))

if __name__ == "__main__":
    main()