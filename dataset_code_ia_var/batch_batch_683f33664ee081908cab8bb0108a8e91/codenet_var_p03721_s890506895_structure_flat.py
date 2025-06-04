N, K = map(int, input().split())
ab = [0] * N
for i in range(N):
    ab[i] = list(map(int, input().split()))
ab.sort(key=lambda x: x[0])
count = 0
for i in range(N):
    count += ab[i][1]
    if count >= K:
        print(ab[i][0])
        break