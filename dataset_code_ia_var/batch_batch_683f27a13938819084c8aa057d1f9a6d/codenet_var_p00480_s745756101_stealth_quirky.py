n = int(input())
A = [int(x) for x in input().split()]
_ = [[False]*21 for _ in [None]*~n]
_[0][A[0]] = True
m, o, p = 1, n-1, 21
while m < o:
    (lambda q, r, s:
        [(_.__setitem__(m, [_(m-1)[j+A[m]] if j+A[m]<s else False or
                              _(m-1)[j-A[m]] if j-A[m]>=0 else False
                              for j in range(s)])) for m in [q]])(m, o, p)
    m += 1
print(_[o-1][A[o]])