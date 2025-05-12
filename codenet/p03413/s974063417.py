n = int(input())
a = list(map(int,input().split()))
f = 1
for i in range(n):
    if a[i]>0:
        f = 0
if f:
    ind = a.index(max(a))
    print(max(a))
    list = []
    for i in range(n,ind+1,-1):
        list.append(i)
    for _ in range(ind):
        list.append(1)
    print(len(list))
    for i in list:
        print(i)
    exit()
g1 = a[1::2]
g2 = a[::2]
ans1,ans2 = 0,0
l1,l2 = [],[]
for i in range(len(g1)):
    if g1[i]>0:
        ans1 += g1[i]
        l1.append(i*2+2)
for i in range(len(g2)):
    if g2[i]>0:
        ans2 += g2[i]
        l2.append(i*2+1)
length = n
if ans1>=ans2:
    print(ans1)
    list = []
    for i in range(n,l1[-1],-1):
        list.append(i)
    length -= n-l1[-1]
    for i in range(l1[-1],l1[0],-2):
        if not i in l1:
            list.append(i)
            length -= 2
    for i in range(l1[0]-1):
        list.append(1)
    length -= l1[0]
    for _ in range(length,0,-2):
        list.append(2)
    print(len(list))
    for i in list:
        print(i)
else:
    print(ans2)
    list = []
    for i in range(n,l2[-1],-1):
        list.append(i)
    length -= n-l2[-1]
    for i in range(l2[-1],l2[0],-2):
        if not i in l2:
            list.append(i)
            length -= 2
    for i in range(l2[0]-1):
        list.append(1)
    length -= l2[0]
    for _ in range(length,0,-2):
        list.append(2)
    print(len(list))
    for i in list:
        print(i)