import sys  # On importe le module sys pour accéder à stdin (entrée standard) permettant de lire les entrées.

# On redéfinit la fonction input pour qu'elle lise une ligne depuis l'entrée standard,
# ce qui est plus rapide que l'utilisation de la fonction input() de base en cas de nombreux appels.
input = sys.stdin.readline

def main():
    # La fonction principale va itérer indéfiniment jusqu'à rencontrer une instruction de sortie explicite (break).
    while True:
        # On lit trois entiers séparés par des espaces sur une ligne, les convertit en int et les affecte à n, w, d.
        # n = nombre de découpes, w = largeur initiale du gâteau, d = longueur initiale du gâteau.
        n, w, d = map(int, input().split())

        # Si la largeur du gâteau (w) vaut 0, cela indique la fin des données d'entrée selon l'énoncé supposé.
        if w == 0:
            break  # On sort de la boucle infinie pour terminer le programme.

        # On lit la liste des découpes. Il y a n découpes à traiter.
        # Pour chaque découpe, on lit deux entiers sur une ligne (p et s),
        # puis on créé une liste de listes où chaque sous-liste correspond à une découpe.
        cuts = [list(map(int, input().split())) for i in range(n)]

        # On initialise la liste des gâteaux (cakes) avec un seul élément.
        # Chaque élément du tableau cakes est un tuple de trois valeurs (largeur, longueur, aire).
        # Aire calculée comme produit de la largeur (w) et de la longueur (d).
        cakes = [(w, d, w*d)]

        # Pour chaque découpe, on va transformer la liste cakes en appliquant la découpe.
        for cut in cuts:
            # On extrait le numéro de pièce à découper (p),
            # et la distance (s) depuis l'origine sur le périmètre de la pièce spécifiée.
            p, s = cut

            # On retire la pièce d'indice (p-1) de la liste cakes.
            # Attention : on travaille avec un indice basé sur 1 (d'où le -1), car l'entrée est donnée de cette façon.
            # Cela nous donne la largeur (w), la longueur (d) et l'aire (wd) de la pièce sélectionnée.
            w, d, wd = cakes.pop(p-1)

            # On prend s modulo le périmètre de la pièce (qui est 2*w + 2*d),
            # ce qui permet de traiter les cas où s dépasse la longueur du périmètre.
            s = s % (w*2 + d*2)

            # Si s est supérieur à la somme de la largeur et de la longueur,
            # on enlève cette valeur (w + d) pour rebasculer s dans le bon segment du périmètre.
            if s > w + d:
                s -= w + d

            # On vérifie si le point de découpe s se trouve sur un côté de largeur (le "haut" ou le "bas").
            # Cela revient à vérifier si s est strictement plus grand que 0 ET strictement plus petit que la largeur.
            if 0 < s and s < w:
                # La longueur du premier nouveau gâteau (w1) est la longueur minimum entre s et w-s
                # Cela garantit que l'on coupe dans la largeur, et que l'on prend la plus petite section d'un côté de la coupe.
                w1 = min(s, w-s)

                # La largeur du deuxième gâteau après découpe (w2) est ce qui reste.
                w2 = w - w1

                # On ajoute deux nouvelles pièces découpées à la liste cakes.
                # Chacune a la largeur calculée (w1, w2) et la profondeur d'origine (d).
                # On calcule aussi leur aire respective.
                cakes.append((w1, d, w1*d))
                cakes.append((w2, d, w2*d))
            else:
                # Sinon, la coupe se fait sur la profondeur (d),
                # Sur le côté "gauche" ou "droit" de la pièce. On procède donc à une découpe parallèle à la longueur.
                d1 = min(w + d - s, s - w)  # On détermine la longueur d'un des côtés après découpe.

                d2 = d - d1  # La profondeur restante correspond à ce qui manque pour obtenir la partie totale.

                # On ajoute les deux nouvelles pièces découpées,
                # la largeur restant la même et la longueur étant d1 et d2, avec calcul des aires.
                cakes.append((w, d1, w*d1))
                cakes.append((w, d2, w*d2))

        # Après toutes les découpes, on trie la liste cakes selon l'aire croissante de chaque morceau.
        cakes = sorted(cakes, key=lambda x: x[2])

        len_ = len(cakes)  # On stocke la longueur de cakes pour l'utiliser dans la boucle d'affichage.

        # On parcourt chaque morceau de gâteau trié selon l'aire.
        for i in range(len_):
            _, __, area = cakes[i]  # On extrait la troisième composante (aire) du tuple.

            # On affiche l'aire du morceau, sans passer à la ligne (end="").
            print(area, end="")

            # Si ce n'est pas le dernier morceau de gâteau, on affiche aussi un espace pour séparer les aires.
            # Sinon, on passe à la ligne après avoir affiché toutes les aires.
            if i != len_ - 1:
                print(" ", end="")
            else:
                print()

# On vérifie si ce fichier est exécuté comme un script principal,
# et on appelle la fonction main() pour démarrer l'exécution principale.
if __name__ == "__main__":
    main()