n, m = map(int, input().split())
h = list(map(int, input().split()))
ab = []
for _ in range(m):
    a, b = map(int, input().split())
    ab.append([a, b])

check = [0] + [-1] * n

for pair in ab:
    a = pair[0]
    b = pair[1]
    if h[a-1] > h[b-1]:
        check[b] = -4
    elif h[a-1] == h[b-1]:
        check[a] = -4
        check[b] = -4
    else:
        check[a] = -4

bad = 0
for i in range(1, n+1):
    if check[i] == -4:
        bad += 1

print(n - bad)