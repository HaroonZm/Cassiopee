# On demande à l'utilisateur d'entrer deux entiers séparés par un espace.
# raw_input() lit une ligne depuis l'entrée standard (l'utilisateur tape au clavier).
# split() coupe la ligne entrée en une liste de sous-chaînes selon les espaces.
# map(int, ...) convertit chaque sous-chaîne de la liste en un entier.
# n recevra le premier entier (nombre d'itérations à faire), t recevra le second (une limite ou un total).
n, t = map(int, raw_input().split())

# On initialise une variable mx à 0. Cette variable va servir à mémoriser la plus grande valeur de x rencontrée jusque-là.
mx = 0
# On initialise une variable s à 0. Elle va garder une somme cumulative des x rencontrés.
s = 0

# On commence une boucle qui va s'exécuter n fois.
# xrange(n) génère une séquence de nombres entiers de 0 à n-1 (cela permet de faire la boucle le bon nombre de fois).
for i in xrange(n):
    # À chaque itération, on lit une valeur depuis l'entrée standard avec input().
    # On suppose que la valeur entrée est un entier (attention : sous Python 2, input() évalue l'entrée comme du code Python).
    x = input()

    # On met à jour la valeur maximale rencontrée jusqu'ici.
    # max(mx, x) renvoie le plus grand des deux nombres mx et x.
    mx = max(mx, x)

    # r représente le restant de t après avoir soustrait la somme cumulative s.
    r = t - s

    # Si ce restant est négatif...
    if r < 0:
        # Alors, on affiche 1. Ceci pourrait signifier que la limite t est déjà dépassée.
        print 1
    else:
        # Sinon, on calcule une valeur appelée ans.
        # r / mx : il s'agit d'un division entière (en Python 2, cela garde la partie entière).
        # On ajoute 1 au résultat de la division.
        ans = r / mx + 1

        # On regarde si le reste de la division entière de r par mx est supérieur ou égal à x actuel.
        # r % mx calcule le reste de la division de r par mx.
        if r % mx >= x:
            # Si c'est le cas, on incrémente ans de 1 supplémentaire.
            ans += 1

        # On affiche la valeur de ans calculée.
        print ans

    # On ajoute x à la somme cumulative s, pour l'utiliser à la prochaine itération.
    s += x