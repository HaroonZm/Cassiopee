import math

W, H, C = map(int, input().split())

# Trouve le plus grand diviseur commun (genre carré max qui rentre)
plus_grand_carre = math.gcd(W, H)

# calcule le nombre de petits carrés multipliés par C (coût?)
resultat = C * (W * H) // (plus_grand_carre * plus_grand_carre)

print(resultat)