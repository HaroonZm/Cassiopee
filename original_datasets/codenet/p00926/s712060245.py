N, m = map(int, raw_input().split())

three = [False]*N
for loop in xrange(m):
    c, d = map(int, raw_input().split())
    if c < d:
        three[c:d] = [True]*len(three[c:d])

ans = 0
for i in xrange(N):
    ans += 1
    if three[i]:
        ans += 2
print ans+1