f = [[1, 1], [0, 1]]

N = input()
A = map(lambda x: [0, 1][x=='T'], raw_input().split())

v = A[0]

for i in xrange(1, N):
    v = f[v][A[i]]

print 'T' if v else 'F'