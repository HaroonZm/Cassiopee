N = int(input())
S = input()
E = [0] * N
W = [0] * N
i = 0
while i < N:
    if S[i] == "E":
        E[i] += 1
    else:
        W[i] += 1
    i += 1
i = 1
while i < N:
    E[i] = E[i-1] + E[i]
    i += 1
i = N - 2
while i >= 0:
    W[i] = W[i+1] + W[i]
    i -= 1
SUM = []
i = 0
while i < N:
    SUM.append(E[i] + W[i])
    i += 1
m = SUM[0]
i = 1
while i < N:
    if SUM[i] > m:
        m = SUM[i]
    i += 1
print(N - m)