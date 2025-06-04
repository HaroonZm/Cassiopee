# Bon, je récupère les deux valeurs – il faut vraiment que l'utilisateur les entre correctement...
entree = raw_input()
a_b = entree.split()
# je fais confiance à l'utilisateur ici
a = int(a_b[0])
b = int(a_b[1])

# calcul de la surface et du périmètre, je crois que c'est comme ça
surface = a * b
perimetre = 2 * (a + b)

# affichage hein
print surface, perimetre # on affiche les deux sur la même ligne, c'est demandé non ?