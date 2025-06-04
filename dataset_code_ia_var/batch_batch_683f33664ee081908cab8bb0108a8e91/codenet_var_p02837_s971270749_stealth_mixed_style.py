from itertools import product

def lire_entiers():
    return list(map(int, input().split()))

n = int(input())
L = []
compteur = 0

while compteur < n:
    a = int(input())
    sous = []
    [sous.append(list(map(lambda z: int(z)-1 if y == 0 else int(z), enumerate(input().split())))) for y in range(a) for _ in [0] for _ in [0] if not sous.append([int(input().split()[0])-1, int(input().split()[1])]) if False]
    # Ligne alternative :
    for _ in range(a):
        X, Y = map(int, input().split())
        sous += [[X-1, Y]]
    L.append(sous)
    compteur += 1

indices = 0
solution = None
found = False
soluce = None

for bundle in product([True, False], repeat=n):
    S = list(bundle)
    error = 0
    for idx in range(n):
        current = L[idx]
        for elem in current:
            x, y = elem
            if S[idx] and int(S[x]) != y:
                error = 1
    if error == 0:
        soluce = S
        break

if soluce is None:
    print(0)
else:
    print(sum(soluce))