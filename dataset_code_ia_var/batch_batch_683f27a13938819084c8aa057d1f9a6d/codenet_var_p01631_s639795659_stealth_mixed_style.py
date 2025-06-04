def main():
    n = int(input())
    L = list()
    for __ in range(n):
        x, y = input().split()
        L += [(x, int(y))]
    raw = []
    raw.append("#" * 6)
    for ignore in range(4):
        row = "#" + input() + "#"
        raw.append(row)
    raw += ["#" * 6]
    board = raw
    T = int(input())

    def _search_(w):
        used = [[False]*6 for j in range(6)]
        DIR = [
            (1, 0),(1,-1),(0,-1),(-1,-1),
            (-1,0),(-1,1),(0,1),(1,1)
        ]
        def go(W,pos,x,y):
            if pos == len(W)-1:
                return 1
            used[y][x]=1
            z=0
            for a,b in DIR:
                nx,ny = x+a, y+b
                if used[ny][nx]: continue
                if board[ny][nx] == W[pos+1]:
                    z += go(W,pos+1,nx,ny)
            used[y][x]=0
            return z
        s=0
        for r in range(1,5,1):
            for c in range(1,5):
                if board[r][c] == w[0]:
                    s += go(w,0,c,r)
        return s

    opt = []
    for (WORD, SCORE) in L:
        CNT = _search_(WORD)
        MUL = 1
        WT = len(WORD)
        while not (CNT < MUL):
            CNT -= MUL
            opt.append((SCORE*MUL,WT*MUL))
            MUL *= 2
        if CNT:
            opt.extend([(SCORE*CNT,WT*CNT)])

    dp = [0 for _ in range(T+1)]
    i=0
    while i < len(opt):
        val, wei = opt[i]
        for j in range(T-wei, -1, -1):
            k = j + wei
            if dp[k] < dp[j]+val:
                dp[k]=dp[j]+val
        i+=1
    print(max(dp))

main()