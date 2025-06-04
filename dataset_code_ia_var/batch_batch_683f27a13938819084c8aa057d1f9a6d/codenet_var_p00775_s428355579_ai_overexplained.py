import math  # On importe le module "math" pour utiliser des fonctions mathématiques comme la racine carrée (sqrt).

# On entre dans une boucle infinie qui permettra d'exécuter le programme tant qu'une condition d'arrêt n'est pas rencontrée.
while True:
    # On lit une ligne saisie par l'utilisateur (sous forme de chaîne de caractères), on la découpe en deux parties,
    # puis on les convertit en entiers à l'aide de map(int, ...). On stocke ensuite ces deux entiers dans les variables r et n.
    (r, n) = map(int, raw_input().split())

    # On vérifie si la somme de r et n est égale à 0, ce qui signifie que les deux sont nuls.
    # Si c'est le cas, on arrête la boucle en utilisant l'instruction break.
    if r + n == 0:
        break

    # On crée un dictionnaire vide hs (pour "heights"), qui gardera en mémoire la hauteur maximale rencontrée pour chaque position i.
    hs = {}

    # On parcourt tous les entiers i de -22 à 22 inclus (22 + 1)
    # Cela représente peut-être la portée horizontale maximale considérée.
    for i in range(-22, 22 + 1):
        hs[i] = 0  # Pour chaque position i, on initialise la hauteur à 0.

    # On lit n fois les valeurs suivantes, car il y a n intervalles donnés à traiter.
    for _ in range(n):
        # On lit une nouvelle ligne de trois entiers (xl, xr, h) :
        # xl = borne gauche de l'intervalle (inclus)
        # xr = borne droite de l'intervalle (exclu)
        # h  = hauteur associée à cet intervalle
        (xl, xr, h) = map(int, raw_input().split())

        # Pour toutes les positions i comprises entre xl (inclus) et xr (exclu)
        for i in range(xl, xr):
            # On met à jour hs[i] pour que ce soit la hauteur maximale rencontrée à la position i.
            # Cela assure que, s'il existait déjà une hauteur à cet endroit, seule la plus grande est conservée.
            hs[i] = max(hs[i], h)

    # On initialise une variable ans à une valeur très grande (10 puissance 9).
    # Cela servira à garder la solution minimale trouvée.
    ans = 10 ** 9

    # On parcourt tous les entiers i de -r (inclus) à r (exclus)
    # Cela semble correspondre à l'intérieur d'un disque centré en 0 de rayon r.
    for i in range(-r, r):
        # On affecte la valeur de i à la variable temporaire p.
        p = i

        # Si i est strictement négatif (inférieur à 0)
        if i < 0:
            # On augmente p de 1.
            # Cela peut corriger un décalage dû à la discrétisation de l'axe.
            p += 1

        # On calcule la valeur rr qui correspond à la hauteur (hs[i]) à la position i,
        # plus le rayon r, moins la racine carrée de (r*r - p*p).
        # La racine carrée représente probablement la profondeur verticale à partir d'un cercle de rayon r.
        rr = hs[i] + r - math.sqrt(r * r - p * p)

        # On prend la valeur minimale entre la valeur actuelle de ans et rr,
        # et on met à jour ans avec cette valeur.
        ans = min(ans, rr)

    # On affiche à l'écran la valeur maximale entre 0 et ans (pour éviter d'afficher une valeur négative),
    # en la formatant avec 10 chiffres après la virgule.
    print "%.10f" % max(0, ans)