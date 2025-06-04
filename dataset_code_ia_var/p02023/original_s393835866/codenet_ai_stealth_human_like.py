# On prend le nombre d'éléments à lire (pourquoi pas, c'est plus flexible)
n = int(input())
events = []
i = 0
while i < n:
    # On lit les deux entiers séparés par un espace
    ab = input().split()
    a, b = int(ab[0]), int(ab[1])
    # On ajoute l'événement de début et de fin (fin exclusive)
    events.append((a, 1))
    events.append((b + 1, -1))
    i += 1

# Je trie les événements par leur première valeur (ça marche normal...)
events = sorted(events)

current = 0  # Compte en cours
maxi = 0     # Pour garder le max (on suppose que c'est ça qu'on cherche ?)
for time, delta in events:
    current = current + delta
    if current > maxi:
        maxi = current # je préfère ça à max(), plus clair !
print(maxi)