def solve(n):
    teams = []
    for i in range(n):
        teams.append(list(map(int, raw_input().split())))

    teams = sorted(teams, key=lambda x: -1e12 * x[2] + x[3] * 1e6 + x[0])

    A = []
    B = []
    threshold = 3
    for team in teams:
        if len(A) == 10:
            threshold = 2
        elif len(A) == 20:
            threshold = 1

        if B.count(team[1]) < threshold:
            A.append(team[0])
            B.append(team[1])

        if len(A) == 26:
            break

    for a in A:
        print(a)

while True:
    n = int(raw_input())
    if n == 0:
        break
    solve(n)