# Boucle infinie utilisant 'while 1:', ce qui signifie que la boucle s'exécutera jusqu'à ce qu'un 'break' intervienne.
while 1:
    # Lecture de deux entiers séparés par un espace depuis l'entrée utilisateur grâce à 'raw_input()'.
    # 'map(int, ...)' convertit les deux chaînes en entiers.
    h, w = map(int, raw_input().split())
    
    # Si les deux entiers lus, h et w, sont tous les deux égaux à 0, cela signifie que l'utilisateur veut arrêter.
    if h == w == 0:
        # La commande 'break' permet de sortir définitivement de la boucle while.
        break
    
    # Crée un objet range représentant la suite de valeurs de 0 à h-1 (exclusivement h).
    # C'est donc une liste d'indices pour les lignes de la grille.
    H = range(h)
    
    # Création d'une liste C de longueur h+1, initialisée à 0.
    # Cette liste sera utilisée comme aide-mémoire temporaire pendant le traitement de chaque ligne.
    C = [0] * (h + 1)
    
    # Création d'une autre liste M (pour mémorisation) comme copie de C, donc initialisée aussi à 0.
    # M servira à stocker des valeurs maximales à chaque étape.
    M = C[:]
    
    # Crée une liste 'a' de longueur w (le nombre de colonnes), initialisée à 0.
    # Cette liste va stocker, pour chaque colonne, la taille du segment vertical courant de cellules vides.
    a = [0] * w
    
    # Boucle sur chaque ligne de la grille (indice 'i' de 0 à h-1).
    for i in H:
        # Lit une chaine de caractères représentant une ligne de la grille (par exemple : '.*..*')
        x = raw_input()
        
        # Crée une nouvelle liste 'b' de longueur w initialisée à 0.
        # b va contenir temporairement des valeurs pour la ligne courante.
        b = [0] * w
        
        # Initialise 'sp' à -1. 'sp' va servir de pointeur sur la "hauteur courante" du segment le plus long de points consécutifs.
        sp = -1
        
        # Réinitialise la liste C avec la valeur -1 partout (de longueur h+1).
        # Cela signifie qu'aucun segment n'est encore détecté pour la ligne courante.
        C = [-1] * (h + 1)
        
        # Boucle sur chaque colonne 'j' de la ligne courante.
        for j in range(w):
            # Si le caractère à l'indice j de la ligne x est une étoile '*', cela indique une case pleine.
            if x[j] == "*":
                # Case pleine : La taille du segment doit être remise à 0.
                c = 0
            # Sinon, si le caractère est un point '.', c'est une case vide.
            elif x[j] == ".":
                # On ajoute 1 à la valeur du segment au-dessus (colonne j, sur la ligne précédente).
                c = a[j] + 1
            # Place la valeur trouvée (c) dans la liste temporaire b en position j.
            b[j] = c
            
            # Si c (hauteur du segment de points) est strictement supérieure à 'sp' (le segment précédent),
            # alors on met à jour 'C' sur l'intervalle concerné pour indiquer une nouvelle position de début pour ce segment.
            if c > sp:
                # 'sp+1:c+1' est un intervalle (en python, le second paramètre est exclu du range).
                # On remplit cet intervalle dans la liste C par la valeur j.
                # Cela revient à remplir les entrées C pour tous les segments de taille entre sp+1 et c avec j (la colonne actuelle).
                C[sp + 1 : c + 1] = [j] * (c - sp)
            # Si c (hauteur courante) est strictement inférieure à 'sp' (le segment précédent),
            # alors certains segments se terminent ici. Il faut donc mettre à jour les valeurs maximales dans M et remettre C à -1.
            elif c < sp:
                # Pour toutes les hauteurs k allant de c+1 à sp inclus,
                for k in range(c + 1, sp + 1):
                    # On met à jour M[k] avec la distance maximale entre la colonne actuelle (j) et le début du segment (C[k]).
                    M[k] = max(M[k], j - C[k])
                    # Puis on invalide la position de début de segment en mettant -1.
                    C[k] = -1
            # Met à jour la "hauteur courante" du segment
            sp = c
        
        # Après la fin de la ligne, il peut rester des segments ouverts que l'on doit boucler jusqu'au bord à droite.
        for k in range(1, sp + 1):
            # Si la position de début existe (C[k] >= 0)
            if C[k] >= 0:
                # On met à jour M[k] avec la largeur allant jusqu'au bord droit (w - C[k])
                M[k] = max(M[k], w - C[k])
        # Sauvegarde la nouvelle grille des hauteurs pour la prochaine itération.
        a = b[:]
    
    # Enfin, calcule le plus grand produit de a*b pour toutes les hauteurs possibles (a)
    # et leur largeur maximale (b) stockée dans M[hauteur]
    s = max([a * b for a, b in zip(M, range(h + 1))])
    
    # Affiche le plus grand produit trouvé, c'est-à-dire l'aire du plus grand rectangle possible dans la grille.
    print s