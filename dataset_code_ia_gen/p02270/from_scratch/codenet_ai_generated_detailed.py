# Lecture de l'entrée
n, k = map(int, input().split())
weights = [int(input()) for _ in range(n)]

# Fonction pour vérifier si on peut charger tous les paquets dans k camions avec une capacité max P
def can_load(P):
    current_sum = 0  # somme cumulée du poids des paquets dans le camion courant
    trucks_used = 1  # on commence avec un camion
    for w in weights:
        if w > P:
            # Si un paquet est plus lourd que P, impossible de charger
            return False
        if current_sum + w <= P:
            # On ajoute le paquet au camion courant si possible
            current_sum += w
        else:
            # Sinon, on passe au camion suivant
            trucks_used += 1
            current_sum = w
            if trucks_used > k:
                # On dépasse le nombre de camions disponibles
                return False
    return True


# Recherche binaire sur la valeur de P (charge maximale)
# P doit au minimum être au moins le poids du plus lourd paquet (sinon impossible)
# P au maximum être la somme totale des poids (tout dans un seul camion)
low = max(weights)
high = sum(weights)
answer = high

while low <= high:
    mid = (low + high) // 2
    if can_load(mid):
        # Si on peut charger avec cette capacité, on tente plus petit
        answer = mid
        high = mid - 1
    else:
        # Sinon on doit augmenter la capacité
        low = mid + 1

# Affichage de la réponse minimale
print(answer)