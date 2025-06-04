from operator import floordiv as ff

parse = lambda: [*map(int, input().split())]
r = parse()
N, M = r[0], r[1]

A = min(N, ff(M,2)) if N >= ff(M,2) else N + ff(M-2*N,4)
print(A)