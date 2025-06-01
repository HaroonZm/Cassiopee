n = int(input())
lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))

a_start = []
a_end = []
h_start = []
h_end = []
b_start = []
b_end = []
for x in lst:
    a_start.append(x[0] * 60 + x[1])
    a_end.append(x[2] * 60 + x[3])
    h_start.append(x[4] * 60 + x[5])
    h_end.append(x[6] * 60 + x[7])
    b_start.append(x[8] * 60 + x[9])
    b_end.append(x[10] * 60 + x[11])

def make_sets(s, e):
    sets = []
    member = []
    i = 0
    while i < 1440:
        updated = False
        for j in range(n):
            if s[j] == i:
                member.append(j)
                updated = True
            if e[j] == i - 1:
                member.remove(j)
                updated = True
        if updated:
            sets.append(set(member))
        i += 1
    return sets

a_sets = make_sets(a_start, a_end)
h_sets = make_sets(h_start, h_end)
b_sets = make_sets(b_start, b_end)

ans = 0
for s1 in a_sets:
    for s2 in h_sets:
        for s3 in b_sets:
            intersection = s1.intersection(s2)
            intersection &= s3
            if len(intersection) > ans:
                ans = len(intersection)
print(ans)