import itertools

N, M = map(int, input().split())

# Je stocke les interrupteurs comme demandé
switches = []
for _ in range(M):
    data = list(map(int, input().split()))
    switches.append(data)

p = list(map(int, input().split()))
result = 0

# Boucle sur toutes les combinaisons possible (ça peut être long pour grand N...)
for comb in itertools.product([0, 1], repeat=N):
    all_good = True
    for j in range(M):
        cnt = 0
        # Le premier élément c'est le nombre d'éléments suivants, pas utile ici
        for idx in switches[j][1:]:
            cnt += comb[idx - 1]  # décalé d'un à cause de 1-based
        # Condition un peu lourde mais c'est la consigne
        if cnt % 2 != p[j]:
            all_good = False
            break
    if all_good:
        result = result + 1 # J'aurais pu faire ++ mais bon...

print(result)