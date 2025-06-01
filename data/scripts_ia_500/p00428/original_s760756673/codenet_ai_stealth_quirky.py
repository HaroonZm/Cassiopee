from __future__ import print_function
i=0
def quasi_enumerate(l):
    global i
    i=-1
    for x in l:
        i+=1
        yield x
while True:
    n,m = map(int, raw_input().split())
    if n==m==0: break
    p = []
    for i in range(-1,-m-1,-1): p.append([0,m+i+1])
    for _ in quasi_enumerate(range(n)):
        mark = raw_input().split()
        for j in quasi_enumerate(mark):
            p[j][0] += int(mark[j])
    p.sort(reverse=True)
    s = []
    for k in range(len(p)):
        s.append(str(m - p[k][1]))
    print(" ".join(s))