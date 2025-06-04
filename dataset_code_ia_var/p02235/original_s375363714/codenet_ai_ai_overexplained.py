# Définition de la fonction lcs, qui calcule la longueur de la plus longue sous-séquence commune ("Longest Common Subsequence", LCS)
# entre deux chaînes de caractères X et Y.
def lcs(X, Y):
    # Création d'une liste vide L. Cette liste va garder les indices correspondants de X
    # pour la construction de la sous-séquence commune avec Y.
    L = []

    # Boucle pour parcourir chaque caractère 'yk' de la chaîne Y, un par un.
    # 'yk' est une lettre de Y.
    for yk in Y:
        # Initialisation de la variable prev_idx à -1. Cela servira à indiquer le point de départ
        # pour effectuer la prochaine recherche dans X, à travers la méthode find.
        prev_idx = -1

        # Parcours de chaque élément l dans la liste L ainsi que son indice l_idx.
        # enumerate(L) produit à chaque tour l'index l_idx et la valeur l correspondante.
        for l_idx, l in enumerate(L):
            # Recherche de la position (index) du caractère yk dans la chaîne X, 
            # en partant juste après prev_idx pour éviter de reprendre le même caractère.
            x_idx = X.find(yk, prev_idx + 1)

            # Si x_idx est inférieur à 0, cela signifie que le caractère yk 
            # n'a pas été trouvé à partir de prev_idx + 1, donc on interrompt la boucle.
            if x_idx < 0:
                break

            # Mise à jour de la valeur à l'indice l_idx dans la liste L.
            # Ce sera le minimum entre l'ancien index (l) et le nouvel index trouvé (x_idx).
            # Cela permet de trouver la plus petite position possible dans X pour ce caractère.
            L[l_idx] = min(l, x_idx)

            # Mise à jour de prev_idx pour le prochain passage. prev_idx prend la valeur l,
            # qui était l'ancienne position correspondante dans X. 
            # Cela permet de s'assurer que les sous-séquences sont dans l'ordre croissant des indices dans X.
            prev_idx = l

        # Le "else" d'une boucle "for" en Python s'exécute seulement
        # si la boucle n'a PAS été interrompue par un 'break'.
        # Cela signifie ici que chaque caractère de L a trouvé un match dans X,
        # on peut donc tenter d'étendre la chaîne commune.
        else:
            # Recherche d'un nouvel index de yk dans X, après prev_idx+1.
            x_idx = X.find(yk, prev_idx + 1)

            # Si un index est trouvé (x_idx >= 0), on ajoute ce nouvel index à la fin de L.
            # Cela permet d'ajouter un nouveau caractère valide à la sous-séquence commune potentielle.
            if x_idx >= 0:
                L.append(x_idx)

    # La fonction retourne la taille de la liste L.
    # La longueur de L correspond à la taille de la plus longue sous-séquence commune trouvée.
    return len(L)

# Définition de la fonction main, qui gère les entrées/sorties du programme.
def main():
    # Lecture d'un entier q au clavier, qui indique combien de paires de chaînes seront fournies.
    # Utilisation de int() pour convertir l'entrée utilisateur (texte) en un nombre entier.
    q = int(input())

    # Boucle d'itération q fois, une fois pour chaque paire (X, Y).
    for _ in range(q):
        # Lecture de la première chaîne, X, au clavier.
        X = input()

        # Lecture de la seconde chaîne, Y, au clavier.
        Y = input()

        # Calcul de la taille de la plus longue sous-séquence commune entre X et Y,
        # en appelant la fonction lcs avec ces deux chaînes.
        # Le résultat est affiché avec print.
        print(lcs(X, Y))

# Condition spéciale qui vérifie si ce fichier est exécuté comme un programme principal,
# et non importé en tant que module dans un autre script.
if __name__ == "__main__":
    # On importe sys et io, mais ils ne sont pas utilisés dans ce code.
    import sys, io
    # Appel de la fonction main pour démarrer le programme.
    main()