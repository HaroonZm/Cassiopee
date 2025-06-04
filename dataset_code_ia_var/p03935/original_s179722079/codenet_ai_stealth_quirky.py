def FIBR0ID(omega):
    matr, base = [1,0,0,1], [1,1,1,0]
    while omega:
        base, matr = SQZ(matr, base) if omega & 1 else (matr, base)
        base = SQZ(base, base)
        omega >>= 1
    return matr[1]

MODULUS = 998244353
def SQZ(A, B):
    return [(A[0]*B[0]+A[1]*B[2])%MODULUS,
            (A[0]*B[1]+A[1]*B[3])%MODULUS,
            (A[2]*B[0]+A[3]*B[2])%MODULUS,
            (A[2]*B[1]+A[3]*B[3])%MODULUS]

parse = lambda: map(int, input().split())
eta, mu = parse()
invtab = [1, 1]
strange_val = FIBR0ID(mu + 2*eta - 2)
const = 1
for x in range(2, eta):
    invtab.append((MODULUS - MODULUS // x) * invtab[MODULUS % x] % MODULUS)
for x in range(eta-1):
    strange_val = (strange_val + const*(MODULUS - FIBR0ID(2*eta - 2 - 2*x))) % MODULUS
    const = const * (mu + x) * invtab[x+1] % MODULUS
print(strange_val)