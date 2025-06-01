def print_table(t):
    # Cette fonction affiche une table (liste de listes) de nombres entiers.
    # Le paramètre 't' est une liste de listes, où chaque sous-liste représente une ligne de la table.
    
    for c in t:
        # Pour chaque sous-liste 'c' dans la liste 't' (c'est-à-dire pour chaque ligne de la table),
        
        for r in c:
            # On parcourt chaque élément 'r' dans la sous-liste 'c' (c'est-à-dire chaque nombre entier dans la ligne).
            
            print("{0:d}".format(r), end="")
            # Affiche l'élément 'r' en format entier décimal.
            # Le paramètre 'end=""' signifie qu'il n'y aura pas de saut de ligne après l'affichage,
            # Ainsi, tous les éléments de la ligne s'affichent sur la même ligne sans espace.
            
        print("")
        # Après avoir affiché tous les éléments d'une ligne, on imprime un saut de ligne pour passer à la ligne suivante.
        # C'est ce qui permet d'avoir une représentation en forme de tableau à l'écran.

def play(t, x, y):
    # Cette fonction modifie la table t selon une règle de propagation à partir d'un point (x, y).
    # Les coordonnées x et y sont des indices dans la table t.
    # La fonction retourne la table modifiée après propagation.
    
    q = [[x, y]]
    # On initialise une liste 'q' qui servira de file d'attente pour garder les coordonnées à traiter.
    # Elle commence avec le point initial [x, y].
    
    while True:
        # Boucle infinie qui s'arrêtera lorsque la file d'attente 'q' sera vide.
        
        p = q.pop(0)
        # On enlève et récupère le premier élément de la file 'q' (FIFO - premier entré, premier sorti).
        # 'p' est donc une liste de deux éléments représentant les coordonnées à traiter.
        
        x = p[0]
        y = p[1]
        # On récupère les coordonnées x et y à partir de 'p'.
        
        t[y][x] = 0
        # On modifie la valeur dans la table à la position (y, x) en la mettant à 0.
        # Attention à l'ordre: la table est indexée par ligne puis colonne, donc t[y][x].
        
        for i in range(1, 4):
            # On veut explorer les positions à une distance de 1 à 3 pas dans les quatre directions cardinales
            # (droite, gauche, bas, haut) autour du point (x,y).
            
            if x + i < 8:
                # Vérifie que la position à droite (x + i) n'est pas en dehors des limites (maximum index 7).
                
                if t[y][x + i] == 1:
                    # Si à cette position il y a la valeur 1 (condition de propagation),
                    
                    q.append([x + i, y])
                    # On ajoute cette position à la file d'attente 'q' pour traitement ultérieur.
                    
                    t[y][x + i] = 0
                    # On met immédiatement à 0 cette cellule pour éviter de la revisiter plusieurs fois.
                    
            if x - i >= 0:
                # Vérifie que la position à gauche (x - i) est toujours valide (non négative).
                
                if t[y][x - i] == 1:
                    # Si à gauche la valeur est 1,
                    
                    q.append([x - i, y])
                    # On l'ajoute à la file d'attente.
                    
                    t[y][x - i] = 0
                    # Et on la marque comme visitée.
            
            if y + i < 8:
                # Vérifie que la position en bas (y + i) est valide (dans les limites).
                
                if t[y + i][x] == 1:
                    # Si la valeur est 1 à cette position,
                    
                    q.append([x, y + i])
                    # Ajout à la file d'attente.
                    
                    t[y + i][x] = 0
                    # Marquage comme visitée.
            
            if y - i >= 0:
                # Vérifie que la position en haut (y - i) est valide.
                
                if t[y - i][x] == 1:
                    # Si la valeur est 1,
                    
                    q.append([x, y - i])
                    # Ajout à la file d'attente.
                    
                    t[y - i][x] = 0
                    # Marquage comme visitée.
        
        if q == []:
            # Si la file d'attente est vide (plus aucun point à traiter),
            
            break
            # On sort de la boucle infinie.
            
    return t
    # On retourne la table modifiée après avoir propagé la conversion des 1 en 0.

n = int(input())
# On lit un entier 'n' depuis l'entrée standard.
# Cela représente le nombre de fois que l'on va répéter un certain processus.

for i in range(1, n + 1):
    # On réalise une boucle de 1 à n inclus.
    # 'i' sert typiquement à numéroter les cas ou les jeux de données.
    
    input()
    # On lit une ligne qu'on ignore (ne stocke pas).
    # Cela peut servir à consommer une ligne vide ou quelconque séparateur dans le format d'entrée.
    
    t = [[int(i) for i in list(input())]]
    # On lit une ligne de texte (supposée être composée de chiffres).
    # 'list(input())' convertit cette ligne en liste de caractères.
    # Chaque caractère est converti en entier via la compréhension de liste.
    # Le résultat est une liste d'entiers correspondant à une ligne de la table.
    # On met cette ligne dans une liste parente car la table est une liste de lignes.
    
    for j in range(0, 7):
        # Pour compléter la table, on répète 7 fois (on veut a priori 8 lignes au total).
        
        t.append([int(i) for i in list(input())])
        # Pour chaque itération, on lit une nouvelle ligne, on la convertit en liste d'entiers et on l'ajoute à la table 't'.
    
    x = int(input())
    # On lit un entier 'x' (coordonnée en colonne).
    
    y = int(input())
    # On lit un entier 'y' (coordonnée en ligne).
    
    tt = play(t, x - 1, y - 1)
    # On appelle la fonction 'play' avec la table t et les coordonnées ajustées (soustraction de 1 pour passer à un indice 0-based).
    # Le résultat (table modifiée) est stocké dans 'tt'.
    
    print('Data {0:d}:'.format(i))
    # On affiche un titre pour ce jeu de données avec son numéro.
    
    print_table(tt)
    # On affiche la table résultante transformée grâce à la fonction 'print_table'.