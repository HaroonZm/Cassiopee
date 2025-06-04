import sys

def read_elements(n, lines):
    elems = []
    while len(elems) < n:
        line = lines.pop(0).strip()
        elems.extend(line.split())
    return elems[:n]

def add_pos(p1, direction):
    x, y, z = p1
    if direction == '+x':
        return (x+1, y, z)
    elif direction == '-x':
        return (x-1, y, z)
    elif direction == '+y':
        return (x, y+1, z)
    elif direction == '-y':
        return (x, y-1, z)
    elif direction == '+z':
        return (x, y, z+1)
    elif direction == '-z':
        return (x, y, z-1)
    else:
        return p1

def parse_key_description(elems):
    label_pos = {}
    pos_label = {}
    bars = set()
    idx = 0
    l = len(elems)
    start_points = {}
    # first path starts at origin
    origin = (0,0,0)
    curr_pos = origin
    if elems[idx].isdigit(): # label at start?
        label = int(elems[idx])
        label_pos[label] = curr_pos
        pos_label[curr_pos] = label
        idx += 1

    positions_taken = set()
    positions_taken.add(curr_pos)

    while idx < l:
        elem = elems[idx]

        if elem.isdigit():
            label = int(elem)
            # start a new path at the labeled position
            curr_pos = label_pos[label]
            idx += 1
            # next elem must be direction
            continue
        else:
            # elem is a direction
            new_pos = add_pos(curr_pos, elem)
            # check overlapping bars - but problem says input valid, so we trust
            bar = tuple(sorted([curr_pos,new_pos]))
            if bar in bars:
                # a bar already exists here, invalid input but we can just ignore as input valid
                pass
            bars.add(bar)
            curr_pos = new_pos
            positions_taken.add(curr_pos)
            idx += 1
            # check if next elem is label for this point
            if idx < l and elems[idx].isdigit():
                label = int(elems[idx])
                if label not in label_pos:
                    label_pos[label] = curr_pos
                    pos_label[curr_pos] = label
                idx += 1
    return bars

def normalize_key(bars):
    points = set()
    for b in bars:
        points.add(b[0])
        points.add(b[1])
    # translate so min coord is at origin
    minx = min(p[0] for p in points)
    miny = min(p[1] for p in points)
    minz = min(p[2] for p in points)
    def translate(p):
        return (p[0]-minx, p[1]-miny, p[2]-minz)
    norm_bars = set()
    for b in bars:
        p1 = translate(b[0])
        p2 = translate(b[1])
        norm_bars.add(tuple(sorted([p1,p2])))
    return norm_bars

def generate_rotations(pos):
    x,y,z = pos
    # all 24 rotations of cube around origin
    rotations = []
    # helper: rotate around x axis
    def rx(p): return (p[0], -p[2], p[1])
    # rotate around y axis
    def ry(p): return (p[2], p[1], -p[0])
    # rotate around z axis
    def rz(p): return (-p[1], p[0], p[2])

    def all_rotations(p):
        res = []
        p0 = p
        for i in range(4): # around x axis
            p0 = rx(p0) if i>0 else p0
            p1 = p0
            for j in range(4): # around y axis
                p1 = ry(p1) if j>0 else p1
                p2 = p1
                for k in range(4): # around z axis
                    p2 = rz(p2) if k>0 else p2
                    res.append(p2)
        return res

    # but this generates duplicates, better explicit 24 rotations
    return [
        (x, y, z), (x, -z, y), (x, -y, -z), (x, z, -y),
        (-x, -y, z), (-x, -z, -y), (-x, y, -z), (-x, z, y),
        (y, z, x), (y, -x, z), (y, -z, -x), (y, x, -z),
        (-y, -z, x), (-y, -x, -z), (-y, z, -x), (-y, x, z),
        (z, x, y), (z, -y, x), (z, -x, -y), (z, y, -x),
        (-z, -x, y), (-z, -y, -x), (-z, x, -y), (-z, y, x),
    ]

def rotate_key(bars, rot_idx):
    rotated_bars = set()
    for b in bars:
        p1, p2 = b
        rp1 = generate_rotations(p1)[rot_idx]
        rp2 = generate_rotations(p2)[rot_idx]
        rotated_bars.add(tuple(sorted([rp1, rp2])))
    return rotated_bars

def translate_bars(bars):
    points = set()
    for b in bars:
        points.add(b[0])
        points.add(b[1])
    minx = min(p[0] for p in points)
    miny = min(p[1] for p in points)
    minz = min(p[2] for p in points)
    def translate(p): return (p[0]-minx, p[1]-miny, p[2]-minz)
    translated = set()
    for b in bars:
        translated.add(tuple(sorted([translate(b[0]), translate(b[1])])))
    return translated

def keys_equal(bars1, bars2):
    if len(bars1) != len(bars2):
        return False
    for rot in range(24):
        rbars = rotate_key(bars1, rot)
        rbars = translate_bars(rbars)
        if rbars == bars2:
            return True
    return False

def main():
    lines = sys.stdin.read().splitlines()
    idx = 0
    
    while True:
        if idx >= len(lines):
            break
        line = lines[idx].strip()
        if line == '0':
            break
        if not line.isdigit():
            idx += 1
            continue
        n1 = int(line)
        idx += 1
        elems1 = []
        while len(elems1) < n1:
            elems1.extend(lines[idx].strip().split())
            idx += 1

        n2 = int(lines[idx].strip())
        idx += 1
        elems2 = []
        while len(elems2) < n2:
            elems2.extend(lines[idx].strip().split())
            idx += 1

        bars1 = parse_key_description(elems1)
        bars2 = parse_key_description(elems2)

        bars1 = normalize_key(bars1)
        bars2 = normalize_key(bars2)
        if keys_equal(bars1, bars2):
            print("SAME")
        else:
            print("DIFFERENT")

if __name__ == '__main__':
    main()