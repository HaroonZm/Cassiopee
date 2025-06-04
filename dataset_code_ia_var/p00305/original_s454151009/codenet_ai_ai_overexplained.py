from sys import stdin  # Importe le module 'stdin' du package 'sys', qui permet de lire l'entrée standard (typiquement, ce que l'utilisateur tape au clavier ou redirige vers le script)
from itertools import accumulate  # Importe la fonction 'accumulate' du module 'itertools'. Cette fonction permet de calculer les sommes cumulées sur une séquence (ex: [1,2,3] -> [1,3,6])

def solve():  # Définit une fonction nommée 'solve'. Les fonctions servent à regrouper des blocs de code réutilisables.
    file_input = stdin  # Assigne à la variable 'file_input' le flux d'entrée standard (permet d'utiliser 'readline' pour lire les lignes de l'entrée)

    N = int(file_input.readline())  # Lit la première ligne de l'entrée, la convertit en entier et assigne cette valeur à la variable 'N'
    # 'N' représentera généralement le nombre de lignes suivantes (par convention dans de nombreux problèmes)

    G = tuple(tuple(map(int, line.split())) for line in file_input)  
    # Lit toutes les lignes restantes de l'entrée standard avec une boucle 'for'
    # Pour chaque ligne, 'line.split()' découpe la chaîne en sous-chaînes selon les espaces (par défaut) pour obtenir une liste de chaînes
    # 'map(int, ...)' transforme chacune de ces sous-chaînes en entiers
    # 'tuple(...)' convertit ce résultat (un itérable d'entiers) en un tuple d'entiers (une séquence immuable)
    # Le résultat final est un tuple de tuples, représentant une grille ou matrice d'entiers de dimension (N x M)

    # accumulated rows - on va créer les sommes partielles (cumulées) de chaque ligne
    # Cela veut dire que pour chaque ligne du tableau G, on prendra les valeurs successives de la somme de gauche à droite
    ar = (
        (0,) + tuple(accumulate(line))  
        for line in G
    )
    # Pour chaque ligne, 'accumulate' va générer les préfixes de somme (par exemple, [1,2,3] -> [1,3,6])
    # On ajoute un 0 au début de chaque séquence ('(0,)' + ...), car souvent, pour les calculs de sous-tableaux, on veut une base 0
    # On construit ainsi, pour toutes les lignes du tableau G, un générateur d'objets tuple

    # accumulated columns - crée les sommes cumulées sur les COLONNES, c'est-à-dire pour chaque colonne, les différentes préfixes de sommes par lignes
    ac = (
        (0,) + tuple(accumulate(line)) 
        for line in zip(*G)
    )
    # 'zip(*G)' transpose la matrice G : cela rassemble les éléments d'indice identique de chaque ligne pour générer chaque colonne sous forme de tuple
    # On fait ensuite, pour chaque colonne, le même calcul de sommes cumulées que pour les lignes (ajout d'un 0 devant)
    # Cela construit un générateur qui donne pour chaque colonne ses préfixes de sommes

    ac_1 = next(ac)  
    # On extrait la première valeur du générateur ac (en général, la 1ère colonne cumulée) et on l'assigne à ac_1
    # C'est utile pour des comparaisons ultérieures colonne à colonne

    ac = tuple(zip(*ac))
    # Ici, on reconstruit (via un 'zip' dépaqueté et tuple) la structure des préfixes somme colonne par colonne et la transpose 
    # pour retrouver une structure "ligne par ligne" (chaque élément est maintenant le préfixe cumulatif sur la colonne à un moment donné sur la matrice)
    # Cela permet d'accéder facilement à la somme cumulée des colonnes à chaque ligne

    ans = 0  # Initialise 'ans', la variable qui va contenir la réponse finale (le maximum trouvé). On démarre à 0.

    # On parcourt par double boucle tous les couples d'indices (i,j) correspondant à différents sous-tableaux ou sous-matrices.
    for i, t1 in enumerate(zip(G, ar, ac, ac_1)):  
        # 'enumerate' génère un indice 'i' (allant de 0 au nombre de lignes) et 't1' qui contient, pour la i-ème ligne :
        # - G_i : la i-ème ligne de la grille
        # - ar_i : la i-ème ligne des préfixes cumulés ligne
        # - ac_i : la i-ème ligne de la transposée des préfixes colonnes
        # - ac_1i : la i-ème valeur de la première colonne cumulée

        G_i, ar_i, ac_i, ac_1i = t1  # On assigne à chaque variable le bon composant du tuple t1
        ar_ii = ar_i[i]  # 'ar_ii' est la somme cumulée jusqu'à la colonne i dans la ligne i

        # On va parcourir, à partir de la ligne i jusqu'à la fin, pour couvrir toutes les sous-matrices débutant ligne i
        for j, t2 in enumerate(zip(G[i:], ar_i[i+1:], ac[i+1:], ac_1[i+1:]), start=i):
            # 'G[i:]' donne toutes les lignes à partir de la i-ème
            # 'ar_i[i+1:]' donne les préfixes sommes de la ligne i, de la colonne i+1 vers la droite
            # 'ac[i+1:]' donne, pour toute colonne à droite de i, la valeur cumulée des colonnes sur la ligne
            # 'ac_1[i+1:]' donne les valeurs cumulées sur la première colonne à droite de i
            # 'enumerate' génère un indice j (démarrant à i)

            G_j, ar_ij, ac_j, ac_1j = t2  # On assigne à chaque variable le bon composant du tuple t2

            # On calcule la somme cumulée sur la ligne i pour la portion allant de position i+1 à j
            if ar_ij - ar_ii > ans:
                ans = ar_ij - ar_ii  # On met à jour la réponse si on trouve une somme plus grande que le maximum courant

            if i == j:
                continue  # Si on est sur la diagonale (i == j), on passe à l'itération suivante, car les sous-matrices de taille 1x1 sont déjà traitées

            col_max = ac_1j - ac_1i  
            # On calcule la différence cumulative sur la première colonne entre la ligne j et i, ce qui donne la somme totale sur cette colonne de i+1 à j

            for ac_jk, ac_ik, G_ik, G_jk in zip(ac_j, ac_i, G_i[1:], G_j[1:]):
                # On itère simultanément :
                # - ac_jk : cumul colonne k sur la ligne j+1
                # - ac_ik : cumul colonne k sur la ligne i
                # - G_ik : valeur de la ligne i et colonne k (commence à 1 pour ignorer la diagonale de départ)
                # - G_jk : valeur de la ligne j et colonne k

                col = ac_jk - ac_ik
                # Différence entre les cumuls colonnes sur la portion i à j, ce qui donne la somme totale sur cette colonne, entre les lignes i+1 à j

                if col_max > 0:
                    c_ans = col_max + col
                    if c_ans > ans:
                        ans = c_ans
                    # Si on a déjà une somme cumulée positive sur la première colonne, on voit si en lui ajoutant la colonne courante on bat le maximal courant
                else:
                    if col > ans:
                        ans = col
                    # Sinon, on teste si la somme sur la colonne courante bat le maximal

                t_col_max = col_max + G_ik + G_jk
                if t_col_max > col:
                    col_max = t_col_max
                else:
                    col_max = col
                # On met à jour col_max, qui conserve le meilleur score courant pour une extension de sous-matrice/colonne
                # Si en prolongeant la sous-matrice à la colonne courante on améliore le score (en incluant les deux nouvelles cases concernées), on prend ce score
                # Sinon, on recommence la somme à partir de la colonne courante

    print(ans)  # On affiche la valeur maximale trouvée au final

solve()  # Appel effectif de la fonction solve pour exécuter tout le traitement ci-dessus