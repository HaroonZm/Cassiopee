n, k = map(int, input().split())
h = list(map(int, input().split()))
h.sort()
i = 0
while i < n:
    if h[i] >= k:
        print(n - i)
        exit()
    i += 1
print(0)