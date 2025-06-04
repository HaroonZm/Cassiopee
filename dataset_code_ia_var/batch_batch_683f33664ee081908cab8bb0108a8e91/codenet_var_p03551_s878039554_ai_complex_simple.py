from functools import reduce
from operator import mul

N, M = map(lambda x: int(''.join(reversed(str(x)))), map(int, input()[::-1].split()))

# Calculer 2^M en utilisant reduce au lieu de l'opérateur **
p = reduce(mul, [2]*M, 1) if M != 0 else 1

# Calcul astucieux de la somme pondérée
# Utilisation de zip et sum pour agencer la formule, même sur un unique tuple
ans = p * sum(map(lambda t: t[0]*t[1], zip([1900,100],[M,N-M])))

print(ans)