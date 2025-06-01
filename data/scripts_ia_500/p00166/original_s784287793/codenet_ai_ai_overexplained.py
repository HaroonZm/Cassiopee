from math import *  # Importation de toutes les fonctions mathématiques du module math, comme sin, cos, pi, etc.

# Définition d'une fonction nommée S qui prend un paramètre p, supposé être une liste d'angles exprimés en degrés.
def S(p):
    # La fonction retourne la somme d'une liste créée par une compréhension de liste.
    # Pour chaque élément angle dans la liste p, on fait la conversion de l'angle de degrés en radians
    # en multipliant angle par pi/180. En effet, la fonction sin attend un angle en radians.
    # On calcule ensuite le sinus de cet angle en radians.
    # Le résultat du sinus est divisé par 2, puis ajouté à la liste temporaire.
    # La fonction sum additionne tous les éléments de cette liste temporaire.
    return sum([sin(angle * pi / 180) / 2 for angle in p])

# Boucle infinie (while 1) qui ne s'arrêtera que si une condition explicite de sortie est rencontrée (break).
while 1:
    # On lit l'entrée utilisateur via input(), censée être un entier. Cette valeur est affectée à m.
    # ATTENTION : input() retourne une chaîne de caractères, donc il faudrait normalement la convertir en int.
    # Mais on suit strictement ce qui est donné.
    m = input()
    # Condition pour sortir de la boucle : si m est égal à 0, on sort avec break.
    # En Python 2, input() évalue l'entrée, donc si l'utilisateur entre 0, m est bien entier 0.
    if m == 0:
        break

    # Création de la liste p1 contenant m-1 angles, lus un par un en entier via raw_input() converti en int.
    # raw_input() est utilisé ici, ce qui correspond à Python 2.
    # On utilise une compréhension de liste qui itère i de 0 à m-2 (m-1 éléments).
    p1 = [int(raw_input()) for i in range(m - 1)]

    # On calcule l'angle manquant pour que la somme des angles soit 360 degrés.
    # sum(p1) calcule la somme des éléments de la liste p1.
    # On soustrait cette somme à 360 pour avoir l'angle manquant.
    # On ajoute cet angle manquant à la liste p1 avec append.
    p1.append(360 - sum(p1))

    # Même procédé pour la deuxième liste p2, on lit n-1 angles.
    n = input()
    p2 = [int(raw_input()) for i in range(n - 1)]

    # On complète la liste p2 en ajoutant l'angle tel que la somme soit 360.
    p2.append(360 - sum(p2))

    # Calcul des sommes s1 et s2 en appliquant la fonction S définie précédemment aux listes p1 et p2.
    s1, s2 = S(p1), S(p2)

    # Comparaison des deux sommes avec une marge de tolérance de 1e-10 pour éviter les erreurs dues à la précision des nombres flottants.
    # Si s1 est strictement supérieur à s2 de plus de 1e-10, on affiche 1.
    if s1 - s2 > 1e-10:
        print 1
    # Sinon, si s2 est strictement supérieur à s1 de plus de 1e-10, on affiche 2.
    elif s2 - s1 > 1e-10:
        print 2
    # Sinon, les deux sommes sont considérées égales à une erreur numérique proche, on affiche 0.
    else:
        print 0