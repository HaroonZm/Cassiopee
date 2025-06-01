import math  # Importe le module math qui contient des fonctions mathématiques avancées dont sqrt()

# Définition d'une liste "sample1" contenant 8 sous-listes représentant des couleurs en format RGB.
# Chaque sous-liste contient 3 entiers (rouge, vert, bleu) chacun compris entre 0 et 255.
sample1 = [ 
    [0, 0, 0],        # noir (noir absolu)
    [0, 0, 255],      # bleu
    [0, 255, 0],      # vert lime
    [0, 255, 255],    # aqua (cyan)
    [255, 0, 0],      # rouge
    [255, 0, 255],    # fuchsia (magenta)
    [255, 255, 0],    # jaune
    [255, 255, 255]   # blanc
]

# Définition d'une autre liste "sample2" contenant les noms des couleurs correspondantes aux valeurs RGB dans sample1.
sample2 = ['black', 'blue', 'lime', 'aqua', 'red', 'fuchsia', 'yellow', 'white']

# Boucle infinie pour permettre à l'utilisateur d'entrer plusieurs codes couleurs jusqu'à ce qu'il décide d'arrêter.
while True:
    # Lecture d'une chaîne de caractères entrée par l'utilisateur via le clavier.
    color = input()
    
    # Condition pour sortir de la boucle : si l'utilisateur tape '0', fin du programme.
    if color == '0':
        break
    
    # Conversion de la chaîne de caractères "color" en une liste de caractères individuels.
    Color = list(color)
    
    # Suppression du premier caractère de la liste, qui est très probablement '#' dans un code hexadécimal.
    Color.pop(0)
    
    # Une boucle parcourant chaque index i de 0 à 5 inclus,
    # car un code couleur hexadécimal complet (sans #) est toujours composé de 6 caractères (2 pour R, 2 pour G, 2 pour B).
    for i in range(6):
        # Remplacement manuel des lettres hexadécimales minuscules a,b,c,d,e,f par leurs valeur décimales correspondantes 10-15,
        # ceci est fait pour faciliter la conversion ultérieure en nombre entier.
        if Color[i] == 'a':
            Color.pop(i)       # On enlève le caractère 'a' à l'index i
            Color.insert(i, 10) # On insère le nombre entier 10 à l'index i
        if Color[i] == 'b':
            Color.pop(i)
            Color.insert(i, 11)
        if Color[i] == 'c':
            Color.pop(i)
            Color.insert(i, 12)
        if Color[i] == 'd':
            Color.pop(i)
            Color.insert(i, 13)
        if Color[i] == 'e':
            Color.pop(i)
            Color.insert(i, 14)
        if Color[i] == 'f':
            Color.pop(i)
            Color.insert(i, 15)
    
    # Conversion des deux premiers caractères (représentant la composante rouge en hexadécimal) en entier décimal.
    # La valeur de la première position est multipliée par 16 (base hexadécimale),
    # puis on additionne la valeur de la seconde position.
    R = int(Color[0]) * 16 + int(Color[1])
    
    # Même opération pour les deux caractères suivants qui représentent la composante verte.
    G = int(Color[2]) * 16 + int(Color[3])
    
    # Même opération pour les deux derniers caractères représentant la composante bleue.
    B = int(Color[4]) * 16 + int(Color[5])
    
    # Initialisation d'une liste vide D qui contiendra la distance entre la couleur entrée et chacune des 8 couleurs de reference.
    D = []
    
    # Boucle parcourant les index de 0 à 7 (pour parcourir les 8 couleurs de sample1).
    for i in range(8):
        # Calcul de la distance Euclidienne dans l'espace RGB entre la couleur entrée et la i-ème couleur de sample1.
        # La distance Euclidienne est la racine carrée de la somme des carrés des différences entre les composantes R, G, B.
        d = math.sqrt( (R - sample1[i][0])**2 + (G - sample1[i][1])**2 + (B - sample1[i][2])**2 )
        
        # Ajout de la distance calculée à la liste D.
        D.append(d)
    
    # Recherche de la valeur minimale dans la liste D (distance la plus petite).
    dmin = min(D)
    
    # Recherche de l'indice dans D qui correspond à cette valeur minimale,
    # cela indique l'indice de la couleur dans sample1 la plus proche de la couleur entrée.
    index = D.index(dmin)
    
    # Affichage du nom de la couleur la plus proche basée sur son indice, en récupérant la valeur dans sample2.
    print(sample2[index])