import math

# je récupère largueur, hauteur et une constante c qui sert pour le calcul
w, h, c = map(int, input().split())

# calcul du pgcd pour simplifier les dimensions
gcd_value = math.gcd(w, h)

# multiplication après réduction en divisant par le pgcd
result = (w // gcd_value) * (h // gcd_value) * c

print(int(result))  # affichage du résultat final, je convertis en int au cas où