N = int(input())
src = []
i = 0
while i < N:
    parts = input().split()
    src.append((int(parts[0]), int(parts[1])))
    i += 1

cum_r = [src[0][1]]
i = 0
while i < N-1:
    x1, s1 = src[i]
    x2, s2 = src[i+1]
    gain = s2 - (x2 - x1)
    cum_r.append(cum_r[-1] + gain)
    i += 1

best_l = [0]
i = 1
while i < N:
    x, s = src[i]
    c = cum_r[i]
    last = best_l[-1]
    val = s - c
    if val > last:
        best_l.append(val)
    else:
        best_l.append(last)
    i += 1

ans = 0
i = 0
while i < N:
    l = best_l[i]
    r = cum_r[i]
    if l+r > ans:
        ans = l+r
    i += 1
print(ans)