n = int(input())
a = list(map(int, input().split()))
f = 1
i = 0
while i < n:
    if a[i] > 0:
        f = 0
    i += 1
if f == 1:
    mx = a[0]
    ind = 0
    i = 1
    while i < n:
        if a[i] > mx:
            mx = a[i]
            ind = i
        i += 1
    print(mx)
    reslist = []
    i = n
    while i > ind + 1:
        reslist.append(i)
        i -= 1
    i = 0
    while i < ind:
        reslist.append(1)
        i += 1
    print(len(reslist))
    i = 0
    while i < len(reslist):
        print(reslist[i])
        i += 1
    exit()
g1 = []
g2 = []
i = 1
while i < n:
    g1.append(a[i])
    i += 2
i = 0
while i < n:
    g2.append(a[i])
    i += 2
ans1 = 0
ans2 = 0
l1 = []
l2 = []
i = 0
while i < len(g1):
    if g1[i] > 0:
        ans1 += g1[i]
        l1.append(i * 2 + 2)
    i += 1
i = 0
while i < len(g2):
    if g2[i] > 0:
        ans2 += g2[i]
        l2.append(i * 2 + 1)
    i += 1
length = n
if ans1 >= ans2:
    print(ans1)
    reslist = []
    i = n
    while i > l1[-1]:
        reslist.append(i)
        i -= 1
    length -= (n - l1[-1])
    i = l1[-1]
    while i > l1[0]:
        if i not in l1:
            reslist.append(i)
            length -= 2
        i -= 2
    i = 0
    while i < l1[0] - 1:
        reslist.append(1)
        i += 1
    length -= l1[0]
    i = length
    while i > 0:
        reslist.append(2)
        i -= 2
    print(len(reslist))
    i = 0
    while i < len(reslist):
        print(reslist[i])
        i += 1
else:
    print(ans2)
    reslist = []
    i = n
    while i > l2[-1]:
        reslist.append(i)
        i -= 1
    length -= (n - l2[-1])
    i = l2[-1]
    while i > l2[0]:
        if i not in l2:
            reslist.append(i)
            length -= 2
        i -= 2
    i = 0
    while i < l2[0] - 1:
        reslist.append(1)
        i += 1
    length -= l2[0]
    i = length
    while i > 0:
        reslist.append(2)
        i -= 2
    print(len(reslist))
    i = 0
    while i < len(reslist):
        print(reslist[i])
        i += 1