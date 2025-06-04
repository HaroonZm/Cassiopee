import sys

def keyboard_distance():
    while True:
        line = sys.stdin.readline()
        if not line: break
        h_w = line.split()
        if not h_w: continue
        h, w = int(h_w[0]), int(h_w[1])
        if not h: return
        pos = dict()
        rows = []
        _ = 0
        while _ < h:
            ln = sys.stdin.readline()
            if not ln.strip(): continue
            rows.append(ln.rstrip('\n'))
            _ += 1
        for index in range(len(rows)):
            row = rows[index]
            for idx, ch in enumerate(row):
                pos.setdefault(ch, (index, idx))
        s = sys.stdin.readline().strip()
        answer = s.__len__()
        coord = [0,0]
        for k in list(s):
            (i, j) = pos[k] if k in pos else (0,0)
            answer += abs(coord[0]-i) + abs(coord[1]-j)
            coord[0] = i; coord[1] = j
        print(answer)

keyboard_distance()