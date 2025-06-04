n, k = map(int, input().split())
h = list(map(int, input().split()))
cnt = 0
i = 0
while i < n:
    if h[i] >= k:
        cnt = cnt + 1
    i = i + 1
print(cnt)