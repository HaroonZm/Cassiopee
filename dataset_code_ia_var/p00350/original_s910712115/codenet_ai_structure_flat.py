n = int(raw_input())
u = raw_input()
qn = int(raw_input())

for _ in range(qn):
    qq = raw_input().split()
    cmd = qq[0]
    del qq[0]
    if cmd == 'comp':
        a = int(qq[0])
        b = int(qq[1])
        c = int(qq[2])
        d = int(qq[3])
        s = u[a-1:b]
        t = u[c-1:d]
        if s < t:
            print "s"
        elif s > t:
            print "t"
        else:
            print "e"
    elif cmd == 'set':
        x = int(qq[0])
        y = int(qq[1])
        z = qq[2]
        h = u[:x-1]
        t = u[y:]
        zz = z*(y-x+1)
        u = h+zz+t