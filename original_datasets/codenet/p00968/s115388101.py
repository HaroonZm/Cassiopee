n = int(input())
ss = [input() for _ in range(n + 1)]
sp = [[s[0]] for s in ss]
for i, s in enumerate(ss):
    for j in range(1, len(s)):
        if s[j - 1].isdigit() != s[j].isdigit():
            sp[i].append('')
        sp[i][-1] += s[j]
s0 = sp[0]
for s in sp[1:]:
    p = 0
    m = min(len(s0), len(s))
    while p < m and s0[p] == s[p]:
        p += 1
    if p == m:
        print('-+'[len(s0) <= len(s)])
        continue
    a = s0[p].isdigit()
    b = s[p].isdigit()
    if a and b:
        print('-+'[int(s0[p]) <= int(s[p])])
    elif a or b:
        print('-+'[a])
    else:
        print('-+'[s0[p] <= s[p]])