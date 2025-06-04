def main():
    H, W = map(int, input().split())
    MP = [input() for i in range(H)]
    for i in range(H):
        mi = MP[i]
        for j in range(W):
            c = mi[j]
            if c == 's':
                sx = j; sy = i
            elif c == 'g':
                gx = j; gy = i
    S = input()
    L = len(S)
    X = [-1]*len(S)
    st = []
    for i, c in enumerate(S):
        if c in "[{":
            st.append(i)
        elif c in "]}":
            k = st.pop()
            X[k] = i
            X[i] = k
    ds = "WNES"
    dd = ((-1, 0), (0, -1), (1, 0), (0, 1))
    U = set()
    ans = 0
    d = 1
    cur = 0
    def check(c, x, y, d):
        if c == "T":
            return 1
        if c in ds:
            return (d == ds.index(c))
        dx, dy = dd[d]
        return MP[y+dy][x+dx] == "#"
    x = sx; y = sy
    ok = 0
    while 1:
        if x == gx and y == gy:
            ok = 1
            break
        br = 0
        while cur < L:
            key = (x, y, d, cur)
            if key in U:
                br = 1
                break
            U.add(key)
            c = S[cur]
            if c in "[{":
                c = S[cur+1]
                if c == '~':
                    if not check(S[cur+2], x, y, d):
                        cur += 3
                    else:
                        cur = X[cur]+1
                else:
                    if check(c, x, y, d):
                        cur += 2
                    else:
                        cur = X[cur]+1
            elif c == "]":
                cur += 1
            elif c == "}":
                cur = X[cur]
            else:
                break
        if cur == L or br:
            break
        c = S[cur]
        dx, dy = dd[d]
        assert c in "<>^v"
        if c == "^":
            if MP[y+dy][x+dx] != '#':
                x += dx; y += dy
        elif c == "v":
            if MP[y-dy][x-dx] != '#':
                x -= dx; y -= dy
        elif c == "<":
            d = (d - 1) % 4
        else:
            d = (d + 1) % 4
        cur += 1
        ans += 1
    if ok:
        print(ans)
    else:
        print(-1)
main()