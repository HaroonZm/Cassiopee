def main():
    """
    Programme principal qui lit des paires de chaînes de caractères depuis l'entrée standard,
    puis calcule et affiche le nombre de correspondances exactes (hit) et de correspondances de caractères
    mal positionnés (br) pour chaque paire, jusqu'à ce que la paire '0 0' soit rencontrée.

    La correspondance exacte (hit) correspond au nombre de caractères aux mêmes positions dans les deux chaînes.
    La correspondance mal positionnée (br) correspond au nombre de caractères présents dans les deux chaînes,
    mais aux positions différentes.
    """
    while True:
        # Lecture d'une ligne de l'entrée standard, division en deux chaînes a et b
        a, b = input().split(' ')

        # Condition d'arrêt: si les deux chaînes sont '0', on sort de la boucle
        if a == '0' and b == '0':
            break

        # Conversion des chaînes en listes pour pouvoir accéder aux caractères par indices
        a = list(a)
        b = list(b)

        br = 0  # Compteur pour les correspondances mal positionnées
        hit = 0  # Compteur pour les correspondances exactes

        # Parcours des caractères de la deuxième liste avec leur index
        for i, data in enumerate(b):
            # Vérification si le caractère data existe dans la liste a
            if data in a:
                # Si le caractère est aussi à la même position, on compte un hit
                if a[i] == data:
                    hit += 1
                else:
                    # Sinon, si le caractère est présent mais pas à la même position, on compte un br
                    br += 1

        # Affichage du nombre de hits et de br pour la paire lue
        print(hit, br)


if __name__ == '__main__':
    main()