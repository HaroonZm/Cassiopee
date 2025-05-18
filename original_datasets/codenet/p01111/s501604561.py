#2005_c
"""
n = int(input())
k = list("mcxi")
for i in range(n):
    d = {"m":0,"c":0,"x":0,"i":0}
    a,b  = input().split()
    a = list(a)
    b = list(b)
    a.insert(0,1)
    b.insert(0,1)
    for j in range(1,len(a)):
        if a[j] in k:
            if a[j-1] in k:
                d[a[j]] += 1
            else:
                d[a[j]] += int(a[j-1])
    for j in range(1,len(b))[::-1]:
        if b[j] in k:
            if b[j-1] in k:
                d[b[j]] += 1
            else:
                d[b[j]] += int(b[j-1])
            if d[b[j]] >= 10:
                l = b[j]
                while d[l] >= 10:
                    d[l] -= 10
                    l = k[k.index(l)-1]
                    d[l] += 1
    for j in k:
        if d[j]:
            if d[j] == 1:
                print(j,end = "")
            else:
                print(str(d[j])+j,end = "")
    print()
"""

#2017_c
"""
while 1:
    h, w = map(int, input().split())
    if h == w == 0:
        break
    s = [list(map(int, input().split())) for i in range(h)]

    ans = 0
    for u in range(h):
        for d in range(u+2,h):
            for l in range(w):
                for r in range(l+2,w):
                    m = float("inf")
                    for i in range(u,d+1):
                        m = min(m,s[i][l],s[i][r])
                    for i in range(l,r+1):
                        m = min(m,s[u][i],s[d][i])
                    f = 1
                    su = 0
                    for i in range(u+1,d):
                        for j in range(l+1,r):
                            su += (m-s[i][j])
                            if s[i][j] >= m:
                                f = 0
                                break
                        if not f:
                            break
                    if f:
                        ans = max(ans,su)
    print(ans)
"""

#2016_c
"""
while 1:
    m,n = map(int, input().split())
    if m == n == 0:
        break
    d = {}
    ma = 7368791
    for i in range(m,ma+1):
        d[i] = 1
    z = m
    for i in range(n):
        for j in range(z,ma+1):
            if d[j]:
                z = j
                break
        j = 1
        while z*j <= ma:
            d[z*j] = 0
            j += 1
    for j in range(z,ma+1):
        if d[j]:
            print(j)
            break
"""

#2018_c
def factorize(n):
    if n < 4:
        return [1,n]
    i = 2
    l = [1]
    while i**2 <= n:
        if n%i == 0:
            l.append(i)
            if n//i != i:
                l.append(n//i)
        i += 1
    l.append(n)
    l.sort()
    return l
while 1:
    b = int(input())
    if b == 0:
        break
    f = factorize(2*b)
    for n in f[::-1]:
        a = 1-n+(2*b)//n
        if a >= 1 and a%2 == 0:
            print(a//2,n)
            break