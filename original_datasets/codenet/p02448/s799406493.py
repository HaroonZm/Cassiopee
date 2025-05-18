readline = open(0).readline

N = int(readline())
P = [readline().split() for i in range(N)]

P = [(int(v), int(w), t, int(d), s) for v, w, t, d, s in P]
P.sort()

open(1, 'w').writelines(["%d %d %s %d %s\n" % e for e in P])