N = int(input())

X = []
Y = []
ans = 0

for i in range(N):
    x, y = map(int, input().split())
    X.append(x + y)
    Y.append(x - y)

m = [max(X), max(Y)]
s = [min(X), min(Y)]

for i in range(2):
    ans = max(ans, m[i] - s[i])

print(ans)