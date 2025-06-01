import math  # Importation du module math qui fournit des fonctions mathématiques avancées comme sqrt pour la racine carrée

# Début d'une boucle infinie while True qui tournera sans fin jusqu'à rencontrer un break
while True :
    # Définition d'une liste appelée color qui contient 8 sous-listes représentant des couleurs en format RGB
    # Chaque sous-liste contient trois valeurs entières correspondant aux intensités des canaux Rouge, Vert et Bleu (allant de 0 à 255)
    # Par exemple [0,0,0] correspond à la couleur noire, [255,255,255] à la couleur blanche
    color = [[0, 0, 0], [0, 0, 255], [0, 255, 0], [0, 255, 255], 
    [255, 0, 0], [255, 0, 255], [255, 255, 0], [255, 255, 255]]

    # Attente d'une entrée utilisateur au clavier, stockée comme une chaîne de caractères dans color_16
    # Cette chaîne est censée être un code hexadécimal commençant par '#' suivi de 6 caractères hexadécimaux (ex: #1A2B3C)
    color_16 = input()
    # Vérification si la chaîne entrée est exactement "0"
    # Si oui, on sort de la boucle infinie avec break, ce qui arrête le programme
    if color_16 == "0" :
        break
    
    # Extraction et conversion des composantes rouge, vert et bleu depuis la chaîne hexadécimale
    # color_16[1]+color_16[2] récupère les deux caractères correspondant au canal rouge (ex: "1A")
    # int(...,16) convertit cette valeur hexadécimale en nombre entier base 10 (ex: 0x1A -> 26)
    color_R = int(color_16[1] + color_16[2], 16)
    # Même principe pour la composante verte, récupérant les caractères aux positions 3 et 4
    color_G = int(color_16[3] + color_16[4], 16)
    # Même pour la composante bleue, positions 5 et 6
    color_B = int(color_16[5] + color_16[6], 16)
    
    # Initialisation d'une variable min_d à une valeur élevée arbitraire (500)
    # Cette variable servira à stocker la distance la plus faible trouvée entre la couleur entrée et celles de la liste
    min_d = 500
    # Boucle for allant de 0 à 7 (8 itérations) pour parcourir toutes les couleurs définies dans la liste color
    for i in range(8) :
        # Récupération des composantes rouge, vert et bleu de la i-ème couleur dans la liste color
        R = color[i][0]
        G = color[i][1]
        B = color[i][2]
        # Calcul de la distance euclidienne entre la couleur entrée (color_R,color_G,color_B)
        # et la i-ème couleur dans color selon la formule racine carrée de la somme des carrés des différences des composantes
        # Cette distance est une mesure de similarité entre les deux couleurs dans l'espace RGB
        d = math.sqrt((R - color_R)**2 + (G - color_G)**2 + (B - color_B)**2)
        # Si la distance d calculée est inférieure à la distance minimale stockée min_d,
        # on met à jour min_d avec cette nouvelle valeur plus petite
        # ainsi que color_num avec l'indice i correspond à la couleur la plus proche jusqu'à présent
        if min_d > d :
            min_d = d
            color_num = i
    
    # Après avoir déterminé la couleur la plus proche color_num, on utilise une série de conditions if-elif-else
    # pour afficher le nom de la couleur correspondante selon l'indice color_num trouvé
    if color_num == 0 :
        print("black")  # Si l'indice est 0, afficher "black" pour noir
    elif color_num == 1 :
        print("blue")   # Indice 1 correspond à bleu
    elif color_num == 2 :
        print("lime")   # 2 correspond à lime (vert clair)
    elif color_num == 3 :
        print("aqua")   # 3 correspond à aqua (cyan)
    elif color_num == 4 :
        print("red")    # 4 correspond à rouge
    elif color_num == 5 :
        print("fuchsia") # 5 correspond à fuchsia (magenta)
    elif color_num == 6 :
        print("yellow")  # 6 correspond à jaune
    else :
        print("white")   # Sinon, on affiche white pour blanc (indice 7)