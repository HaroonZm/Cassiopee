N = int(input())
A = list(map(int, [input() for _ in range(5)]))
small=lambda l:sorted(l)[0]
x=small(A)
q,r=divmod(N,x)
out=[q+4,q+5][bool(r)]
print(out)