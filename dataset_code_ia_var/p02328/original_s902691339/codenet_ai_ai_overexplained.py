import sys  # On importe le module sys pour accéder aux arguments de la ligne de commande (bien que non utilisés ici, c'est standard).

def solve(heights):
    # Cette fonction prend une liste d'entiers appelée 'heights', où chaque entier représente la hauteur d'une barre dans l'histogramme.
    # L'objectif de cette fonction est de trouver la plus grande aire rectangulaire pouvant être formée dans l'histogramme.

    h_len = len(heights)  # Nombre total de barres dans l'histogramme.
    left = [-1] * h_len  # Création d'une liste qui va stocker, pour chaque barre, l'indice de la première barre à gauche qui est plus basse.
    right = [-1] * h_len  # Création d'une liste qui va stocker, pour chaque barre, l'indice de la première barre à droite qui est plus basse.
    stack = []  # Initialisation d'une pile vide ; sera utilisée pour garder les indices et hauteurs des barres pendant le parcours.

    # PREMIÈRE BOUCLE : On parcourt toutes les barres de gauche à droite pour trouver le bord gauche de chaque plus grand rectangle possible.
    for i in range(h_len):  # On itère sur chaque indice de hauteur dans la liste 'heights'.
        if not stack:
            # Si la pile est vide, cela signifie qu'il n'y a pas encore de barre à gauche,
            # donc le bord gauche du rectangle pour la barre courante sera zéro (tout à gauche du tableau).
            left[i] = 0
        else:
            # Sinon, on cherche la première barre à gauche qui est strictement plus basse que la barre courante.
            # On fait cela en dépilant toutes les barres dont la hauteur est supérieure ou égale à la hauteur courante, car elles ne délimitent pas la zone rectangulaire.
            while stack and stack[-1][1] >= heights[i]:
                stack.pop()  # On retire le sommet de la pile tant qu'il y a un conflit de hauteur.
            # Après la boucle, soit la pile est vide, soit elle contient au sommet une barre plus basse. On prend donc l'indice de cette dernière et on y ajoute 1.
            left[i] = stack[-1][0] + 1 if stack else 0  # Si la pile est vide, il n'y a rien à gauche => 0.
        # On empile le couple (indice courant, hauteur courante) pour les itérations suivantes.
        stack.append((i, heights[i]))

    # On vide la pile pour le parcours dans le sens opposé (droite à gauche).
    stack = []

    # DEUXIÈME BOUCLE : On parcourt les barres de droite à gauche pour trouver le bord droit de chaque rectangle pour chaque barre.
    for i in range(h_len - 1, -1, -1):  # On part de la fin et on va jusqu'au début inclusivement, en décrémentant.
        if not stack:
            # Si la pile est vide, cela signifie que le bord droit est à l'extérieur des limites, donc à l'indice h_len.
            right[i] = h_len
        else:
            # Pareil que précédemment, mais vers la droite : on enlève de la pile toutes les barres plus hautes ou égales à la barre courante.
            while stack and stack[-1][1] >= heights[i]:
                stack.pop()
            # Si la pile n'est pas vide, le sommet donne l'indice de la première barre plus basse à droite.
            right[i] = stack[-1][0] if stack else h_len  # Si la pile est vide, tout à droite du tableau.
        # On empile la barre courante pour les prochaines vérifications.
        stack.append((i, heights[i]))

    # On calcule l'aire maximale pour chaque barre. L'aire possible pour une barre donnée est sa hauteur multipliée par la largeur :
    # largeur = indice droit - indice gauche.
    # On fait un calcul pour chaque triple (hauteur, bord gauche, bord droit).
    area = [h * (r - l) for h, l, r in zip(heights, left, right)]

    # On renvoie la plus grande aire trouvée parmi toutes les aires calculées.
    return max(area)


def main(args):
    # Fonction principale gérant l'entrée et la sortie standard. Prend en argument args (liste non utilisée ici).
    _ = input()  # On lit la première ligne d'entrée, mais on ne l'utilise pas (souvent la taille, ici inutile car input().split() suffit).
    heights = [int(h) for h in input().split()]  # On lit la deuxième ligne, on la divise en entiers pour obtenir la liste des hauteurs.
    ans = solve(heights)  # On appelle la fonction solve pour obtenir la plus grande aire de rectangle.
    print(ans)  # On affiche le résultat à la sortie standard (console).


if __name__ == '__main__':
    # Point d'entrée du script Python. Cette condition vérifie que ce script est exécuté directement (et non importé comme module dans un autre script).
    main(sys.argv[1:])  # On passe les arguments de la ligne de commande (sauf le nom du script) à main.