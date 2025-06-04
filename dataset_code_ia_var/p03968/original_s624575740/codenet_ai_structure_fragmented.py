import sys
from collections import Counter

def read_int():
    return int(sys.stdin.readline())

def read_tuple():
    return tuple(map(int, sys.stdin.readline().split()))

def compress(L):
    unique_sorted = get_sorted_unique(L)
    mapping = build_mapping(unique_sorted)
    return unique_sorted, mapping

def get_sorted_unique(L):
    return sorted(set(L))

def build_mapping(L):
    return {v: k for k, v in enumerate(L, 1)}

def order(a, b, c, d):
    if a == b == c == d:
        return 4
    if a == c and b == d:
        return 2
    return 1

def init_calc(limit):
    size = limit * 400
    calc = [[None]*limit for _ in range(size)]
    for i in range(size):
        calc[i][1] = i
        for j in range(2, limit):
            calc[i][j] = calc[i][j-1]*(i-j+1)
    return calc

def init_pp():
    return [[pow(i, j) for j in range(10)] for i in range(10)]

def all_rotations(t):
    a, b, c, d = t
    return [
        (a, b, c, d),
        (d, a, b, c),
        (c, d, a, b),
        (b, c, d, a),
    ]

def minimal_rotation(t):
    return min(all_rotations(t))

def process_rotations(C):
    Rot = []
    for t in C:
        Rot.extend(all_rotations(t))
    return Rot

def process_C(N, C, Cr):
    Cc = []
    Od = Counter()
    Base = Counter()
    D = Counter()
    for i in range(N):
        t = C[i]
        min_t = minimal_rotation(t)
        od = order(*min_t)
        r_idxs = [Cr[r] for r in all_rotations(min_t)]
        base = r_idxs[0]
        for r in r_idxs:
            Base[r] = base
            Od[r] = od
        Cc.append(tuple(r_idxs))
        D[base] += 1
    return Cc, Od, Base, D

def build_Lc(Lc):
    return [None] + Lc

def get_face_from_index(Lc, idx):
    return Lc[idx]

def process_pair(ans, D, calc, pp, Base, Od, Cr, Lc, Cc, i, j):
    for idx in range(4):
        E = Counter()
        t1 = get_face_from_index(Lc, Cc[i][0])
        t2 = get_face_from_index(Lc, Cc[j][idx])
        b = t1[1]
        c = t1[2]
        a = t1[0]
        d = t1[3]
        e, f, g, h = t2
        # Define the 4 tuples to look up
        faces = [
            (b, e, h, c),
            (a, f, e, b),
            (d, g, f, a),
            (c, h, g, d)
        ]
        valid = True
        rotated_idxs = []
        for face in faces:
            if face not in Cr:
                valid = False
                break
            rotated_idxs.append(Base[Cr[face]])
        if not valid:
            continue
        for r in rotated_idxs:
            E[r] += 1
        res = 1
        for k, n in E.items():
            res *= calc[D[k]][n] * pp[Od[k]][n]
        ans[0] += res

def main():
    limit = 5
    calc = init_calc(limit)
    pp = init_pp()
    N = read_int()
    C = [read_tuple() for _ in range(N)]
    Rot = process_rotations(C)
    Lc, Cr = compress(Rot)
    Lc = build_Lc(Lc)
    Cc, Od, Base, D = process_C(N, C, Cr)
    ans = [0]
    for i in range(N):
        D[Cc[i][0]] -= 1
        for j in range(i+1, N):
            D[Cc[j][0]] -= 1
            process_pair(ans, D, calc, pp, Base, Od, Cr, Lc, Cc, i, j)
            D[Cc[j][0]] += 1
        D[Cc[i][0]] += 1
    print(ans[0])

if __name__ == "__main__":
    main()