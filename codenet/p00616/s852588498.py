def hole(query,n):
    dir=query[0]
    [a,b]=[int(x)-1 for x in query[1:]]
    if dir=="xy":
        ret=[b*n+a+z*n**2 for z in range(n)]
    elif dir=="xz":
        ret=[n**2*b+a+y*n for y in range(n)]
    else:
        ret=[n**2*b+a*n+x for x in range(n)]
    return ret

while(1):
    [n,h]=[int(x) for x in raw_input().split()]
    if n==0:
        break
    else:
        bad=[]
        for i in range(h):
            query=raw_input().split()
            bad+=hole(query,n)
        hset=set(bad)
        print n**3-len(hset)