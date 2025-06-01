def calculer_somme_maximale():
    """
    Cette fonction lit six entiers depuis l'entrée standard,
    répartis en deux groupes de tailles différentes (4 et 2).
    Elle trie les deux groupes en ordre décroissant, sélectionne
    les trois plus grands éléments du premier groupe et le plus
    grand élément du second groupe, puis calcule et affiche la
    somme de ces valeurs sélectionnées.
    """
    # Lecture des six entiers depuis l'entrée standard
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    f = int(input())

    # Regroupement des quatre premiers entiers dans une liste 'm'
    m = [a, b, c, d]
    # Regroupement des deux derniers entiers dans une liste 'n'
    n = [e, f]

    # Tri des listes 'm' et 'n' en ordre décroissant pour obtenir les plus grandes valeurs en premier
    k = sorted(m, reverse=True)
    l = sorted(n, reverse=True)

    # Sélection des trois plus grands éléments de la liste 'k' (issue de 'm')
    x = k[:3]
    # Sélection de l’élément le plus grand de la liste 'l' (issue de 'n')
    y = l[:1]

    # Calcul de la somme des éléments sélectionnés et affichage du résultat
    print(sum(x) + sum(y))

# Appel de la fonction principale pour exécuter le programme
calculer_somme_maximale()