def process_queries():
    """
    Lit une chaîne initiale, puis applique une série de requêtes de manipulation
    sur cette chaîne à partir des entrées utilisateur. Les opérations possibles sont :
    - Remplacer une sous-chaîne par une nouvelle sous-chaîne.
    - Inverser une sous-chaîne d'indices donnés.
    - Afficher une sous-chaîne comprise entre deux indices.

    Les requêtes sont demandées à l'utilisateur sous forme de lignes d'entrée.
    """
    # Lire la chaîne de caractères initiale
    s = input()

    # Lire le nombre de requêtes à traiter
    q = int(input())

    # Parcourir toutes les requêtes
    for _ in range(q):
        # Lecture et découpage de chaque requête
        input_list = input().split()
        o = input_list[0]  # Opération à effectuer
        a = int(input_list[1])  # Indice de début
        b = int(input_list[2])  # Indice de fin

        # Si la requête contient un quatrième élément, il s'agit d'un remplacement
        if len(input_list) == 4:
            p = input_list[3]  # Chaîne de remplacement
            # Remplacer la portion de s de a à b (inclus) par p
            s = s[:a] + p + s[b+1:]
        # Si l'opération est 'reverse', il faut inverser la sous-chaîne [a, b]
        elif o == "reverse":
            # Inverser la sous-chaîne s[a:b+1] et reconstituer la chaîne complète
            s = s[:a] + s[a:b+1][::-1] + s[b+1:]
        # Sinon, on demande simplement l'affichage de la sous-chaîne [a, b]
        else:
            print(s[a:b+1])

# Lancement du programme principal
process_queries()