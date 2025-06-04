n, k = map(int, input().split())
h = list(map(int, input().split()))

h.sort()
for i in range(n):
    if h[i] >= k:
        print(n - i)
        exit()
print(0)