# Déclaration de la fonction 'calc' pour calculer la hauteur verticale atteinte à un instant t
def calc(vy, t):
    # vy : composante verticale initiale de la vitesse
    # t  : temps écoulé
    # g  : accélération gravitationnelle (constante globale)
    # La formule est : y = vy * t - (1/2) * g * t^2
    return vy * t - g / 2 * t * t  # Ceci applique la physique élémentaire du mouvement rectiligne uniformément accéléré

# Déclaration de la fonction 'cmp' pour comparer une valeur x à une plage [lb, ub], en tenant compte d'une tolérance (eps)
def cmp(lb, ub, x):
    # Si x est strictement inférieur à lb + eps (proche de la borne inférieure)
    if x < lb + eps:
        return -1  # On retourne -1 pour signifier "en dessous"
    # Si x est strictement supérieur à ub - eps (proche de la borne supérieure)
    elif x > ub - eps:
        return 1   # On retourne 1 pour signifier "au dessus"
    # Sinon, x est dans la plage comprise entre lb et ub
    return 0       # On retourne 0 pour signifier "dedans"

# Déclaration de la fonction 'check' pour vérifier s'il existe une trajectoire valide vers un point donné (qx, qy)
def check(qx, qy):
    # qx : coordonnée x de la cible à vérifier
    # qy : coordonnée y de la cible à vérifier
    # Si qx = 0, on ne peut pas atteindre le point (trajectoire verticale sans portée horizontale)
    if qx == 0:
        return 0
    # Calcul des coefficients de l'équation quadratique résultant de la physique du projectile
    a = g * g / 4  # (g^2)/4
    b = qy * g - V * V  # terme lié à l'énergie cinétique et à la hauteur cible
    c = qx * qx + qy * qy  # somme des carrés (distance euclidienne au carré du but)
    # Calcul du discriminant (Delta) pour déterminer l'existence de solutions réelles
    D = b * b - 4 * a * c  # Delta de l'équation quadratique
    # Si D < -eps, aucune solution réelle
    if D < -eps:
        return 0
    # Si D est très légèrement négatif (en raison des erreurs de calcul flottant), on le considère comme nul
    if -eps <= D < 0:
        D = 0
    # Pour chaque racine possible (on teste avec les deux signes du radical de Delta)
    for d in (-1, 1):
        # Calcul de la racine de l'équation du second degré, c'est tt^2 (tt sera le temps au carré)
        tt = (-b + d * D ** 0.5) / (2 * a)
        # Si tt est négatif ou nul, ce temps n'est pas physique (pas de solution valide)
        if tt <= 0:
            continue
        # t (temps) est la racine carrée de tt (temps doit être positif)
        t = tt ** 0.5
        # Détermination de la composante horizontale de la vitesse (vx), basée sur la distance horizontale qx et le temps total t
        vx = qx / t
        # Détermination de la composante verticale de la vitesse initiale, corrigeant pour la gravité
        vy = qy / t + g * t / 2
        # On vérifie que la hauteur atteinte à la position X (objectif final) est suffisante (sinon, collision avec le sol ou échec)
        if calc(vy, X / vx) < Y - eps:
            return 0
        # Pour chaque obstacle dans la liste, on vérifie les intersections avec la trajectoire
        for L, B, R, T in obstacles:
            # Calcul de la position verticale à l'abscisse L par la trajectoire, comparée aux bornes verticales de l'obstacle
            l = cmp(B, T, calc(vy, L / vx))
            # Même chose à l'abscisse R (côté droit de l'obstacle)
            r = cmp(B, T, calc(vy, R / vx))
            # Calcul de la position du sommet de la trajectoire en x et comparaison aux bornes horizontales de l'obstacle
            xh = cmp(L, R, vx * (vy / g))
            # Calcul de la hauteur maximale atteinte et comparaison aux bornes verticales de l'obstacle
            yh = cmp(B, T, calc(vy, vy / g))
            # Si la trajectoire passe à l'intérieur de l'obstacle (intersection relevée)
            if l * r <= 0 or (not xh and yh * l <= 0):
                break  # On sort immédiatement, trajectoire bloquée
        else:
            # Si la boucle s'est terminée sans interruption, aucune collision n'a été trouvée
            return 1
    # Si aucune trajectoire valide n'a été trouvée, on retourne 0
    return 0

# Déclaration et initialisation de constantes physiques et de la tolérance de calcul
g = 9.8        # Accélération due à la gravité (mètres par seconde carré)
eps = 1e-10    # Petite valeur pour compenser les imprécisions des calculs sur flottants

# Lecture de la première ligne d'entée : le nombre d'obstacles (N), la vitesse initiale (V), la cible X et Y
N, V, X, Y = map(int, input().split())

# Création d'une liste vide pour stocker les obstacles valides
obstacles = []
# Boucle de lecture de chaque obstacle
for i in range(N):
    # Lecture des coordonnées de l'obstacle sous la forme (L, B, R, T)
    L, B, R, T = map(int, input().split())
    # On ne conserve que les parties des obstacles qui sont avant la cible X (sinon, ils sont hors du chemin)
    if L < X:
        obstacles.append((L, B, min(R, X), T))  # Si un obstacle dépasse X, on le tronque à X côté droit

# On essaie de vérifier d'abord s'il existe une trajectoire directe franchissable vers le point (X, Y) sans heurter un obstacle
if check(X, Y):
    print('Yes')  # Si c'est possible, on affiche 'Yes'
    exit()        # On termine le programme immédiatement

# Sinon, on essaye autour des coins supérieurs des obstacles (généralement pour frôler le dessus d'un obstacle)
for L, B, R, T in obstacles:
    # S'il n'y a pas de largeur (L=0 ou R=0), on ignore
    if not L or not R:
        continue
    # On essaye d'atteindre les coins supérieurs gauche ou droit de l'obstacle
    if check(L, T) or check(R, T):
        print('Yes')  # Si un passage est possible, on affiche 'Yes'
        exit()        # Et on termine immédiatement

# Si aucune solution n'a été trouvée, on affiche 'No'
print('No')