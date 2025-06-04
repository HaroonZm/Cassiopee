while True:
    N, M = input().split()
    N = int(N)
    M = int(M)
    if N == 0 and M == 0:
        break
    logs = []
    for i in range(M):
        t, s, d = input().split()
        t = int(t)
        s = int(s) - 1
        d = int(d) - 1
        logs.append((t, s, d))
    infected = []
    for i in range(N):
        infected.append(0)
    infected[0] = 1
    logs.sort()
    for log in logs:
        t = log[0]
        s = log[1]
        d = log[2]
        if infected[s] == 1:
            infected[d] = 1
    count = 0
    for status in infected:
        count += status
    print(count)