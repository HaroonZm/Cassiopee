from collections import defaultdict,deque

fact = [1 for i in range(1000001)]
fact[1] = 0
z = 2
while 1:
    j = 2
    while z*j < 1000001:
        fact[z*j] = 0
        j += 1
    for j in range(z+1,1000001):
        if fact[j]:
            z = j
            break
    else:
        break
d = defaultdict(lambda : None)
f = [None for i in range(1000001)]
x,y,di = 0,0,"d"
f[1] = (0,0)
d[(0,0)] = 1
for i in range(2,1000001):
    if di == "d":
        if d[(x+1,y)] == None:
            x += 1
            di = "r"
        else:
            y += 1
    elif di == "r":
        if d[(x,y-1)] == None:
            y -= 1
            di = "u"
        else:
            x += 1
    elif di == "u":
        if d[(x-1,y)] == None:
            x -= 1
            di = "l"
        else:
            y -= 1
    else:
        if d[(x,y+1)] == None:
            y += 1
            di = "d"
        else:
            x -= 1
    d[(x,y)] = i
    f[i] = (x,y)
v = [[] for i in range(1000001)]
for i in range(1,1000001):
    x,y = f[i]
    for j in range(-1,2):
        if d[(x+j,y+1)] != None:
            v[i].append(d[(x+j,y+1)])

while 1:
    m,n = map(int, input().split())
    if m == n == 0:
        break
    ans = [-1 for i in range(m+1)]
    q = deque()
    q.append(n)
    ans[n] = fact[n]
    while q:
        x = q.popleft()
        for y in v[x]:
            if y <= m:
                if ans[y] < 0:
                    ans[y] = ans[x]+fact[y]
                    q.append(y)
                else:
                    if ans[x]+fact[y] > ans[y]:
                        ans[y] = ans[x]+fact[y]
    ma = max(ans)
    if ma == 0:
        print(0,0)
    else:
        for i in range(m+1)[::-1]:
            if fact[i]:
                if ans[i] == ma :
                    k = i
                    break
        print(ma, k)