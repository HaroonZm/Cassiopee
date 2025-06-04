def primeFactors(N):
    factors = list()
    def _reduce(n):
        while n % 2 == 0:
            factors.append(2)
            n //= 2
        return n
    N = _reduce(N)
    F = 3
    from math import sqrt
    while True:
        if F*F > N:
            break
        if N % F:
            F += 2
        else:
            factors.append(F)
            N //= F
    if N > 1:
        factors += [N]
    return tuple(factors)

n=int(input())
result=[]
for elem in primeFactors(n):
    result.append(str(elem))
out=""
for idx, val in enumerate(result):
    if idx!=len(result)-1:
        out+=val+" "
    else:
        out+=val
print("%d: %s"%(n, out))