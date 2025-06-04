# Lecture de l'entrée
N, T = map(int, input().split())

# On initialise un tableau "delta" de taille T+1 à 0, 
# ce tableau va servir à représenter les entrées (+1) et sorties (-1)
delta = [0] * (T + 1)

for _ in range(N):
    l, r = map(int, input().split())
    # On ajoute +1 à l'indice l pour marquer l'entrée d'une personne
    delta[l] += 1
    # On enlève 1 à l'indice r car la personne est partie à r (intervalle [l, r[)
    delta[r] -= 1

# Maintenant, on va calculer le nombre de personnes présentes à chaque instant
max_customers = 0
current_customers = 0

for time in range(T + 1):
    # On cumule les modifications
    current_customers += delta[time]
    # On garde en mémoire le maximum
    if current_customers > max_customers:
        max_customers = current_customers

# Affichage du résultat
print(max_customers)