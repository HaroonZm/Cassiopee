def magic(n):
    # Initialiser une variable compteur 'c' qui représente le nombre à insérer dans la matrice magiqu
    c = 1
    
    # Calculer la position initiale en x (colonne) comme la moitié de n, en division flottante
    x = n / 2  # En Python 2, '/' est une division entière si n est un int; ici il reste entier
    
    # Calculer la position initiale en y (ligne) en ajoutant 1 à x
    y = x + 1
    
    # Boucle infinie pour placer tous les nombres de 1 à n*n dans la matrice 'A'
    while True:
        # Inscrire la valeur actuelle de 'c' dans la case (y, x) de la matrice A
        A[y][x] = c
        
        # Si nous avons atteint le nombre maximal (n*n), sortir de la boucle
        if c == n * n:
            break
        
        # Boucle infinie pour trouver la prochaine position libre où insérer le prochain nombre
        while True:
            # Calculer les nouvelles coordonnées en se décalant d'une case en diagonale vers le bas à droite,
            # avec l'opération modulo 'n' pour assurer un indice cyclique et rester dans la matrice
            x, y = (x + 1) % n, (y + 1) % n
            
            # Vérifier si la case suivante est libre (égale à 0 ici)
            if A[y][x] == 0:
                # Case libre trouvée, sortir de cette boucle interne
                break
            
            # Si la case est occupée, essayer une autre direction:
            # Calculer de nouveaux indices en allant d'une case vers la droite (x-1) et vers le bas (y+1),
            # modulo 'n' pour un comportement cyclique dans la matrice
            x, y = (x - 1) % n, (y + 1) % n
            
            # Vérifier si cette nouvelle case est libre
            if A[y][x] == 0:
                # Case libre trouvée, sortir de la boucle interne
                break
        
        # Incrémenter 'c' pour passer au nombre suivant à insérer
        c += 1
    
    # Fin de la fonction sans valeur de retour explicite (retourne None par défaut)
    return

# Boucle principale infinie pour traiter plusieurs entrées utilisateur successives
while True:
    # Lire une valeur entrée par l'utilisateur et stocker dans 'n'
    n = input()
    
    # Condition d'arrêt de la boucle si l'utilisateur entre 0 (zéro)
    if n == 0:
        break
    
    # Créer un objet 'N' représentant la gamme d'indices de 0 à n-1 pour itération
    N = range(n)
    
    # Initialiser la matrice A comme une liste de listes (n lignes, n colonnes),
    # chaque élément initialisé à 0 pour représenter une case vide
    A = [[0] * n for i in N]
    
    # Appeler la fonction 'magic' pour remplir la matrice A avec la méthode définie
    magic(n)
    
    # Boucle pour parcourir chaque ligne 'i' dans la matrice
    for i in N:
        # Afficher la ligne entière sous forme de chaîne,
        # en formatant chaque élément 'e' avec un champ de largeur 4,
        # afin d'assurer un alignement visuel propre lors de l'affichage
        print "".join(["%4d" % (e) for e in A[i]])