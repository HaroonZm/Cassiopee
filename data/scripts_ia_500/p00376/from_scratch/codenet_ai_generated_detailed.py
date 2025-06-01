# Solution complète pour le problème "Red Dragonfly"

# L'approche est simple : 
# On reçoit deux positions entières x1 et x2 correspondant aux positions des têtes des libellules.
# Pour calculer la distance entre elles, on doit simplement calculer la valeur absolue de leur différence,
# c'est-à-dire |x1 - x2|.
# Ensuite, on affiche ce résultat.

# Le code suivant réalise cette tâche avec des commentaires détaillés.

# Lecture des positions x1 et x2 depuis l'entrée standard
x1, x2 = map(int, input().split())

# Calcul de la distance absolue entre les deux positions
distance = abs(x1 - x2)

# Affichage du résultat
print(distance)