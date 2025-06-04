import math

primes=[2]
top=2
nlist=[2*x-1 for x in range(2,500)]
while top<math.sqrt(500):
    top=nlist[0]
    primes.append(top)
    newnlist=[]
    for i in nlist:
        if i%top!=0:
            newnlist.append(i)
    nlist=newnlist
primes=primes+nlist

def getpoints(a):
    primelist=[]
    while a>1:
        primeflag=0
        for p in primes:
            if a%p==0:
                primeflag=1
                a=a/p
                if p not in primelist:
                    primelist.append(p)
                break
        if primeflag==0:
            primelist.append(a)
            a=1
    psorted=sorted(primelist)
    pts=primelist[-1]-sum(psorted[:-1])
    return pts

while 1:
    [a,b]=[int(x) for x in raw_input().split()]
    if a==0:
        break
    else:
        pta=getpoints(a)
        ptb=getpoints(b)
        if pta>ptb:
            print 'a'
        else:
            print 'b'