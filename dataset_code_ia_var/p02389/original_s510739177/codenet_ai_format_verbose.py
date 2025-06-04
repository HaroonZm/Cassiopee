# Lecture de l'entrée utilisateur et suppression des espaces superflus en fin de ligne, puis découpage en liste de chaînes
dimensions_entrees_chaine = input().rstrip().split(' ')

# Conversion des dimensions de la chaîne vers des entiers pour la largeur et la hauteur
largeur_rectangle = int(dimensions_entrees_chaine[0])
hauteur_rectangle = int(dimensions_entrees_chaine[1])

# Calcul de l'aire du rectangle
aire_rectangle = largeur_rectangle * hauteur_rectangle

# Calcul du périmètre du rectangle
perimetre_rectangle = (largeur_rectangle * 2) + (hauteur_rectangle * 2)

# Affichage de l'aire et du périmètre du rectangle, séparés par un espace
print(str(aire_rectangle) + " " + str(perimetre_rectangle))