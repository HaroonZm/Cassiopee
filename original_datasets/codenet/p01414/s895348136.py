def solve():
    from sys import stdin
    from itertools import combinations
    file_input = stdin
    
    N = int(file_input.readline())
    hw = [tuple(map(int, file_input.readline().split())) for i in range(N)]
    goal = (line.rstrip() for line in file_input)
    goal = ''.join(goal)
    
    R = 0
    G = 0
    B = 0
    b = 1
    for c in goal[:]:
        if c == 'R':
            R += b
        elif c == 'G':
            G += b
        else:
            B += b
        b <<= 1
    c_m = (R, G, B) # color mask
    g_m = (1 << 16) - 1 # goal mask
    
    stamps = []
    for r1, r2 in combinations(range(5), 2):
        rw = r2 - r1
        for c1, c2 in combinations(range(5), 2):
            cw = c2 - c1
            for h, w in hw:
                if (rw == h and cw == w) or \
                ((r1 == 0 or r2 == 4) and rw < h and cw == w) or \
                ((c1 == 0 or c2 == 4) and cw < w and rw == h) or \
                ((r1 == 0 or r2 == 4) and (c1 == 0 or c2 == 4) and \
                 rw < h and cw < w):
                    m = 1
                    for i in range(cw - 1):
                        m <<= 1
                        m += 1
                    m <<= c1
                    r_m = m
                    for i in range(rw - 1):
                        m <<= 4
                        m += r_m
                    m <<= (r1 * 4)
                    for c in c_m:
                        s = c & m
                        if s:
                            stamps.append((m ^ g_m, s))
                    break
    
    picture = [0]
    generated_picture = [False] * (2 ** 16)
    generated_picture[0] = True
    step = 0
    while True:
        t_picture = picture[:]
        picture = []
        step += 1
        for p in t_picture:
            for m, s in stamps:
                n_p = p & m | s
                if generated_picture[n_p]:
                    continue
                if n_p == g_m:
                    return step
                generated_picture[n_p] = True
                picture.append(n_p)

print(solve())