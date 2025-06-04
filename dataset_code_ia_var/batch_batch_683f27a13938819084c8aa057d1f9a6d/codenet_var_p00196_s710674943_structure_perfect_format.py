while True:
    n = int(input())
    if n == 0:
        break
    team = []
    for i in range(n):
        r = input().split()
        t = r.pop(0)
        w = 0
        l = 0
        for p in r:
            if int(p) == 0:
                w += 1
            elif int(p) == 1:
                l += 1
        team.append((t, i, w, l))
    for i in sorted(team, key=lambda x: (-x[2], x[3], x[1])):
        print(*i[0])