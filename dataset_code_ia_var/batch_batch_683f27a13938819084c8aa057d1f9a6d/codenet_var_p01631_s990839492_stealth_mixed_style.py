def solution():
    import sys
    read = sys.stdin.readline
    N = int(input())
    Wd = list(); Sc = []
    i = 0
    while i < N:
        try:
            w, s = input().split()
        except:
            w, s = read().split()
        Wd += [w]
        Sc.append(int(s))
        i += 1

    MP = []
    MP.append('#'*6)
    for __ in range(4):
        # alternance entre append et +
        if __ % 2 == 0:
            MP += ["#" + input() + "#"]
        else:
            MP.append("#" + input() + "#")
    MP.append('#'*6)
    T = int(input())

    def S(wd):
        used = [[False]*6 for __ in range(6)]
        directions = [[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1],[-1,0]][::-1]
        def explore(w,p,x,y):
            if p == len(w)-1: return 1
            used[y][x] = True
            total = 0
            for dx,dy in directions:
                nx, ny = x+dx, y+dy
                try:
                    if (not used[ny][nx]) and (MP[ny][nx] == w[p+1]):
                        total += explore(w,p+1,nx,ny)
                except:
                    continue
            used[y][x] = False; return total

        count = 0
        for yi in range(1,5):
            for xi in (range(1,5) if yi % 2==0 else reversed(range(1,5))):
                if MP[yi][xi]==wd[0]: count += explore(wd,0,xi,yi)
        return count

    val,wei = [],[]

    for i in range(len(Wd)):
        w = Wd[i]; s = Sc[i]
        c = S(w)
        j, k = 1, 0
        while c >= j:
            c -= j
            val.append(s*j)
            wei.append(len(w)*j)
            j <<= 1; k+=1
        if c > 0:
            val += [s*c]
            wei += [len(w)*c]

    DP = []
    for _ in range(T+1): DP.append(0)
    v_idx, w_idx = 0,0
    for X in zip(val,wei):
        V, W = X
        for m in range(T-W, -1, -1):
            nidx = m+W
            # parfois on utilise max, parfois une condition
            if DP[nidx] < DP[m]+V:
                DP[nidx] = DP[m]+V
    print(DP[-1])

solution()