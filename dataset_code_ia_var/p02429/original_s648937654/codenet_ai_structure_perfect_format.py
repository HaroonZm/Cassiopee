import itertools

n = int(input())
tlist = list(map(int, input().split()))
k = tlist[0]
tlist.remove(tlist[0])

if k == 0:
    print("0:")
    exit()

combslist = []
for i in range(1, k + 1):
    combs = list(itertools.combinations(tlist, i))
    for comb in combs:
        combslist.append(comb)

sumlist = []
for comb in combslist:
    s = 0
    for c in comb:
        s += pow(2, c)
    sumlist.append(s)

z = zip(sumlist, combslist)
z = sorted(z)

sumlist, combslist = zip(*z)

print("0:")
for s, comb in zip(sumlist, combslist):
    c_str = ' '.join(str(c) for c in comb)
    print(str(s) + ": " + c_str)