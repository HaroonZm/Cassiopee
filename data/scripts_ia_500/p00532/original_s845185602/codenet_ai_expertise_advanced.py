N, M = int(input()), int(input())
target = list(map(int, input().split()))
yosou = [list(map(int, input().split())) for _ in range(M)]

ten = [0] * N
for i in range(M):
    hazure = sum(t != y for t, y in zip(target, yosou[i]))
    for j, y in enumerate(yosou[i]):
        if target[i] == y:
            ten[j] += 1
    ten[target[i] - 1] += hazure

print(*ten, sep='\n')