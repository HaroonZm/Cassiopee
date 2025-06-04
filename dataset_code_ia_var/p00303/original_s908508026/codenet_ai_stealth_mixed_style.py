n = int(input())
g = [list() for _ in range(200)]
u, used, hold = [0]*200, [0]*200, [0]*200

for k in range(n):
    t = input().split()
    a = int(t[0])-1
    b = int(t[2])-1
    u[a] = 1
    u[b+100] = 1
    if t[1] == 'lock':
        g[a] += [b+100]
    else:
        g[b+100].extend([a])

def f(x):
    if used[x]: return False
    hold[x]=True
    res = False
    for y in g[x]:
        if hold[y]: 
            res = True
            continue
        res = res or f(y)
    hold[x]=False
    used[x]=1
    return res

def check():
    y=0
    i=0
    while i<200:
        if u[i]:
            if f(i):
                print(1)
                y=1
                break
        i+=1
    if y==0:
        print(0)
check()