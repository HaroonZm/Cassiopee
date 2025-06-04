# voilà, je fais quelques trucs pour calculer un truc avec les entiers
n, k = map(int, input().split())   # je prends 2 entiers

cubes1 = n // k

cubes2 = 0
# hmm il paraît que si k est pair, faut en ajouter d'autres ?
if (k%2==0):
    cubes2 = (n + (k//2)) // k   # un truc bizarre mais bon

# le résultat final est la somme des cubes ?
print(cubes1 * cubes1 * cubes1 + cubes2 ** 3)  # pourquoi pas...