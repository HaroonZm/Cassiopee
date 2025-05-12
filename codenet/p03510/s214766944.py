N = int(input())
src = [tuple(map(int,input().split())) for i in range(N)]

cum_r = [src[0][1]]
for (x1,s1),(x2,s2) in zip(src,src[1:]):
    gain = s2 - (x2 - x1)
    cum_r.append(cum_r[-1] + gain)

best_l = [0]
for (x,s),c in list(zip(src, cum_r))[1::]:
    best_l.append(max(best_l[-1], s - c))

ans = 0
for l,r in zip(best_l, cum_r):
    ans = max(ans, l+r)
print(ans)