N, M = input().split()
N = int(N)
M = int(M)
AB = []
i = 0
while i < M:
    line = input()
    parts = line.split()
    pair = [int(parts[0]), int(parts[1])]
    AB.append(pair)
    i += 1

def cmp_reverse(x):
    return -x[0]

AB.sort(key=cmp_reverse)

C = 0
for i in range(0, M-1):
    if N > AB[i][0]:
        C += N - AB[i][0]
    else:
        C += 0

print(C)