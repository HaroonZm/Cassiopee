import math

# Récupérer les valeurs de N et C, même si je sais pas trop à quoi sert C ici
N, C = map(int, input().split())

# Liste des parts de gâteaux
cakes = list(map(int, input().split()))

total_cakes = sum(cakes)
# Je calcule combien de gâteau je peux prendre, un peu à l'arrache
my_cake = math.ceil(total_cakes / (N+1))

print(my_cake)