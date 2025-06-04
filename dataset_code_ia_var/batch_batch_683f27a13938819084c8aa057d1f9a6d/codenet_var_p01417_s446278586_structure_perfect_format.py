import itertools

N, M = map(int, raw_input().split())
data = [map(float, raw_input().split()) for _ in range(N)]
maxV = 0.0

for comb in itertools.combinations(range(N), M):
    dist = 0.0
    for i in range(M - 1):
        for j in range(i + 1, M):
            t = comb[i]
            s = comb[j]
            dist += (
                pow(data[t][0] - data[s][0], 2) +
                pow(data[t][1] - data[s][1], 2) +
                pow(data[t][2] - data[s][2], 2)
            )
    maxV = max(maxV, dist)

print maxV