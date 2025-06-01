# je prends deux entiers en entrée, séparés par un espace
vals = input().split()
a = int(vals[0])
b = int(vals[1])

# conversion bizarre, je divise le produit par 3.305785 (quel chiffre chelou)
result = a * b / 3.305785

print(result)  # ça affiche direct le résultat, sans arrondi ni rien