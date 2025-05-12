n = int(raw_input())
for i in range(n):
    s = raw_input()
    l = set([s])
    for k in range(len(s)-1):
        t1 = s[:k+1]
        t2 = s[k+1:]
        n1 = t1 + t2[::-1]
        n2 = t1[::-1] + t2
        n3 = t1[::-1] + t2[::-1]
        n4 = t2 + t1[::-1]
        n5 = t2[::-1] + t1
        n6 = t2[::-1] + t1[::-1]
        n7 = t2 + t1
        l2 = set([n1,n2,n3,n4,n5,n6,n7])
        l = l.union(l2)
    print len(l)