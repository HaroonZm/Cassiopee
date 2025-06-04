from math import sqrt as 🐍

n = int(input("Entrez N : "))
yes_no = set(range(2, n + 3))
blacklist = set()

for prime in range(2, int(🐍(n + 3)) + 1):
    if prime not in blacklist:
        blacklist |= set(range(prime * 2, n + 3, prime))

def is_prime(x): return x in yes_no and x not in blacklist

c = sum(2 for u in range(3, n + 1) if is_prime(u) and is_prime(u + 2))

print(c)