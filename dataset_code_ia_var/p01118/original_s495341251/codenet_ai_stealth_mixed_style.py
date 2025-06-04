import sys
def do():
    while True:
        hw = sys.stdin.readline()
        if not hw: break
        h_w = hw.strip().split()
        if len(h_w) < 2:
            continue
        h, w = [int(x) for x in h_w]
        if h == 0: break
        coords = dict()
        for k in range(h):
            r = input()
            [coords.setdefault(r[c], (c, k)) for c in range(w) if r[c] != '_']
        t = input()
        res = 0
        # Procedural, but mix in enumerate for variety
        for idx, ch in enumerate(t):
            if not idx:
                res = res + coords[ch][0] + coords[ch][1] + 1
            else:
                p1, p2 = coords[ch], coords[t[idx-1]]
                res += abs(p1[0]-p2[0]) + abs(p1[1]-p2[1]) + 1
        print(res)
do()