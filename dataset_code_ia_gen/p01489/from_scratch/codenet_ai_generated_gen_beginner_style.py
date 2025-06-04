K = int(input())

MOD = 10**9 + 7

# Cette fonction vérifie si un nombre est un nombre de Fibonacci (approche simple)
def is_fibo(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n

# On veut trouver le K-ième plus petit nombre qui peut être un nombre de chemins d'ika
# En analysant le problème, les nombres d'ika sont des nombres de Fibonacci sauf 1 (car 1 apparaît deux fois)
# Mais avec une approche simple et directe, on peut simplement générer les nombres de Fibonacci jusque ce qu'on trouve le K-ième.

# Comme K peut être très grand (jusqu'à 10^18), on ne peut pas générer directement.
# On remarque que les nombres d'ika sont les nombres de Fibonacci depuis la 2nd position,
# 1,1,2,3,5,8,13,...
# Le k-ième plus petit ika number = fib(k+1)
# Donc on calcule fib(K+1) modulo MOD

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, (a + b) % MOD
    return a

print(fib(K+1) % MOD)