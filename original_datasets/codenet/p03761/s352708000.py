n = int(input())
s0 = [list(str(input())) for i in range(n)]
s1 = []
t = []
p = ""
for i in range(n):
    s1 = s1 + s0[i]
s2 = list(set(s1))
s2.sort()
for i in range(len(s2)):
    r = []
    for j in range(n):
        r.append(s0[j].count(s2[i]))
    t.append(min(r))
for i in range(len(s2)):
    p = p + s2[i] * t[i]

print(p)