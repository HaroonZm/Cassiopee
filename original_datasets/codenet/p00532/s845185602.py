N = int(input())
M = int(input())

target = list(map(int, input().split()))
yosou = [list(map(int, input().split())) for i in range(M)]

ten = [0 for _ in range(N)]
for i in range(M) :
    hazure = 0
    for j in range(N) :
        if target[i] == yosou[i][j] :
            ten[j] += 1
        else :
            hazure += 1
    ten[target[i]-1] += hazure

for i in range(N) :
    print(ten[i])