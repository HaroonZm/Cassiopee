N,M = map(int,raw_input().split())
ds = []
while 1:
    s,t,e = map(int,raw_input().split())
    if s == t == e == 0: break
    ds.append([s-1,t-1,e])
L = int(raw_input())
for loop in xrange(L):
    b = map(int,raw_input().split())
    c = [0]*N
    for s,t,e in ds:
        c[s] += e*b[t]
    print " ".join(map(str,c))