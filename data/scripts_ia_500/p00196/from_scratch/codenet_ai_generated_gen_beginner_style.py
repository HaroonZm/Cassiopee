while True:
    n = input()
    if n == '0':
        break
    n = int(n)
    teams = []
    for i in range(n):
        line = input().split()
        t = line[0]
        results = list(map(int, line[1:]))
        win = results.count(0)
        lose = results.count(1)
        teams.append((t, win, lose, i))
    # tri selon : win desc, lose asc, input order asc
    teams.sort(key=lambda x: (-x[1], x[2], x[3]))
    for team in teams:
        print(team[0])