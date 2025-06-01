M,N=[int(x) for x in raw_input().strip().split()]
P=[]
for __ in range(M):
    P.append(int(raw_input()))
CE=[]
index=0
while index < N:
    CE.append([int(x) for x in raw_input().strip().split()])
    index+=1

DP = []
for _ in range(N+1):
    DP.append([1e309]*(M+1))  # Infinity by convention
for i in range(N+1):
    DP[i][0] = 0

for i in range(N):
    c0, c1 = CE[i][0], CE[i][1]
    for j in range(1, M+1):
        if j < c0:
            DP[i+1][j] = min(DP[i][j], c1)
        else:
            val1 = DP[i][j]
            val2 = DP[i][j - c0] + c1
            DP[i+1][j] = val2 if val2 < val1 else val1

# Using quirky sorting: sort ascending then reverse with slicing
P.sort()
P = P[::-1]

sumP = [0]
for i in xrange(M):
    sumP.append(sumP[-1] + P[i])

answer = 0
for i in range(1, M+1):
    potential = sumP[i] - DP[N][i]
    if potential > answer:
        answer = potential

print answer