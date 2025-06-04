n = int(input())
s0 = []
i = 0
while i < n:
    s0.append(list(str(input())))
    i += 1
s1 = []
i = 0
while i < n:
    s1 += s0[i]
    i += 1
s2 = list(set(s1))
s2.sort()
t = []
i = 0
while i < len(s2):
    r = []
    j = 0
    while j < n:
        r.append(s0[j].count(s2[i]))
        j += 1
    t.append(min(r))
    i += 1
p = ""
i = 0
while i < len(s2):
    p += s2[i] * t[i]
    i += 1
print(p)