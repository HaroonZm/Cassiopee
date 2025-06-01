from math import *  # Importe toutes les fonctions du module math, permettant d'utiliser des fonctions et constantes mathématiques (ex : pi, atan2, sqrt).

def check(hx, hy, fx, fy, df, w, a):
    # Fonction check qui détermine si un point (hx, hy) est dans un certain secteur angulaire
    # centré en (fx, fy) avec une largeur angulaire df et une distance maximale a,
    # et si l'angle entre la direction du point et la direction w est inférieur à df.
    # hx, hy : coordonnées du point à vérifier (ex : héros).
    # fx, fy : coordonnées du point de référence (ex : feu).
    # df : demi-largeur angulaire admissible en radians (tolerance d'angle).
    # w : angle de la direction principale en radians.
    # a : distance maximale admissible.
    
    # Calcul de la distance euclidienne entre les deux points (hx, hy) et (fx, fy).
    # La distance est calculée avec la formule racine carrée de la somme des carrés des différences des coordonnées.
    distance = ((hx - fx) ** 2 + (hy - fy) ** 2) ** 0.5
    
    # Calcul de la différence angulaire absolue entre l'angle du vecteur (hx - fx, hy - fy) et l'angle w.
    # atan2(y,x) retourne l'angle en radians du point (x,y) par rapport à l'axe horizontal.
    # On soustrait w et on prend la valeur absolue adaptée pour prendre en compte le cercle trigonométrique.
    angle_diff = Abs(atan2(hy - fy, hx - fx) - w)
    
    # On teste si la distance est inférieure à a ET si la différence angulaire est inférieure à df.
    if distance < a and angle_diff < df:
        return True  # Le point est dans le cône/direction souhaité.
    else:
        return False  # Le point n'est pas dans le cône/direction souhaité.

def Abs(e):
    # Fonction Abs qui calcule la distance angulaire minimale sur un cercle de rayon 2*pi.
    # Cette fonction corrige la valeur absolue classique pour gérer le fait que l'angle est modulo 2*pi.
    # e : angle en radians.
    e = abs(e)  # Prend la valeur absolue classique (positive).
    if e > pi:
        # Si l'angle est supérieur à pi, on prend la valeur complémentaire à 2*pi pour obtenir l'angle minimum.
        e = 2 * pi - e
    return e  # Retourne l'angle minimal entre deux directions.

while 1:
    # Boucle infinie pour traiter plusieurs jeux de données tant que la condition de sortie n'est pas respectée.
    
    # Lecture de deux entiers H et R depuis l'entrée standard.
    # H : nombre d'éléments héros.
    # R : nombre de directions/essais.
    H, R = map(int, raw_input().split())
    
    # Condition d'arrêt de la boucle : si H vaut 0, on arrête la lecture et le programme.
    if H == 0:
        break
    
    # Lecture des coordonnées des H héros.
    # Chaque héros est défini par deux entiers x et y.
    # La liste hxy est une liste de listes, chaque sous-liste contient [x, y].
    hxy = [map(int, raw_input().split()) for i in range(H)]
    
    # Lecture des paramètres U, M, S, du, dm, ds (entiers).
    # U, M, S : nombres d'éléments de trois types différents (ex: différents ennemis ou points).
    # du, dm, ds : données d'angle en degrés, converties en radians.
    U, M, S, du, dm, ds = map(int, raw_input().split())
    
    # Conversion des tolérances angulaires en radians (demi-angle : on divise par 360 pour convertir en pi/180 * x/2).
    # Conversion du degrés en radians : deg * pi / 180, ici divisé par 2 donc pi/360.
    du = du * pi / 360
    dm = dm * pi / 360
    ds = ds * pi / 360
    
    # Lecture des coordonnées des U éléments du premier type + ajout de la tolérance angulaire du.
    # Chaque élément est une liste [x, y, du].
    dxy = [map(int, raw_input().split()) + [du] for i in range(U)]
    
    # Lecture des coordonnées des M éléments du second type + ajout de la tolérance angulaire dm.
    mxy = [map(int, raw_input().split()) + [dm] for i in range(M)]
    
    # Lecture des coordonnées des S éléments du troisième type + ajout de la tolérance angulaire ds.
    sxy = [map(int, raw_input().split()) + [ds] for i in range(S)]
    
    # Regroupe tous ces éléments ensemble dans une unique liste fxy.
    fxy = dxy + mxy + sxy
    
    # Initialisation de la liste count, qui comptera pour chaque héros le nombre de fois qu'une condition est remplie.
    count = [0] * H  # Liste de taille H remplie de zéros.
    
    # Boucle sur chaque direction/essai parmi les R.
    for i in range(R):
        # Lecture de l'angle w en degrés et de la distance maximale a.
        w, a = map(int, raw_input().split())
        
        # Conversion de w (angle) en radians.
        w = w * pi / 180
        
        # Normalisation de l'angle w pour qu'il soit entre -pi et pi.
        # Si w est supérieur à pi, on soustrait 2*pi pour le ramener dans l'intervalle.
        if w > pi:
            w -= 2 * pi
        
        # Pour chaque héros (index j et coordonnées hx, hy).
        for j in range(H):
            hx, hy = hxy[j]
            
            # Vérifie si le héros est dans le coin directionnel à partir de l'origine (0,0) avec tolérance du et angle w.
            # Si ce n'est pas le cas, on continue directement au héros suivant.
            if not check(hx, hy, 0, 0, du, w, a):
                continue
            
            # Pour chaque élément (fx, fy, df) de la liste fxy (obstacles/ennemis).
            for fx, fy, df in fxy:
                # Vérifie si le héros correspond à la zone bloquée par un élément dans la direction w.
                if check(hx, hy, fx, fy, df, w, a):
                    break  # On stoppe la recherche pour ce héros car il est bloqué par cet élément.
            else:
                # Si on arrive ici, c'est que le héros n'est bloqué par aucun élément dans cette direction.
                # Incrémenter le compteur pour ce héros.
                count[j] += 1
    
    # Après toutes les directions, on cherche le max des valeurs dans count (le maximum de succès).
    mx = max(count)
    
    # Si ce maximum est supérieur à zéro, on affiche la liste des indices+1 des héros ayant ce max.
    if mx > 0:
        # Transformation des indices (0-based) en indices 1-based, et affichage séparé par des espaces.
        print " ".join(map(str, [i + 1 for i in range(H) if count[i] == mx]))
    else:
        # Si aucun héros n'a satisfait la condition au moins une fois, on affiche "NA".
        print "NA"