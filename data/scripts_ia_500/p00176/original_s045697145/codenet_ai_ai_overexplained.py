import math

# Définition d'une liste nommée L qui contient des tuples.
# Chaque tuple représente une couleur avec :
# - un nom de couleur sous forme de chaîne de caractères (string)
# - trois entiers représentant les composantes Rouge (R), Vert (G) et Bleu (B)
#   qui vont de 0 à 255 inclus. Ces valeurs définissent la couleur dans l'espace RGB.
L=[
    ("black", 0, 0, 0),        # Noir : pas de lumière (R=0, G=0, B=0)
    ("blue", 0, 0, 255),       # Bleu pur : maximum de bleu (R=0, G=0, B=255)
    ("lime", 0, 255, 0),       # Vert pur (appelé "lime") : max vert (R=0, G=255, B=0)
    ("aqua", 0, 255, 255),     # Cyan (aqua) : mélange vert et bleu max (R=0, G=255, B=255)
    ("red", 255, 0, 0),        # Rouge pur : max rouge (R=255, G=0, B=0)
    ("fuchsia", 255, 0, 255),  # Magenta (fuchsia) : mélange rouge et bleu max (R=255, G=0, B=255)
    ("yellow", 255, 255, 0),   # Jaune : mélange rouge et vert max (R=255, G=255, B=0)
    ("white", 255, 255, 255)   # Blanc : toutes les couleurs au maximum (R=255, G=255, B=255)
]

# Boucle infinie permettant à l'utilisateur d'entrer plusieurs valeurs successivement.
while True:
    # Lecture d'une chaîne de caractères entrée par l'utilisateur.
    # raw_input() renvoie la chaîne saisie, ici on l'attribue à la variable 'c'.
    # Note : en Python 3, la fonction s'appelle input(), ici raw_input() est utilisé (Python 2).
    c = raw_input()
    
    # Condition pour vérifier si l'utilisateur a entré "0"
    # Si oui, on sort de la boucle (break met fin à la boucle while).
    if c == "0":
        break
    
    # Extraction des composantes RGB depuis la chaîne c qui est supposée être un code hexadécimal de couleur.
    # Par exemple, si c = "#FFAA00", alors :
    # - c[1:3] récupère "FF"
    # - c[3:5] récupère "AA"
    # - c[5:7] récupère "00"
    # Chaque substring est converti en entier base 16 via int(..., 16).
    # Cela donne les valeurs entières de rouge, vert et bleu.
    Rk = int(c[1:3], 16)  # Rouge extrait de la chaîne hexadécimale
    Gk = int(c[3:5], 16)  # Vert extrait
    Bk = int(c[5:7], 16)  # Bleu extrait
    
    # Initialisation d'une variable m avec une grande valeur arbitraire (ici 10000)
    # Cette variable va conserver la plus petite distance trouvée entre la couleur entrée et celles de la liste.
    m = 10000
    
    # Parcours de chaque couleur dans la liste L.
    # Pour chaque tuple on récupère le nom (cl), et les composantes r, g, b.
    for cl, r, g, b in L:
        # Calcul de la distance Euclidienne entre la couleur saisie et la couleur actuelle dans la liste.
        # La distance Euclidienne entre deux points (r, g, b) et (Rk, Gk, Bk) est :
        # racine carrée de ((r - Rk)^2 + (g - Gk)^2 + (b - Bk)^2)
        # Cela mesure à quel point la couleur saisie est proche de la couleur L[i].
        t = math.sqrt(pow(r - Rk, 2) + pow(g - Gk, 2) + pow(b - Bk, 2))
        
        # Si cette distance t est inférieure à m (la plus petite trouvée jusqu'à présent),
        # alors on met à jour m avec t, et on mémorise la couleur associée dans la variable color.
        if t < m:
            m = t
            color = cl
    
    # Affichage du nom de la couleur la plus proche de celle entrée par l'utilisateur.
    print color