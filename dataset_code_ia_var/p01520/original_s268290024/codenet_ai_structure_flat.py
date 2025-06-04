n, t, e = map(int, input().split())
watch = list(map(int, input().split()))
ans = False
w = 0
while w < n:
    i = 0
    while i <= e:
        if (t + i) % watch[w] == 0:
            ans = True
            break
        if (t - i) % watch[w] == 0:
            ans = True
            break
        i += 1
    if ans:
        break
    w += 1
if ans:
    print(w + 1)
else:
    print(-1)