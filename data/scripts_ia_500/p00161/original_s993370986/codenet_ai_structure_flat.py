while True:
    n = int(input())
    if n == 0:
        break
    times = []
    for _ in range(n):
        line = input().split()
        i = int(line[0])
        t = 0
        for j in range(1, len(line), 2):
            m = int(line[j])
            s = int(line[j+1])
            t += m * 60 + s
        times.append((t, i))
    for k in range(len(times)-1):
        for l in range(k+1, len(times)):
            if times[k][0] > times[l][0]:
                times[k], times[l] = times[l], times[k]
    print(times[0][1])
    print(times[1][1])
    print(times[-2][1])