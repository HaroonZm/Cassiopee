import sys
n = int(sys.stdin.readline())
p1 = [[int(x) for x in sys.stdin.readline().split()] for i in range(n)]
p1.insert(0,[0,0])
p1.append([1000,0])
m = int(sys.stdin.readline())
p2 = [[int(x) for x in sys.stdin.readline().split()] for i in range(m)]
p2.insert(0,[0,1000])
p2.append([1000,1000])
ans = float("inf")
for x1,y1 in p1:
    for x2,y2 in p2:
        r = (x1-x2)**2+(y1-y2)**2
        if r < ans:
            ans = r
for x,y in p1:
    for i in range(m+1):
        p,q = p2[i]
        s,t = p2[i+1]
        a = t-q
        b = p-s
        if (b*(s-x)-a*(t-y))*(b*(p-x)-a*(q-y)) < 0:
            c = -a*p-b*q
            d = (a*x+b*y+c)**2
            d /= (a**2+b**2)
            if d < ans:
                ans = d

for x,y in p2:
    for i in range(n+1):
        p,q = p1[i]
        s,t = p1[i+1]
        a = t-q
        b = p-s
        if (b*(s-x)-a*(t-y))*(b*(p-x)-a*(q-y)) < 0:
            c = -a*p-b*q
            d = (a*x+b*y+c)**2
            d /= (a**2+b**2)
            if d < ans:
                ans = d

print(ans**0.5)