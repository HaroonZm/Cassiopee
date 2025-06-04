try:
    go = 1
    while go:
        line = input()
        parts = line.split()
        nums = list(map(int, parts))
        n, a, b, c, x = nums
        if not n:
            go = 0
            continue
        s2 = input().split()
        yis = [int(l) for l in s2]
        res, ok = 0, 1
        z = 0
        def nex(x):
            return (a*x+b)%c
        for idx, y in enumerate(yis):
            cnt=0
            if idx:
                x = nex(x)
                res += 1
            while x != y and res <= 10000:
                x = nex(x)
                res += 1
            if res > 10000:
                print(-1)
                ok = 0
                break
        if ok:
            print(res)
except:
    pass