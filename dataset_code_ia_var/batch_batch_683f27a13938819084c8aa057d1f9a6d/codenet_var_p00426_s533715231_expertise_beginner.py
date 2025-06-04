def solve():
    from sys import stdin

    while True:
        n_m = stdin.readline().split()
        n = int(n_m[0])
        m = int(n_m[1])
        if n == 0:
            break

        cups = [None] * n
        for tray in "ABC":
            line = stdin.readline().split()
            count = int(line[0])
            for idx in line[1:]:
                cups[int(idx)-1] = tray

        def rec(i):
            if i == 0:
                return 0
            tray = cups[n - i]
            if tray == "A":
                return rec(i - 1)
            elif tray == "B":
                return 2 * (3 ** (i - 1)) - 1 - rec(i - 1)
            else:
                return rec(i - 1) + 2 * (3 ** (i - 1))

        num = rec(n)
        total = 3 ** n - 1
        ans = min(num, total - num)
        if ans <= m:
            print(ans)
        else:
            print(-1)

solve()