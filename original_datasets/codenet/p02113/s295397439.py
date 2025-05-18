from functools import cmp_to_key
n, l = map(int, input().split())
ss = {}
for i in range(n):
    s = input()
    ss[s] = ss.get(s, 0) + 1
ans = ""
ma = ""
for s in sorted(ss):
    if s[::-1] == s:
        ans += s * (ss[s]//2)
        ss[s] -= 2*(ss[s]//2)
        if ss[s] > 0 and len(ma) < len(s):
            ma = s
    else:
        rev = s[::-1]
        if rev in ss:
            cnt = min(ss[s], ss[rev])
            ans += s * cnt
            ss[s] -= cnt
            ss[rev] -= cnt
print(ans + ma + ans[::-1])