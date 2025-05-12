def solve(A, b):
    for i in xrange(3):
        if A[i][i] == 0.0:
            for j in xrange(i+1, 3):
                if A[j][i]!=0.0:
                    A[i], A[j] = A[j], A[i]
                    b[i], b[j] = b[j], b[i]
                    break
        for j in xrange(3):
            if i==j:
                continue
            a = A[j][i] / A[i][i]
            for k in xrange(3):
                A[j][k] -= a * A[i][k]
            b[j] -= a * b[i]
    for i in xrange(3):
        b[i] /= A[i][i]
        A[i][i] = 1.0

u = map(float, raw_input().split())
e = map(float, raw_input().split())
o = map(float, raw_input().split())
p = map(float, raw_input().split())
q = map(float, raw_input().split())

n = [(p[i-2]-o[i-2])*(q[i-1]-o[i-1])-(p[i-1]-o[i-1])*(q[i-2]-o[i-2]) for i in xrange(3)]
v = [e[i]-u[i] for i in xrange(3)]
if sum(n[i]*v[i] for i in xrange(3))==0.0:
    print "HIT"
    exit(0)

A = [[p[i]-o[i], q[i]-o[i], e[i]-u[i]] for i in xrange(3)]
b = [e[i] - o[i] for i in xrange(3)]
solve(A, b)
s, t, x = b
j = lambda x: -0.0000001 < x < 1.0000001
if j(s) and j(t) and j(s+t) and j(x):
    print "MISS"
else:
    print "HIT"