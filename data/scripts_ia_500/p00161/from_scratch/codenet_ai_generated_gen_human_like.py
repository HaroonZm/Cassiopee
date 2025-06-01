while True:
    n = int(input())
    if n == 0:
        break
    teams = []
    for _ in range(n):
        data = input().split()
        tid = int(data[0])
        times = list(map(int, data[1:]))
        total_seconds = 0
        for i in range(0, 8, 2):
            m = times[i]
            s = times[i+1]
            total_seconds += m * 60 + s
        teams.append((total_seconds, tid))
    teams.sort()
    print(teams[0][1])
    print(teams[1][1])
    print(teams[-2][1])