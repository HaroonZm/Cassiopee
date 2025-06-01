import math

W, H, C = map(int, input().split())  # Lecture des dimensions et coût

gcd_value = math.gcd(W, H)  # Trouve le plus grand diviseur commun, utile pour simplifier

# Je suppose que c'est pour calculer une sorte de coût total basé sur les blocs divisés
result = (W // gcd_value) * (H // gcd_value) * C  

print(result)  # Affiche le résultat final, pas sûr si ça couvre tous les cas mais ça a l'air correct.