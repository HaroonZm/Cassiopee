n = int(input())
if n == 1:
    print('! 1')
    exit()
elif n == 2:
    print('! 1 2')
    exit()

print('? 1 2')
m = int(input())
d = []

for i in range(3,n+1):
    print('? 1',i)
    p = int(input())
    print('? 2',i)
    q = int(input())
    d.append((p+q,p,q,i))

d = sorted(d)[::-1]
left = []
right = []
i = 0

flag = True
for i in range(len(d)):
    p = d[i][1]
    q = d[i][2]
    j = d[i][3]
    if d[i][0] <= m:
        if flag:
            right.append(2)
            flag = False
        right.append(j)
        continue
    if q > p:
        left.append(j)
    else:
        right.append(j)
if flag:
    right.append(2)

ans = left + [1] + right[::-1]

print('!',' '.join([str(u) for u in ans]))