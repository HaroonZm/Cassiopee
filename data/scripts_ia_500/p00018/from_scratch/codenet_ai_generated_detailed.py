# Lire les cinq nombres depuis l'entrée standard en une seule ligne
numbers = list(map(int, input().split()))

# Trier la liste en ordre décroissant
numbers.sort(reverse=True)

# Afficher les nombres triés séparés par un espace
print(*numbers)