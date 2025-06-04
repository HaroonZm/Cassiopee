import math as M  # Importation du module mathématiques et renommage sous le nom M

# Fonction qui calcule la norme (longueur) d'un vecteur 2D représenté par une liste de 2 nombres
def R(A): 
    # A est une liste de deux éléments [x, y]
    # A[0]**2 est le carré de la composante x
    # A[1]**2 est le carré de la composante y
    # On additionne ces deux carrés et calcule la racine carrée du résultat
    # Ceci correspond à la distance euclidienne de l'origine jusqu'au point (x, y)
    return (A[0]**2 + A[1]**2)**0.5  # 0.5 est l'exposant pour racine carrée

# Fonction pour lire plusieurs lignes d'entrée contenant des entiers
def I(i): 
    # i est le nombre de lignes à lire
    # [0]*i crée une liste de i éléments valant 0 pour permettre une itération exacte i fois
    # Chaque itération lit une ligne entière avec raw_input(), la découpe au niveau des espaces (split),
    # puis convertit chaque morceau de texte (str) en entier avec int()
    # map(int, ...) applique cette transformation à chaque élément de la ligne découpée
    # On encapsule map(int, ...) dans une liste pour obtenir des listes d'entiers
    # Enfin, la liste de listes est renvoyée
    return [list(map(int, raw_input().split())) for _ in [0]*i]

# Fonction de comparaison entre deux nombres float a et b
def C(a, b): 
    # Cette fonction retourne True si a est strictement plus grand que b
    # OU bien si la différence absolue entre a et b est inférieure à 1e-6 (très proche)
    # Cela permet de gérer la comparaison d'entiers et de flottants avec tolérance d'erreur numérique
    return a > b or abs(a - b) < 1e-6

# Fonction principale déterminant si un point d'arrivée sx, sy à partir de tx, ty est "Safe" ou "Danger"
def f(e1):
    # Décomposition de la liste e1 en ses éléments constituants
    tx, ty, sx, sy = e1  # tx, ty : position de destination ; sx, sy : position de départ
    
    x = []  # Liste qui recueille les résultats d'évaluation pour chaque obstacle
    st = [tx - sx, ty - sy]  # Vecteur du point départ vers le point destination
    rst = R(st)  # Distance (longueur du vecteur st)
    
    # Pour chaque obstacle wp dans la liste WP (à chaque itération e2)
    for e2 in WP:
        wx, wy, r = e2  # Décomposition : wx, wy : centre de l'obstacle, r : rayon de l'obstacle
        
        wt = [tx - wx, ty - wy]  # Vecteur du centre de l'obstacle jusqu'au point d'arrivée
        rwt = R(wt)  # Distance du point d'arrivée au centre de l'obstacle
        
        sw = [wx - sx, wy - sy]  # Vecteur du point de départ jusqu'au centre de l'obstacle
        rsw = R(sw)  # Distance du point de départ au centre de l'obstacle
        
        # Vérification de l'inclusion des points dans l'obstacle à l'aide du rayon r
        F = [rwt < r, rsw < r]  # F[0] = True si arrivée DANS l'obstacle, F[1] = True si départ DANS l'obstacle
        
        c = 1  # Variable utilisée pour stocker un état intermédiaire, par défaut "Safe"
        
        # Si un point est DANS l'obstacle mais pas les deux, c'est dangereux
        if F == [1, 0] or F == [0, 1]: 
            return 0  # Retour immédiat : trajet en "Danger"
        
        # Si NI départ, NI arrivée ne sont dans l'obstacle
        elif F == [0, 0]:
            # Calcul d'angle lié à la géométrie tangente de l'obstacle
            # M.acos(r / rsw) donne l'angle dont le cosinus vaut r/rsw
            # M.pi/2 - M.acos(r/rsw) donne l'angle complémentaire
            a = M.pi / 2 - M.acos(r / rsw)
            
            # Produit scalaire entre vecteurs sw et st
            numerator = sw[0] * st[0] + sw[1] * st[1]
            denominator = rsw * rst
            quotient = numerator / denominator
            # arrondi à 4 décimales du quotient pour éviter soucis numériques avec acos
            b = M.acos(round(quotient, 4))
            
            # Si ces deux angles sont proches, ET que la distance carrée du trajet ne dépasse pas
            # la valeur critique, alors DANGER
            if C(a, b) and C(rst ** 2, rsw ** 2 - r ** 2): 
                return 0  # Danger : un obstacle peut être heurté
                
        # On ajoute 1 à la liste x puisqu'il n'y a pas d'obstacle bloquant à cette étape
        x.append(c)
    # La fonction renvoie True si TOUS les obstacles sont "Safe" (aucun 0 dans x)
    return all(x)

# Boucle principale du programme
while 1:
    n = input()  # Lecture d'un nombre entier n, nombre d'obstacles
    if n == 0:
        break  # Condition d'arrêt : si 0, on sort de la boucle principale
        
    WP = I(n)  # Liste des obstacles : chaque élément est une liste [wx, wy, r]
    
    P = I(input())  # Récupération des requêtes à vérifier : chaque requête est une liste [tx, ty, sx, sy]
    
    # Pour chaque point à vérifier dans la liste P :
    for e in P:
        # f(e) détecte si le trajet e traverse un des obstacles
        # L'opérateur [] remplace le if/else : 0 => 'Danger', 1 => 'Safe'
        # Donc si f(e) renvoie 1 (Safe), on obtient "Safe"
        # Sinon si f(e) renvoie 0 (Danger), on obtient "Danger"
        print (["Safe", "Danger"][f(e)])  # Affiche le résultat pour chaque requête