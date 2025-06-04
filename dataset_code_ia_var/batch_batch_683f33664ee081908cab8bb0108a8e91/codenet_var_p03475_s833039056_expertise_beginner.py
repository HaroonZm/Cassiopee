N = int(input())
C = []
S = []
F = []

for i in range(N - 1):
    line = input().split()
    C.append(int(line[0]))
    S.append(int(line[1]))
    F.append(int(line[2]))

def calc_time(idx, current_time):
    if current_time <= S[idx]:
        dep_time = S[idx]
    else:
        wait = 0
        if (current_time - S[idx]) % F[idx] == 0:
            wait = 0
        else:
            wait = F[idx] - (current_time - S[idx]) % F[idx]
        dep_time = current_time + wait
    return dep_time + C[idx]

for i in range(N - 1):
    t = 0
    for j in range(i, N - 1):
        t = calc_time(j, t)
    print(t)

print(0)