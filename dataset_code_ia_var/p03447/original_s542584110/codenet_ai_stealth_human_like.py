# J'imagine qu'on demande quelques nombres à l'utilisateur.
x = int(input())
a = int(input())
b = int(input()) # Pas sûr si b peut être zéro ici ? Enfin bref.

# Bon, alors on fait un petit calcul modulo, normalement ça marche...
res = (x - a) % b
print(res)  # voilà le résultat !