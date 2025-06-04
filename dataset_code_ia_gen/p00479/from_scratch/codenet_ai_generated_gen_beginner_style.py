N = int(input())
K = int(input())
colors = [1, 2, 3]

for _ in range(K):
    a, b = map(int, input().split())
    layer = min(a - 1, b - 1, N - a, N - b)
    c = colors[layer % 3]
    print(c)