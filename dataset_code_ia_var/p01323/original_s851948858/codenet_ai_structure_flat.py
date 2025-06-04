for _ in range(int(input())):
    a = [["." for _ in range(8)]] + [["."] + list(input()) + ["."] for _ in range(12)] + [["." for _ in range(8)]]
    rensa = 0
    while 1:
        n = set()
        # Plate version of kesu pour tout
        for i1 in range(1, 13):
            for j1 in range(1, 7):
                if a[i1][j1] in ("RGBYP"):
                    stack = [((i1, j1), 0)]
                    s = set()
                    c = a[i1][j1]
                    while stack:
                        (x0, x1), h = stack.pop()
                        if (x0, x1) in s: continue
                        s.add((x0, x1))
                        if (x0 - 1, x1) not in s and a[x0 - 1][x1] == c:
                            stack.append(((x0 - 1, x1), h + 1))
                        if (x0 + 1, x1) not in s and a[x0 + 1][x1] == c:
                            stack.append(((x0 + 1, x1), h + 1))
                        if (x0, x1 - 1) not in s and a[x0][x1 - 1] == c:
                            stack.append(((x0, x1 - 1), h + 1))
                        if (x0, x1 + 1) not in s and a[x0][x1 + 1] == c:
                            stack.append(((x0, x1 + 1), h + 1))
                    if len(s) > 3:
                        for i in s:
                            a[i[0]][i[1]] = "."
                        n |= s
        if n == set():
            break
        else:
            rensa += 1
            for i in range(1, 13):
                for j in range(1, 7):
                    if a[i][j] == "O":
                        if (i - 1, j) in n or (i + 1, j) in n or (i, j - 1) in n or (i, j + 1) in n:
                            a[i][j] = "."
        # Plate version of otosu
        for i in range(1,12)[::-1]:
            for j in range(1, 7):
                n2 = 0
                while i + n2 < 12:
                    if a[i + n2][j] != "." and a[i + n2 + 1][j] == ".":
                        a[i + n2][j], a[i + n2 + 1][j] = a[i + n2 + 1][j], a[i + n2][j]
                        n2 += 1
                    else:
                        break
    print(rensa)