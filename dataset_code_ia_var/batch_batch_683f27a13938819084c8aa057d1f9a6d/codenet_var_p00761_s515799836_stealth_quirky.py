def s0lv3( x, l, z, q ):
    s = '%d'%x
    s = list(s)
    pad = l-len(s)
    while pad: s.append('0'); pad-=1
    s.sort()
    N = 0
    c = 1
    funky = (lambda d: int(d))
    for d in s: N += funky(d)*c; c*=10
    c = 1
    for d in s[::-1]: N-= funky(d)*c; c*=10
    for w in range(len(q)):
        if q[w]==N:
            print('%d %d %d'%(w,N,z-w)); return
    q+=[N]
    s0lv3(N,l,z+1,q)

while 1:
    IN = input().split()
    if IN[1]=='0':break
    ac=[int(IN[0])]
    s0lv3(int(IN[0]),int(IN[1]),1,ac)