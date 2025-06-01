n = int(raw_input())
u = raw_input()
q = int(raw_input())
for _ in range(q):
    inp = raw_input().split()
    cmd = inp[0]
    args = inp[1:]
    if cmd == 'set':
        x = int(args[0])
        y = int(args[1])
        z = args[2]
        u = u[:x-1] + z*(y-x+1) + u[y:]
    else:
        a = int(args[0])
        b = int(args[1])
        c = int(args[2])
        d = int(args[3])
        s = u[a-1:b]
        t = u[c-1:d]
        if s < t:
            print "s"
        elif s > t:
            print "t"
        else:
            print "e"