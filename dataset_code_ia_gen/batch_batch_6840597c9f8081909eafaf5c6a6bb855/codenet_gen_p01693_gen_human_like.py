n = int(input())
p = list(map(int, input().split()))

# Vérifier si c'est déjà un dérangement
def est_derangement(arr):
    for i in range(len(arr)):
        if arr[i] == i + 1:
            return False
    return True

if est_derangement(p):
    print(0)
    exit()

# Créer la liste des positions avec p_i == i+1 (éléments fixes)
fixes = [i for i in range(n) if p[i] == i + 1]

# Coût total
cost = 0

# Pour corriger les éléments fixes, on va les permuter entre eux ou avec d'autres indices
# Stratégie : pour chaque élément fixe, on échange avec un autre élément qui n'est pas fixe
# pour diminuer la possibilité d'avoir un nouvel élément fixe.

used = [False]*n  # pour marquer les indices déjà corrigés
for i in range(n):
    if p[i] == i + 1:
        # Chercher un j différent de i pour échanger
        # Priorité : j qui n'est pas fixe
        candidate = -1
        for j in range(n):
            if j != i and not used[j] and p[j] != j + 1:
                candidate = j
                break
        if candidate == -1:
            # Sinon, échanger avec un autre fixe non utilisé
            for j in range(n):
                if j != i and not used[j]:
                    candidate = j
                    break
        # Effectuer l'échange
        cost += (p[i] + p[candidate]) * abs(i - candidate)
        p[i], p[candidate] = p[candidate], p[i]
        used[i] = True
        used[candidate] = True

# Il se peut qu'en corrigeant certains fixes on en crée d'autres. Réitérer jusqu'à dérangement.
while not est_derangement(p):
    for i in range(n):
        if p[i] == i + 1:
            # Trouver un j différent pour échange
            candidate = -1
            for j in range(n):
                if j != i:
                    candidate = j
                    break
            cost += (p[i] + p[candidate]) * abs(i - candidate)
            p[i], p[candidate] = p[candidate], p[i]

print(cost)