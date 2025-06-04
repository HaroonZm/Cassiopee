while True:
    n = int(input())
    if n == 0:
        break
    teams = []
    for i in range(n):
        data = input().split()
        name = data[0]
        w = int(data[1])
        l = int(data[2])
        d = int(data[3])
        points = w * 3 + d * 1
        teams.append((name, points, i))
    teams.sort(key=lambda x: (-x[1], x[2]))
    for team in teams:
        print(f"{team[0]},{team[1]}")
    print()