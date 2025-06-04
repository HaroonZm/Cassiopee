N, W, H = map(int, input().split())

parents = []
for i in range(N):
    parents.append(i)

def find_root(x):
    if x == parents[x]:
        return x
    parents[x] = find_root(parents[x])
    return parents[x]

def union(x, y):
    px = find_root(x)
    py = find_root(y)
    if px < py:
        parents[py] = px
    else:
        parents[px] = py

X_dict = {}
Y_dict = {}

for i in range(N):
    x, y = map(int, input().split())
    if x not in X_dict:
        X_dict[x] = []
    if y not in Y_dict:
        Y_dict[y] = []
    X_dict[x].append(i)
    Y_dict[y].append(i)

for x in X_dict:
    idx_list = X_dict[x]
    for j in range(len(idx_list) - 1):
        union(idx_list[j], idx_list[j+1])

for y in Y_dict:
    idx_list = Y_dict[y]
    for j in range(len(idx_list) - 1):
        union(idx_list[j], idx_list[j+1])

count = 0
for i in range(N):
    if find_root(i) == i:
        count += 1

ans = N - count + 2 * (count - 1)

if count > 1 and 1 not in X_dict and W not in X_dict and 1 not in Y_dict and H not in Y_dict:
    ans += 1

print(ans)