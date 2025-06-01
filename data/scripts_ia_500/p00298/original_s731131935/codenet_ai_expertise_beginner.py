n = int(input())
c_lst = []
w_lst = []
for _ in range(n):
    c, w = map(int, input().split())
    c_lst.append(c)
    w_lst.append(w)

w_acc = [0]
for w in w_lst:
    w_acc.append(w_acc[-1] + w)

connect = []
for i in range(n):
    row = []
    for j in range(n):
        if i == j:
            row.append(True)
        else:
            row.append(None)
    connect.append(row)

def can_connect(left, right):
    if connect[left][right] is not None:
        return connect[left][right]
    left_condition = False
    right_condition = False
    if c_lst[left] >= w_acc[right + 1] - w_acc[left + 1]:
        left_condition = can_connect(left + 1, right)
    if c_lst[right] >= w_acc[right] - w_acc[left]:
        right_condition = can_connect(left, right - 1)
    connect[left][right] = left_condition or right_condition
    return connect[left][right]

for i in range(n):
    for j in range(i + 1, n):
        can_connect(i, j)

INF = 10 ** 20
dp = [INF] * (n + 1)
dp[0] = 0
for i in range(n):
    for j in range(i, n):
        if connect[i][j]:
            if dp[j + 1] > dp[i] + 1:
                dp[j + 1] = dp[i] + 1
        else:
            break

print(dp[n])