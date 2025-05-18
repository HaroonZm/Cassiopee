n = int(input())
h = list(map(int, input().split()))

cnt = 0
cache = 0
last = h[0]
for x in h[1:]:
    if last >= x:
        cnt += 1
    else:
        cnt = 0
    if cache < cnt:
        cache = cnt
    last = x

print(cache)