import math  # Ce module fournit l'accès aux fonctions mathématiques de base, telles que sqrt (racine carrée)

# Déclaration d'une constante représentant l'accélération gravitationnelle à la surface de la Terre, en m/s²
g = 9.8

# Déclaration d'une petite constante epsilon utilisée pour comparer des réels tout en évitant les problèmes de précision numérique
ESP = 1e-6

# Définition d'une fonction qui calcule la hauteur atteinte après un certain temps t, 
# en tenant compte de la vitesse initiale verticale vy et de l'effet de la gravité (g)
def calc(vy, t):
    # vy * t : distance parcourue vers le haut à vitesse constante pendant le temps t
    # g * t * t / 2 : terme représentant la perte d'altitude due à la gravité (formule du mouvement uniformément accéléré)
    return vy * t - g * t * t / 2

# Définition d'une fonction qui compare une valeur 'a' avec un intervalle [lb, ub] (bornes inférieure et supérieure)
# Prend en compte une marge d'erreur ESP pour les comparaisons à virgule flottante
def cmp(lb, ub, a):
    # Si 'a' est strictement inférieur ou égal à la borne inférieure plus une petite marge (ESP)
    if a < lb + ESP:
        # Retourner -1 signifie 'a' est trop petit (en dessous de l'intervalle)
        return -1
    # Si 'a' est strictement supérieur ou égal à la borne supérieure moins ESP
    elif ub - ESP < a:
        # Retourner 1 signifie 'a' est trop grand (au-dessus de l'intervalle)
        return 1
    else:
        # Retourner 0 signifie 'a' est dans les bornes spécifiées (modulo la tolérance ESP)
        return 0

# Définition d'une fonction principale qui vérifie s'il est possible d'atteindre le point (qx, qy)
# en tenant compte de la vitesse maximale V et des obstacles présents
def check(qx, qy):
    # Calcul de coefficients pour une équation du second degré en t², représentant le temps pour atteindre la cible
    a = (g * g) / 4  # Calcul de 'a' du polynôme quadratique
    b = g * qy - V * V  # Calcul de 'b', dépend de la hauteur cible et de la vitesse initiale maximale possible
    c = qx * qx + qy * qy  # Calcul de 'c', somme des carrés des coordonnées de la cible

    # Calcul du discriminant pour savoir si des solutions réelles existent pour cette équation du second degré
    D = b * b - 4 * a * c

    # Si le discriminant D est proche de zéro (mais négatif à cause des imprécisions de floating point), on le fixe à zéro
    if D < 0 and -ESP < D:
        D = 0

    # Si le discriminant est strictement négatif, il n'y a pas de solution réelle pour l'équation
    if D < 0:
        return False

    # Boucle sur deux valeurs : d = -1 et d = 1 ; cela permet de calculer les deux solutions du second degré
    for d in range(-1, 2, 2):
        # Calcul du temps au carré (t2) pour atteindre la cible en utilisant la formule quadratique (-b ± sqrt(D)) / (2a)
        t2 = (-b + d * math.sqrt(D)) / (2 * a)
        # Si ce temps au carré est négatif ou nul, cela n'a pas de sens physiquement
        if t2 <= 0:
            continue  # Passe à la prochaine itération

        t = math.sqrt(t2)  # Récupère le temps t (racine carrée de t2)

        # Calcul de la composante horizontale de la vitesse pour atteindre la cible
        vx = qx / t
        # Calcul de la composante verticale initiale de la vitesse pour atteindre la cible
        vy = (qy + g * t * t / 2) / t

        # Calcul de la hauteur atteinte au point d'abscisse X à partir des vitesses déterminées
        yt = calc(vy, X / vx)
        # Si la hauteur atteinte à X est insuffisante (en-dessous du niveau cible Y), tentative échouée
        if yt < Y - ESP:
            continue

        ok = True  # Indicateur pour déterminer si aucune collision n'a lieu

        # Parcours de tous les obstacles définis par leurs bornes L, R sur x, et B, T sur y
        for i in range(0, N):
            # Si la position horizontale de la borne gauche de l'obstacle est au-delà du but X, ignorer cet obstacle
            if L[i] >= X:
                continue

            # Cas où la borne droite de l’obstacle est alignée sur X et que l’obstacle se trouve entre Y et yt
            if R[i] == X and Y <= T[i] and B[i] <= yt:
                ok = False

            # Calcul de la position verticale atteinte lorsque le projectile passe à la position x = L[i] de l'obstacle
            yL = cmp(B[i], T[i], calc(vy, L[i] / vx))
            # Calcul de la position verticale atteinte en passant à la position x = R[i]
            yR = cmp(B[i], T[i], calc(vy, R[i] / vx))

            # Comparaison de la position du sommet de la trajectoire en x et y avec l'obstacle
            # vx * (vy / g) calcule la position horizontale au sommet de la parabole
            # calc(vy, vy/g) calcule l'altitude maximale atteinte par la trajectoire
            xH = cmp(L[i], R[i], vx * (vy / g))
            yH = cmp(B[i], T[i], calc(vy, vy / g))

            # Si le sommet de la trajectoire tombe dans l'intervalle horizontal de l'obstacle et que son altitude 
            # tombe dans l'obstacle ou au-dessus et que le projectile passe sous la base de l'obstacle à l'entrée,
            # alors il y a collision
            if xH == 0 and yH >= 0 and yL < 0:
                ok = False

            # Si la trajectoire entre dans l'obstacle (changement de signe entre yL et yR), collision détectée
            if yL * yR <= 0:
                ok = False

        # Si, après tous les tests, aucune collision n'est détectée, alors la trajectoire est possible
        if ok:
            return True

    # Après avoir testé toutes les solutions, on conclut qu'il n'est pas possible d'atteindre la cible
    return False

# Bloc principal du programme, exécuté seulement si le script est lancé directement
if __name__ == '__main__':
    # Lecture des quatre premiers entiers depuis l'entrée standard :
    # N = nombre d'obstacles, V = vitesse initiale maximale, X, Y = coordonnées cibles
    N, V, X, Y = list(map(int, input().split()))

    # Initialisation des listes pour stocker les bornes gauche (L), basse (B), droite (R), et haute (T) de chaque obstacle
    L = []
    B = []
    R = []
    T = []

    # Lecture successive de N lignes de l'entrée, chaque ligne décrivant un obstacle par ses coordonnées
    for i in range(N):
        tmp_L, tmp_B, tmp_R, tmp_T = list(map(int, input().split()))
        # Ajout de chaque valeur dans la liste correspondante
        L.append(tmp_L)
        B.append(tmp_B)
        R.append(tmp_R)
        T.append(tmp_T)

    # Pour chaque obstacle, on ajuste la borne droite afin de ne jamais dépasser la position X (la cible)
    for i in range(0, N):
        R[i] = min(R[i], X)

    # Initialisation : on teste s'il est possible d'atteindre directement la cible (X, Y)
    ok = check(X, Y)

    # Boucle sur les obstacles pour tester si une trajectoire passant par leur sommet gauche ou droit permet d'atteindre la cible
    for i in range(0, N):
        # Test sur l'angle supérieur gauche de chaque obstacle
        if L[i] == 0 and T[i] != 0:
            pass  # Si l'obstacle touche le bord gauche (L==0) mais n'est pas à terre (T!=0), on ignore
        else:
            ok |= check(L[i], T[i])  # On vérifie si une trajectoire passe par (L,T)

        # Test sur l'angle supérieur droit de chaque obstacle
        if R[i] == 0 and T[i] != 0:
            pass  # Même raisonnement si l'obstacle touche le bord droit (R==0) mais n'est pas à terre
        else:
            ok |= check(R[i], T[i])  # On vérifie si une trajectoire passe par (R,T)

    # Affichage du résultat final : "Yes" si une trajectoire valide existe, "No" sinon
    print("Yes" if ok else 'No')