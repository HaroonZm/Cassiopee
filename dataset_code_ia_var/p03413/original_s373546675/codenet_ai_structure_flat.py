import sys
N = int(input())
a = []
tmp = input().split()
for i in range(N):
    a.append((int(tmp[i]), i))
ao = 0
ae = 0
for v, i in a:
    if i % 2 and v > 0:
        ao += v
    if not i % 2 and v > 0:
        ae += v
if ao < ae:
    use_even = True
else:
    use_even = False
if max(ao, ae) == 0:
    maxv = a[0]
    idx = 0
    for j in range(N):
        if a[j][0] > maxv[0]:
            maxv = a[j]
            idx = j
    Ans = []
    for ii in range(idx):
        Ans.append(1)
    for k in range(N - idx, 0, -1):
        Ans.append(k)
    print(maxv[0])
    print(len(Ans))
    for t in Ans:
        print(t)
    sys.exit()
if not use_even:
    print(ao)
    yn = []
    for v, i in a:
        if i % 2 and v > 0:
            yn.append(i)
else:
    print(ae)
    yn = []
    for v, i in a:
        if not i % 2 and v > 0:
            yn.append(i)
listyn = []
for i in range(N):
    if i in yn:
        listyn.append(True)
    else:
        listyn.append(False)
Ans = []
while not listyn[0]:
    Ans.append(1)
    listyn = listyn[1:]
while not listyn[-1]:
    Ans.append(len(listyn))
    listyn = listyn[:-1]
while True:
    if len(listyn) == 1:
        break
    if len(listyn) == 2 or len(listyn) == 3:
        Ans.append(2)
        break
    if listyn[2]:
        Ans.append(2)
        listyn = [True] + listyn[3:]
    else:
        Ans.append(3)
        listyn = [True, False] + listyn[4:]
print(len(Ans))
for i in Ans:
    print(i)