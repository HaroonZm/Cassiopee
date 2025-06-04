def main():
    """
    Lit une séquence d'entiers depuis l'entrée standard.
    Le premier entier représente 'n', le nombre de valeurs suivantes.
    Les 'n' entiers suivants sont collectés dans une liste, triés, puis transformés selon une
    règle spécifique. On calcule ensuite le minimum de toutes les différences absolues possibles
    entre les éléments transformés, et on affiche ce minimum.
    """
    # Lire toutes les données de l'entrée standard, les convertir en entiers
    n, *d = map(int, open(0).read().split())

    # Trier la liste des valeurs pour les préparer au traitement suivant
    d.sort()

    # Générer une nouvelle liste 'a' :
    # - Pour chaque élément d'indice i de 'd' :
    #   - Si i est pair, on garde la valeur telle quelle
    #   - Si i est impair, on la transforme en 24 - valeur
    # On utilise 'enumerate' pour avoir accès à l'index et à la valeur.
    a = [24 - b if i & 1 else b for i, b in enumerate(d)]

    # Ajouter '0' à la liste pour inclure ce cas dans la recherche du minimum
    a.append(0)

    # Initialiser une variable 'ans' à 24 (non utilisée ensuite, probablement vestige inutile)
    ans = 24

    # Calculer toutes les différences absolues possibles entre les éléments de 'a'
    # On parcourt tous les couples d'indices i < j (pour éviter doublons et auto-écarts)
    differences = [abs(a[i] - a[j]) for i in range(n + 1)
                                      for j in range(i + 1, n + 1)]

    # Trouver le minimum de toutes ces différences et l'afficher
    print(min(differences))


if __name__ == "__main__":
    main()