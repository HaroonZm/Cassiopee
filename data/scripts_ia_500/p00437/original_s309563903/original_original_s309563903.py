while True:
    i,j,k = map(int, raw_input().split())
    if i==0 and j==0 and k==0: break
    n = i+j+k
    s = []
    a = set(range(n))
    b = set()
    c = set()
    for i in range(input()):
        x, y, z, r = map(int, raw_input().split())
        x-=1;y-=1;z-=1;
        if r==0: s.append(set([x,y,z]))
        else:
            c.add(x);c.add(y);c.add(z);
    while True:
        f = True
        for lst in s:
            if len(lst & c) >=2:
                s.remove(lst)
                lst = lst - c
                if len(lst)>=1: b.add(lst.pop())
                f = False
        if f : break
    a = a - b; a = a - c;
    for i in range(n):
        if i in a: print 2
        elif i in b: print 0
        else: print 1