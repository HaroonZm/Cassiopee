while True:
    n = input()
    if n == '0':
        break
    n = int(n)
    teams = []
    for i in range(n):
        data = input().split()
        t = data[0]
        results = list(map(int, data[1:]))
        win = results.count(0)
        lose = results.count(1)
        teams.append((t, win, lose, i))
    teams.sort(key=lambda x: (-x[1], x[2], x[3]))
    for team in teams:
        print(team[0])