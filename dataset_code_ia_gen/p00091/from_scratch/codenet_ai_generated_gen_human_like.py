n = int(input())
cloth = [list(map(int, input().split())) for _ in range(10)]

# Define blur patterns for each drop size
# For each size: list of (dx, dy) positions relative to center, including center
patterns = {
    1: [(-1, -1), (0, -1), (1, -1),
        (-1,  0), (0,  0), (1,  0),
        (-1,  1), (0,  1), (1,  1)],
    2: [(-2, 0), (-1, -1), (0, -1), (1, -1), (2, 0),
        (-1, 0),  (0, 0),   (1, 0),
        (-1, 1),  (0, 1),   (1, 1)],
    3: [(-3, 0), (-2, -1), (-1, -1), (0, -1), (1, -1), (2, -1), (3, 0),
        (-2, 0), (-1, 0),  (0, 0),  (1, 0),  (2, 0),
        (-2, 1), (-1, 1),  (0, 1),  (1, 1),  (2, 1),
        (0, 2)]
}

# After analysis of the problem and images, the patterns are:
# Small (1): 3x3 square centered
# Medium (2): cross shape vertical 3 and horizontal 5 with center overlap (total 11)
# Large (3): bigger plus shape with extra bottom at (0,2) (total 17)

# But problem requires recreating drops and positions.
# We can predefine actual patterns from problem figures:

# From problem figure, the patterns for small, medium and large are:

# Small (1):
small = [(x,y) for y in range(-1,2) for x in range(-1,2)]
# Medium (2):
medium = [
    (-1,-2), (0,-2), (1,-2),
    (-2,-1), (-1,-1), (0,-1), (1,-1), (2,-1),
    (-2,0),  (-1,0),  (0,0),  (1,0),  (2,0),
    (-1,1),  (0,1),   (1,1)
]
# Large (3):
large = [
    (0,-3),
    (-1,-2), (0,-2), (1,-2),
    (-2,-1), (-1,-1), (0,-1), (1,-1), (2,-1),
    (-3,0), (-2,0), (-1,0), (0,0), (1,0), (2,0), (3,0),
    (-2,1), (-1,1), (0,1), (1,1), (2,1),
    (0,2)
]

patterns = {1: small, 2: medium, 3: large}

# Because patterns must be inside 10x10 cloth for each drop,
# possible centers:
valid_centers = {}
for size, pattern in patterns.items():
    centers = []
    for cx in range(10):
        for cy in range(10):
            if all(0 <= cx+dx <10 and 0 <= cy+dy <10 for dx,dy in pattern):
                centers.append((cx,cy))
    valid_centers[size]=centers

# Make a copy of cloth for deduction
cloth_copy = [row[:] for row in cloth]

res = []

for _ in range(n):
    found = False
    for size in [3,2,1]:
        for cx, cy in valid_centers[size]:
            # check if pattern can be removed (ie all cells in pattern >=1)
            if all(cloth_copy[cy+dy][cx+dx]>=1 for dx,dy in patterns[size]):
                # remove pattern (subtract 1 from each cell covered)
                for dx,dy in patterns[size]:
                    cloth_copy[cy+dy][cx+dx] -= 1
                res.append((cx, cy, size))
                found = True
                break
        if found:
            break

# print results
for x,y,s in res:
    print(x,y,s)