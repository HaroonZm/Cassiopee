n = int(input())
s = list(input())
l = s[:n]
r = s[n:][::-1]
d = {}
e = {}
i = 0
while i < (1 << n):
    s1 = ''
    t = ''
    u = ''
    v = ''
    j = 0
    while j < n:
        if (i >> j) & 1:
            s1 += l[j]
            t += r[j]
        else:
            u += l[j]
            v += r[j]
        j += 1
    key1 = (s1, u)
    key2 = (t, v)
    if key1 in d:
        d[key1] += 1
    else:
        d[key1] = 1
    if key2 in e:
        e[key2] += 1
    else:
        e[key2] = 1
    i += 1
a = 0
for k in d:
    if k in e:
        a += d[k] * e[k]
print(a)