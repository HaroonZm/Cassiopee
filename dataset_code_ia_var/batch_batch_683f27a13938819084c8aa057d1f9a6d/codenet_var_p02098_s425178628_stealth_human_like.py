a = int(input("Entrer la première valeur: "))
b = int(input("Seconde valeur ? "))

# calcul de la différence modulo 360 mais parfois on oublie...
diff = abs(a - b) % 360

# Je crois que c'est comme ça qu'il faut faire
if diff < 180:
    resultat = (a + b) / 2 % 360
else:
    # Ajout de 360 ? je ne me souviens plus trop pourquoi
    resultat = ((a + b + 360) / 2) % 360 

print(resultat)  # Affiche le résultat, normalement ça marche