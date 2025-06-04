import math  # Importe le module math qui fournit des fonctions mathématiques utiles, comme sinus et cosinus.

# On définit deux indices pour accéder plus facilement aux coordonnées x et y dans un tuple (x, y).
x = 0  # L'indice 0 représente la coordonnée x.
y = 1  # L'indice 1 représente la coordonnée y.

# On définit les deux points qui formeront le segment initial à transformer.
p1 = (0, 0)      # Le point de départ du segment, situé à l'origine du plan (abscisse 0, ordonnée 0).
p2 = (100, 0)    # Le point d'arrivée du segment, situé 100 unités à droite le long de l'axe x.

# Calcul de la valeur du sinus et du cosinus de 60 degrés
# math.radians(60) convertit 60 degrés en radians car math.sin/cos attend une valeur en radians.
sin60 = math.sin(math.radians(60))  # Calcul du sinus de 60 degrés en radians.
cos60 = math.cos(math.radians(60))  # Calcul du cosinus de 60 degrés en radians.

# Lecture du niveau de récursion (nombre d'itérations) pour la courbe de Koch
n = int(input())  # On demande à l'utilisateur d'entrer un entier, puis on le convertit en entier avec int().

# Définition de la fonction récursive pour dessiner la courbe de Koch.
# n : le niveau de récursion restant.
# p1 : point de départ du segment actuel (tuple de 2 flottants).
# p2 : point d'arrivée du segment actuel (tuple de 2 flottants).
def kock(n, p1, p2):
    # Cas de base : si le niveau de récursion est 0, la fonction s'arrête (ne fait rien de plus).
    # Cela empêche la récursion infinie.
    if n == 0:
        return  # Quitte la fonction sans exécuter le reste.

    # Pour chaque segment (p1, p2), il faut calculer trois nouveaux points :
    # s, t, et u.
    # s : point situé à 1/3 de la longueur entre p1 et p2.
    # t : point situé à 2/3 de la longueur entre p1 et p2.
    # u : point formant le sommet du triangle équilatéral construit entre s et t.

    # Initialisation des variables s, t, u.
    # On crée des tuples (0, 0) juste pour les déclarer mais en réalité, ce n'est pas obligatoire.
    s = (0, 0)
    t = (0, 0)
    u = (0, 0)

    # Calcul du point s (1/3 de la distance de p1 vers p2).
    # (2*p1 + p2)/3 pour x et y respectivement.
    s = (
        (2 * p1[x] + 1 * p2[x]) / 3,  # Coordonnée x de s
        (2 * p1[y] + 1 * p2[y]) / 3   # Coordonnée y de s
    )

    # Calcul du point t (2/3 de la distance de p1 vers p2).
    # (p1 + 2*p2)/3 pour x et y respectivement.
    t = (
        (1 * p1[x] + 2 * p2[x]) / 3,  # Coordonnée x de t
        (1 * p1[y] + 2 * p2[y]) / 3   # Coordonnée y de t
    )

    # Calcul du point u, qui forme le sommet du triangle équilatéral au-dessus du segment (s, t).
    # Les formules utilisent la rotation d'un point autour d'un autre.
    # Pour construire le triangle équilatéral, on fait tourner le vecteur (t-s) de +60° autour de s.
    # La nouvelle position u est donc donnée par les formules de rotation en coordonnées cartésiennes :
    u = (
        (t[x] - s[x]) * cos60 - (t[y] - s[y]) * sin60 + s[x],  # Coordonnée x de u après rotation
        (t[x] - s[x]) * sin60 + (t[y] - s[y]) * cos60 + s[y]   # Coordonnée y de u après rotation
    )

    # Appels récursifs sur les 4 segments formés : [p1,s], [s,u], [u,t], et [t,p2].

    # Premier segment : de p1 à s
    kock(n - 1, p1, s)
    # On affiche le point s avec une précision de 8 chiffres après la virgule.
    print('{:.8f} {:.8f}'.format(s[x], s[y]))

    # Deuxième segment : de s à u
    kock(n - 1, s, u)
    # On affiche le point u avec une précision de 8 chiffres après la virgule.
    print('{:.8f} {:.8f}'.format(u[x], u[y]))

    # Troisième segment : de u à t
    kock(n - 1, u, t)
    # On affiche le point t avec une précision de 8 chiffres après la virgule.
    print('{:.8f} {:.8f}'.format(t[x], t[y]))

    # Quatrième segment : de t à p2
    kock(n - 1, t, p2)

# À ce point, on est prêt à lancer la génération de la courbe de Koch.

# On affiche d'abord le point de départ initial (p1), formaté à 8 chiffres après la virgule.
print('{:.8f} {:.8f}'.format(p1[x], p1[y]))

# On appelle la fonction récursive de génération avec le niveau de récursion donné et les deux points initiaux.
kock(n, p1, p2)

# Enfin, on affiche le point d'arrivée final (p2), toujours avec 8 chiffres après la virgule.
print('{:.8f} {:.8f}'.format(p2[x], p2[y]))