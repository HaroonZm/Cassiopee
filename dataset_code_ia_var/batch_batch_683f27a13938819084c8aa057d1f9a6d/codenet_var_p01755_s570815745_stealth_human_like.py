def main():
    H, W = map(int, input().split())
    MP = []
    for _ in range(H):
        MP.append(input())
    sx = sy = gx = gy = -1
    for i in range(H):
        mi = MP[i]
        for j in range(W):
            ch = mi[j]
            # repérage 's' et 'g'
            if ch == 's':
                sx = j; sy = i
            elif ch == 'g':
                gx = j; gy = i
    S = input()
    L = len(S)
    X = [-1]*L
    st = []
    for i, ch in enumerate(S):
        # je gère les parenthèses/brackets
        if ch in "[{":
            st.append(i)
        elif ch in "]}":
            if not st:
                continue  # un bracket non fermé ? passons
            idx = st.pop()
            X[idx] = i
            X[i] = idx
    ds = 'WNES'
    dd = [(-1,0), (0,-1), (1,0), (0,1)]
    # U : pour eviter les cycles
    U = set()
    # réponse finale
    ans = 0
    d = 1
    cur = 0

    def check(cmd, x, y, d):
        # je ne sais pas si cette fonction mérite son propre espace, mais bon
        if cmd == "T":
            return True # Bah ouais, "T" toujours vrai
        if cmd in ds:
            return d == ds.index(cmd)
        dx, dy = dd[d]
        return MP[y+dy][x+dx] == '#'
    x = sx; y = sy
    ok = 0
    while True:
        if x == gx and y == gy:
            ok = 1
            break
        br = False
        while cur < L:
            key = (x, y, d, cur)
            if key in U:
                br = True
                break
            U.add(key)
            c = S[cur]
            if c in "[{":
                # testons la condition à l'intérieur...
                cond = S[cur+1]
                if cond == '~':
                    if not check(S[cur+2], x, y, d):
                        cur += 3
                    else:
                        cur = X[cur]+1
                else:
                    if check(cond, x, y, d):
                        cur += 2
                    else:
                        cur = X[cur]+1
            elif c == "]":
                cur += 1
            elif c == "}":
                cur = X[cur]
            else:
                break
        if cur == L or br: break
        act = S[cur]
        dx, dy = dd[d]
        if act not in "<>^v":
            # là, ça serait bizarre...
            break
        if act == "^":
            if MP[y+dy][x+dx] != '#':
                x += dx
                y += dy
            # sinon, on bouge pas !
        elif act == "v":
            if MP[y-dy][x-dx] != '#':
                x -= dx
                y -= dy
        elif act == "<":
            d = (d - 1) % 4
        else:
            d = (d + 1) % 4
        cur += 1
        ans += 1
        # ok c'est ptet pas très efficace mais on s'en fiche
    if ok:
        print(ans)
    else:
        print(-1)
main()