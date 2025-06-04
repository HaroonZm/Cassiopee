while 1:
    n = int(input())
    if n == 0:
        break
    team = []
    for _ in range(n):
        i, *T = map(int, input().split())
        t = 0
        for m, s in zip(T[::2], T[1::2]):
            t += m*60 + s
        team.append((t, i))
    team.sort()
    print(*[team[0][1], team[1][1], team[-2][1]], sep='\n')