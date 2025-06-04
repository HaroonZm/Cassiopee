from collections import defaultdict

while True:
    time = [[0 for _ in range(16)] for __ in range(64)]
    accepted = [[0 for _ in range(16)] for __ in range(64)]
    M, T, P, R = map(int, input().split())
    if M == 0 and T == 0:
        break
    for i in range(R):
        m, t, p, j = map(int, input().split())
        if j == 0:
            accepted[t][p] = 1
            time[t][p] = time[t][p] + m
        else:
            time[t][p] += 20
    score = defaultdict(int)
    for t in range(1, T + 1):
        for p in range(1, P + 1):
            score[t] += accepted[t][p] * (1 << 16)
            if accepted[t][p]:
                score[t] -= time[t][p]
    mp = defaultdict(list)
    for k, v in score.items():
        mp[v].append(k)
    output = ""
    for sc, ts in sorted(mp.items(), key=lambda x: x[0], reverse=True):
        output += '='.join(map(str, sorted(ts, reverse=True)))
        output += ','
    else:
        print(output[:-1])