import sys  # Importe le module 'sys' qui fournit des fonctions et des objets utilisés pour interagir fortement avec l'interpréteur Python

# Redéfinit la fonction d'entrée 'input' pour lire une ligne à partir de l'entrée standard (sys.stdin)
# La méthode readline() lit une seule ligne jusqu'à un saut de ligne (\n)
# La méthode rstrip() supprime tout caractère d'espacement ou retour à la ligne à droite de la chaîne lue
input = lambda: sys.stdin.readline().rstrip()

# Fixe la limite maximale de récursivité du programme à 10 millions (10**7)
# Ceci permet de gérer des appels récursifs profonds dans le cas où cela est nécessaire
sys.setrecursionlimit(10**7)

# Définit une constante INF (infinie pour ce contexte) égale à 10 milliards (10**10)
INF = 10**10

# Définit plusieurs fonctions utilitaires pour faciliter la lecture d'entrée et la conversion des types

# Fonction I : lit une ligne d'entrée et la convertit en entier
def I():
    return int(input())

# Fonction F : lit une ligne d'entrée et la convertit en flottant
def F():
    return float(input())

# Fonction S : lit une ligne d'entrée telle quelle (chaine de caractères)
def S():
    return input()

# Fonction LI : lit une ligne, la découpe par espace (split), et convertit chaque élément en entier pour retourner une liste d'entiers
def LI():
    return [int(x) for x in input().split()]

# Fonction LI_ : lit une ligne, découpe par espace, convertit chaque élément en entier puis soustrait 1 pour chaque (typiquement pour indices base 0), retourne une liste d'entiers
def LI_():
    return [int(x)-1 for x in input().split()]

# Fonction LF : lit une ligne, découpe par espace, convertit chaque élément en flottant, retourne une liste de flottants
def LF():
    return [float(x) for x in input().split()]

# Fonction LS : lit une ligne et la découpe en liste de chaînes, séparées par les espaces
def LS():
    return input().split()

# Définition de la fonction principale 'resolve' qui contient la logique principale de l'algorithme
def resolve():

    # Boucle infinie pour traiter plusieurs jeux de test jusqu'à la condition d'arrêt
    while True:

        # Lit trois entiers depuis l'entrée : n (nombre de coupes à effectuer), w (largeur initiale du gâteau), d (profondeur initiale du gâteau)
        n, w, d = LI()

        # Condition d'arrêt : si toutes les valeurs sont nulles, on quitte la boucle
        if n == 0 and w == 0 and d == 0:
            break  # Interrompt la boucle

        # Création d'une liste nommée 'cake' qui va contenir la taille des différentes parts de gâteau (pavés rectangulaires)
        cake = []

        # Ajoute une part de gâteau représentant le gâteau entier initial (avec la largeur w et profondeur d)
        cake.append([w, d])

        # Pour chaque coupe à effectuer (on fait n coupes)
        for _ in range(n):

            # Récupère les informations sur la coupe courante sous forme d'une liste de deux entiers 
            # ps[0] correspond à l'indice (1-based) de la part à couper, ps[1] représente la longueur du périmètre depuis un certain point pour faire la coupe
            ps = LI()

            # L'indice de la part à couper dans la liste 'cake' est 'p'
            # Comme la liste 'cake' utilise une indexation à base 0 mais les entrées sont à base 1, on soustrait 1
            p = ps[0] - 1

            # La distance le long du périmètre à laquelle la coupe doit être faite
            s = ps[1]

            # On récupère les dimensions (largeur et profondeur) de la part de gâteau qu'on va couper dans la liste 'cake'
            cake_w = cake[p][0]  # Largeur de la part à couper
            cake_d = cake[p][1]  # Profondeur de la part à couper

            # Pour gérer les cas où la distance 's' dépasse le périmètre de la part, on la ramène dans l'intervalle de [0, périmètre)
            s = s % ((cake_w + cake_d) * 2)  # Le périmètre d’un rectangle est deux fois la somme largeur + profondeur

            # Selon la valeur de 's', la coupe se situe sur un des quatre côtés de la part rectangulaire
            # On détermine où la coupe a lieu (côté haut, côté droit, bas, gauche) puis on calcule la taille des deux nouvelles parts

            # Coupe sur le côté en haut (largeur)
            if s < cake_w:
                # Produit deux nouveaux gâteaux
                # L'une aura comme largeur min(s, cake_w-s) et même profondeur
                new_cake_s = [min(s, cake_w - s), cake_d]  # Petite part
                new_cake_l = [max(s, cake_w - s), cake_d]  # Grande part

            # Coupe sur le côté droit (profondeur)
            elif cake_w < s < cake_w + cake_d:
                # On calcule la taille de la coupe par rapport au côté droit (profondeur)
                new_cake_s = [cake_w, min(s - cake_w, cake_w + cake_d - s)]
                new_cake_l = [cake_w, max(s - cake_w, cake_w + cake_d - s)]

            # Coupe sur le côté du bas (largeur, mais de l'autre côté)
            elif cake_w + cake_d < s < cake_w + cake_d + cake_w:
                # Coupe opposée à la première
                new_cake_s = [min(s - (cake_w + cake_d), cake_w + cake_d + cake_w - s), cake_d]
                new_cake_l = [max(s - (cake_w + cake_d), cake_w + cake_d + cake_w - s), cake_d]

            # Coupe sur le côté gauche (profondeur opposée)
            else:
                new_cake_s = [cake_w, min(s - (cake_w + cake_d + cake_w), cake_w + cake_d + cake_w + cake_d - s)]
                new_cake_l = [cake_w, max(s - (cake_w + cake_d + cake_w), cake_w + cake_d + cake_w + cake_d - s)]

            # Après la coupe, on enlève la part que l’on vient de couper de la liste 'cake'
            del cake[p]  # Supprime la part à l’indice p (celle coupée)

            # Ajoute les deux nouvelles parts de gâteau générées par la coupe à la liste
            cake.append(new_cake_s)  # Ajoute la plus petite part résultat
            cake.append(new_cake_l)  # Ajoute la plus grande part résultat

        # On calcule la surface de chaque part de gâteau restante en multipliant largeur * profondeur pour chaque part dans 'cake'
        # Ensuite, on les trie par ordre croissant pour l'affichage
        print(*sorted([i[0] * i[1] for i in cake]))  # L'étoile (*) permet d'imprimer tous les éléments de la liste séparés par des espaces

# Condition qui permet d'exécuter la fonction 'resolve' uniquement si le script est exécuté directement (et pas importé comme module)
if __name__ == '__main__':
    resolve()  # Appelle la fonction principale