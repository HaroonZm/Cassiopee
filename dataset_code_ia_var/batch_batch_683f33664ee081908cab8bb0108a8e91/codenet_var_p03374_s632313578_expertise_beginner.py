n_c = input().split()
N = int(n_c[0])
C = int(n_c[1])

X = [0]
V = [0]
for i in range(N):
    xv = input().split()
    x = int(xv[0])
    v = int(xv[1])
    X.append(x)
    V.append(v)

l_cal = [0] * (N + 1)
r_cal = [0] * (N + 1)
l_cal[1] = V[1] - 2 * (X[1] - X[0])
r_cal[1] = V[N] - 2 * (C - X[N])
for i in range(2, N+1):
    l_cal[i] = l_cal[i-1] + V[i] - 2 * (X[i] - X[i-1])
    r_cal[i] = r_cal[i-1] + V[N-i+1] - 2 * (X[N-i+2] - X[N-i+1])

l_max = [0] * (N + 1)
r_max = [0] * (N + 1)
for i in range(1, N+1):
    l_max[i] = max(l_max[i-1], l_cal[i])
    r_max[i] = max(r_max[i-1], r_cal[i])

l_ans = l_max[N]
r_ans = r_max[N]
for i in range(1, N+1):
    l_ans = max(l_ans, l_max[N-i] + r_cal[i] + (C - X[N-i+1]))
    r_ans = max(r_ans, r_max[N-i] + l_cal[i] + X[i])
print(max(l_ans, r_ans))