n, m = map(int, raw_input().split())
ans = 0
for i in xrange(n):
    A = map(int, raw_input().split())
    if i: A = [e^1 for e in A]
    ans += max(max(A[0]+A[-1] + sum(A[k]^1^(k==j) for k in xrange(1, m-1)) for j in xrange(1, m-1)) if m>2 else 0, max(A[0] + sum(e^1 for e in A[1:]), A[-1] + sum(e^1 for e in A[:-1])))
print ans