n = int(raw_input())
S = [raw_input() for i in xrange(n)]
cnt = [10**9]*28
for s in S:
    for i in xrange(27):
        cnt[i] = min(cnt[i], s.count(chr(ord("a") + i)))
for i in xrange(27):
    cnt[i] = cnt[i] if cnt[i] < 10**9 else 0
ans = ""
for i in xrange(27):
    ans += chr(ord("a") + i)*cnt[i]
print ans