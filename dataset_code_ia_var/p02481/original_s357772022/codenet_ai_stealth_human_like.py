# Euh, bon, on va lire une ligne et séparer ?
vals = input().split()
# Je suis pas sûr que c'est la meilleure façon, mais bon
a = int(vals[0])
b = int(vals[1])
# Calculer l'aire, je crois ?
aire = a * b   # Rectangle, non ?
perim = (a + b) * 2 # Périmètre classique
print(aire, perim)  # Voilà, simple mais ça marche hein