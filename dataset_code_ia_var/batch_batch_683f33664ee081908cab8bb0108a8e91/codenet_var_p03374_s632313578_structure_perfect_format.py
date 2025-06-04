N, C = (int(i) for i in input().split())

X = [0]
V = [0]
for i in range(N):
    x, v = (int(i) for i in input().split())
    X.append(x)
    V.append(v)

l_cal = [0] * (N + 1)
r_cal = [0] * (N + 1)

l_cal[1] = V[1] - 2 * (X[1] - X[0])
r_cal[1] = V[-1] - 2 * (C - X[-1])

for i in range(2, N + 1):
    l_cal[i] = l_cal[i - 1] + V[i] - 2 * (X[i] - X[i - 1])
    r_cal[i] = r_cal[i - 1] + V[-i] - 2 * (X[-i + 1] - X[-i])

l_max = [0] * (N + 1)
r_max = [0] * (N + 1)

for i in range(1, N + 1):
    l_max[i] = max(l_max[i - 1], l_cal[i])
    r_max[i] = max(r_max[i - 1], r_cal[i])

l_ans = l_max[-1]
r_ans = r_max[-1]

for i in range(1, N + 1):
    l_ans = max(l_ans, l_max[-1 - i] + r_cal[i] + (C - X[-i]))
    r_ans = max(r_ans, r_max[-1 - i] + l_cal[i] + X[i])

print(max(l_ans, r_ans))