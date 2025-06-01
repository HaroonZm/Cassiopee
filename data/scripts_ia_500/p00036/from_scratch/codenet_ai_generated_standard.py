import sys

shapes = {
    'A': {(0,0),(0,1),(0,2),(0,3)},
    'B': {(0,0),(1,0),(2,0),(3,0)},
    'C': {(0,0),(0,1),(1,0),(1,1)},
    'D': {(0,0),(1,0),(1,1),(2,1)},
    'E': {(0,1),(0,2),(1,0),(1,1)},
    'F': {(0,0),(0,1),(1,1),(1,2)},
    'G': {(0,1),(1,0),(1,1),(2,0)},
}

def normalize(points):
    min_r = min(p[0] for p in points)
    min_c = min(p[1] for p in points)
    return sorted(((r - min_r, c - min_c) for r,c in points))

def all_rotations(shape):
    # generate all rotations and flips, normalized
    pts = shape
    results = set()
    for _ in range(4):
        pts = [(c, -r) for r,c in pts]
        norm = tuple(normalize(pts))
        results.add(norm)
        # flip horizontally
        flipped = [(r, -c) for r,c in pts]
        norm_flipped = tuple(normalize(flipped))
        results.add(norm_flipped)
    return results

shape_variants = {}
for k,v in shapes.items():
    variants = all_rotations(list(v))
    shape_variants[k] = variants

data = sys.stdin.read().strip('\n ').split('\n')
datasets = []
cur = []
for line in data:
    if line.strip() == '':
        if cur:
            datasets.append(cur)
            cur = []
    else:
        cur.append(line)
if cur:
    datasets.append(cur)

for grid in datasets:
    points = [(r,c) for r,row in enumerate(grid) for c,ch in enumerate(row) if ch=='1']
    norm_pts = normalize(points)
    norm_pts_t = tuple(norm_pts)
    res = '?'
    for k,vset in shape_variants.items():
        if norm_pts_t in vset:
            res = k
            break
    print(res)