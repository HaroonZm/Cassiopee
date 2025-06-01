# Initialisation de variables entières à zéro : h pour la hauteur, w pour la largeur, n pour le nombre d'obstacles
h=0
w=0
n=0

# Boucle infinie qui sera interrompue par un break lorsque la condition de sortie sera remplie
while 1:
    # Lecture d'une ligne d'entrée, séparation des valeurs par espace, conversion en entiers, affectation à h et w
    h,w=map(int,input().split())
    
    # Condition de sortie : si h et w sont tous deux 0, on arrête la boucle
    # La condition 'not h' vérifie si h == 0, même chose pour w
    if not h and not w:
      break
    
    # On décrémente h et w de 1, probablement pour travailler avec des indices commençant à 0
    h-=1
    w-=1
    
    # Création d'une matrice obs de taille (h+1) x (w+1), remplie initialement de 1
    # Cette matrice représente la grille, chaque case valant 1 signifie "accessible"
    obs=[[1]*(w+1) for i in range(h+1)]
    
    # Lecture du nombre d'obstacles à placer dans la grille, conversion en entier
    n=int(input())
    
    # Boucle pour lire les positions des obstacles
    for i in range(n):
        # Lecture des coordonnées x,y, séparées par un espace, conversion en int
        x,y=map(int,input().split())
        # On marque la case correspondante comme 0 dans obs pour indiquer un obstacle (inaccessible)
        # On soustrait 1 pour transformer la base 1 des entrées en base 0 des indices Python
        obs[x-1][y-1]=0
    
    # Création d'une matrice dp pour la programmation dynamique, de taille (h+2)x(w+2) initialisée à 0
    # Addition de 2 pour gérer les bordures et éviter les erreurs d'index lors des calculs
    dp=[[0]*(w+2) for i in range(h+2)]
    
    # Initialisation de la position de départ dans dp avec la valeur de l'accessibilité de la case de départ dans obs
    dp[0][0]=obs[0][0]
    
    # Parcours des lignes de 0 à h (inclus)
    for i in range(h+1):
        
        # Parcours des colonnes de 0 à w (inclus)
        for j in range(w+1):
            
            # Vérification si la case obs[i][j] est accessible (valeur 1)
            if obs[i][j]:
                # On ajoute à la case en dessous (dp[i+1][j]) le nombre de chemins possibles jusqu'à dp[i][j]
                dp[i+1][j]+=dp[i][j]
                
                # On ajoute à la case à droite (dp[i][j+1]) le nombre de chemins possibles jusqu'à dp[i][j]
                dp[i][j+1]+=dp[i][j]
    
    # Après remplissage de dp, on vérifie si la case finale obs[h][w] est accessible
    if obs[h][w]:
        # Si elle est accessible, on affiche le nombre de chemins pour atteindre cette case dans dp
        print(dp[h][w])
    else:
        # Sinon, on affiche 0 signifiant qu'aucun chemin viable n'existe pour atteindre la destination
        print(0)