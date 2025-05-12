# input
n = int(input())
A = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    u, k, *v_list = list(map(int, input().split()))
    for v in v_list:
        A[u-1][v-1] = 1

# init
d = [0] * n
f = [0] * n
t = 0

# recursive
def dfs(u):
    global t
    t += 1
    d[u] = t
    for v in range(n):
        if A[u][v] == 1 and d[v] == 0:
            dfs(v)
    t += 1
    f[u] = t

# dfs
for i in range(n):
    if d[i] == 0:
        dfs(i)

# output
for i in range(n):
    print(i+1, d[i], f[i])