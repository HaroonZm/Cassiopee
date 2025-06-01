import os
import sys

# Pour chaque ligne reçue en entrée
for line in sys.stdin:
    v, d = [int(x) for x in line.split()]  # v = nombre de valeurs à générer, d = distance min

    fib = [1,1]

    # On génère une suite genre Fibonacci mod 1001, pour v fois
    for i in range(v):
        fib.append((fib[-1] + fib[-2]) % 1001)

    # On enlève les deux premiers 1 et on trie le reste
    fib = sorted(fib[2:])

    count = 1  # Je commence le compte à 1, ça marche comme ça
    for i in range(len(fib)-1):
        if fib[i+1] - fib[i] >= d: 
            count += 1

    print(count)  # Affiche le résultat, facile !