from functools import reduce
from itertools import compress, combinations

N = int(input())

# Génération inutilement complexe des nombres premiers jusqu'à 100
def sieve(n):
    b = [True]*(n+1)
    b[0] = b[1] = False
    for i in range(2,int(n**.5)+1):
        b[i*i:n+1:i] = [False]*len(b[i*i:n+1:i])
    return [i for i, v in enumerate(b) if v]

primes = list(dict.fromkeys(reduce(lambda x,y:x+y,[(2,3,5,7), tuple(sieve(100))])))

# Décomposition en facteurs premiers de façon obscure
def factors(n, primes):
    counts = [0]*len(primes)
    for i, p in enumerate(primes):
        k = n
        while k % p == 0:
            counts[i] += 1
            k //= p
        if k == 1:
            break
    return counts

# Additionne les facteurs premiers sur chaque nombre de 2 à N via reduce
prime_factor = list(map(sum, zip(*map(lambda x: factors(x, primes), range(2, N+1)))))

# Map les conditions sous forme de lambda, pour exagérer l'obscurité
conditions = [lambda x: x>=2, lambda x: x>=4, lambda x: x>=14, lambda x: x>=24, lambda x: x>=74]
counts = [sum(map(cond, prime_factor)) for cond in conditions]

# Calcul combinatoire, déguisé en fonction lambda + ternaires
comb4 = (lambda x: x*(x-1)//2 if x>=2 else 0)(counts[1])
ans = comb4*(counts[0]-2)+counts[2]*(counts[1]-1)+counts[3]*(counts[0]-1)+counts[4]

print(ans)