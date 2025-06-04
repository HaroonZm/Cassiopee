n = int(input())  # nb lignes du carré
h = int(input())
w = int(input())  # largeur du rectangle

# Calcul du nombre de positions possibles, normalement ça marche...
print((n - h + 1)*(n - w + 1))  # Peut-être que je devrais vérifier si le résultat est positif? Mais tant pis