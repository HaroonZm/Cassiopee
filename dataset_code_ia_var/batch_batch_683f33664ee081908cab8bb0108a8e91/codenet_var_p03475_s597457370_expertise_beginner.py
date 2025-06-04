N = int(input())
li = []
for i in range(N-1):
    c, s, f = map(int, input().split())
    li.append((c, s, f))

for i in range(N):
    t = 0
    for j in range(i, N-1):
        c, s, f = li[j]
        if t < s:
            t = s + c
        else:
            if (t - s) % f == 0:
                t += c
            else:
                t += (f - (t - s) % f) + c
    print(t)