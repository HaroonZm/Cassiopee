import math as M  # Importation du module math sous l'alias M pour simplifier l'appel aux fonctions mathématiques

def R(A):
    # Cette fonction calcule la norme euclidienne (distance à l'origine) d'un vecteur en 2D.
    # Elle prend en argument une liste ou un tuple A représentant un point ou un vecteur [x, y].
    # Élève les coordonnées au carré, les additionne, puis prend la racine carrée de la somme.
    return (A[0] ** 2 + A[1] ** 2) ** 0.5

def I(i):
    # Cette fonction lit 'i' lignes de l'entrée standard et retourne une liste de listes d'entiers.
    # Elle utilise raw_input() pour lire une ligne au format chaîne de caractères, la découpe en morceaux via split(),
    # applique la conversion int() à chaque élément grâce à map, puis range sur la valeur i pour boucler.
    # Note : raw_input() est utilisé en Python 2. En Python 3, remplacer raw_input() par input().
    return [map(int, raw_input().split()) for _ in [0] * i]

def C(a, b):
    # Cette fonction compare deux nombres a et b.
    # Elle retourne True si 'a' est strictement supérieur à 'b', ou si 'a' et 'b' sont presque égaux à une précision de 1e-6.
    # abs(a-b) < 1e-6 vérifie si la différence absolue est inférieure au seuil, gérant les imprécisions des flottants.
    return a > b or abs(a - b) < 1e-6

def f(e1):
    # Cette fonction prend comme entrée une liste e1 de 4 entiers représentant les coordonnées de deux points :
    # e1 = [tx, ty, sx, sy], où (tx, ty) est un point cible et (sx, sy) est le point source.
    tx, ty, sx, sy = e1  # Décomposition de la liste en variables individuelles
    x = []  # Liste pour stocker les résultats de chaque obstacle rencontré

    for e2 in WP:  # WP est une liste globale contenant les obstacles, chaque obstacle est [wx, wy, r]
        wx, wy, r = e2  # wx, wy : centre de l'obstacle, r : rayon
        
        wt = [tx - wx, ty - wy]  # Vecteur du centre de l'obstacle vers la cible
        rwt = R(wt)  # Distance du centre de l'obstacle jusqu'à la cible
        
        sw = [wx - sx, wy - sy]  # Vecteur du point source vers le centre de l'obstacle
        rsw = R(sw)  # Distance du point source au centre de l'obstacle
        
        st = [tx - sx, ty - sy]  # Vecteur du point source vers la cible
        rst = R(st)  # Distance du point source à la cible
        
        F = [rwt < r, rsw < r]  # Liste booléenne : 
                                 # F[0] -> la cible est dans l'obstacle ?
                                 # F[1] -> la source est dans l'obstacle ?
        
        if rst == 0:
            # Cas où la source et la cible sont superposés (distance nulle)
            c = 1  # Considéré comme 'Safe'
        elif F == [1, 1]:
            # Les deux points (source et cible) sont à l'intérieur de l'obstacle
            c = 1  # 'Safe'
        elif F == [1, 0] or F == [0, 1]:
            # Un seul point sur deux est dans l'obstacle
            c = 0  # 'Danger'
        elif F == [0, 0]:
            # Aucun des deux points n'est dans l'obstacle, il faut vérifier l'interférence
            # Calcul d'un angle entre des vecteurs pour savoir si l'obstacle coupe le segment source-cible
            # a représente l'angle maximal toléré vers lequel le vecteur sw peut être écarté sans toucher l'obstacle
            a = M.pi / 2 - M.acos(r / rsw)
            # Produit scalaire de sw et st, normalisé, donne le cosinus de l'angle entre les deux vecteurs
            val = (sw[0] * st[0] + sw[1] * st[1]) / (rsw * rst)
            # Utiliser round(val,4) pour corriger les petits dépassements de 1 à cause de la précision flottante
            b = M.acos(round(val, 4))
            if C(a, b) and C(rst ** 2, rsw ** 2 - r ** 2):
                # Si l'angle b est compatible et que la distance de la cible au point source
                # est assez grande pour rester hors de la sphère de l'obstacle, c'est 'Danger'
                c = 0
            else:
                # Sinon, c'est 'Safe'
                c = 1
        x.append(c)  # On ajoute l'information de cet obstacle à la liste
    # Retourne True si tous les obstacles sont franchissables sans danger (aucun obstacle n'est 'danger')
    return all(x)

# Boucle principale du programme, qui va traiter plusieurs ensembles de données jusqu'à ce que 0 soit saisi
while 1:
    n = input()  # Lecture d'un entier : nombre d'obstacles
    if n == 0:
        break  # Si 0, fin du traitement (sortie de la boucle infinie)
    WP = I(n)  # Lecture des obstacles : liste de n listes [wx, wy, r]
    P = I(input())  # Lecture du nombre de requêtes (points à vérifier), suivies de ces requêtes
    for e in P:
        # Pour chaque requête, appelle la fonction f pour savoir si le chemin source-cible est 'Safe' ou 'Danger'
        # f(e) renvoie True (Safe) ou False (Danger), la liste ["Safe","Danger"][f(e)] sélectionne la bonne chaîne
        print ["Safe", "Danger"][f(e)]  # Affiche le résultat pour chaque requête