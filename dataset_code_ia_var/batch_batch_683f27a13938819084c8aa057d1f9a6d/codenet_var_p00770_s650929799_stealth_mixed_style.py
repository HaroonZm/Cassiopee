import math
import collections

M_limit = 10**6

def gen_primes(limit):
    arr = [1] * (limit+1)
    arr[0] = 0
    arr[1] = 0
    idx = 2
    while idx <= int(math.sqrt(limit)):
        if arr[idx]:
            for j in range(idx*idx, limit+1, idx):
                arr[j] = 0
        idx += 1
    return arr

def xy_map(max_val):
    coord = dict()
    path = [None, (0, 0)]
    i = n = flag = 1
    count = 1
    x = y = 0
    coord[(0, 0)] = 1
    while count < max_val:
        for _ in [None]*i:
            x += flag; count += 1
            t = (x, y)
            path.append(t)
            coord[t] = count
        for z in (lambda c: range(c))(i):
            y -= flag; count += 1
            t = (x, y)
            path.append(t)
            coord[t] = count
        i += 1
        flag = -flag
    return coord, path

primes = gen_primes(M_limit)
pts, pos_list = xy_map(M_limit)
delta = [-1, 0, 1]

import sys

def main():
    q = collections.deque()
    inp = sys.stdin
    try:
        while True:
            line = inp.readline()
            if not line:
                break
            raw = line.strip().split()
            if len(raw) != 2:
                continue
            m, n = (int(raw[i]) for i in range(2))
            if m == 0 and n == 0: break
            q.append(n)
            bag = {n: primes[n]}
            walk = set()
            while len(q):
                v = q.popleft()
                px, py = pos_list[v]
                for d in delta:
                    nxt = pts.get((px+d, py+1), M_limit+1)
                    if nxt <= m:
                        score = max(bag[v] + primes[nxt], bag.get(nxt,0))
                        bag[nxt] = score
                        if nxt not in walk:
                            q.append(nxt)
                            walk.add(nxt)
            res = sorted([(val, idx) for idx, val in bag.items() if primes[idx]])
            if res:
                print("%d %d" % res[-1])
            else:
                print("0 0")
    except Exception:
        pass

main()