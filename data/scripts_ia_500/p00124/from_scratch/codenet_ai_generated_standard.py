while True:
    n = int(input())
    if n == 0:
        break
    teams = []
    for i in range(n):
        data = input().split()
        name = data[0]
        w, l, d = map(int, data[1:])
        pts = w * 3 + d
        teams.append((i, name, pts))
    teams.sort(key=lambda x: (-x[2], x[0]))
    for _, name, pts in teams:
        print(f"{name},{pts}")
    print()