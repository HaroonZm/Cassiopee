def solve():
    # Demander à l'utilisateur une entrée représentant le nombre d'éléments dans la liste
    N = int(input())  # Convertir l'entrée (qui est une chaîne de caractères) en entier

    # Lire une ligne d'entrée contenant N entiers, séparés par des espaces
    # Diviser cette ligne en une liste de chaînes de caractères grâce à split()
    # Puis pour chaque élément (chaîne), la convertir explicitement en entier grâce à int()
    # Enfin, cet ensemble d'entiers est placé dans une liste nommée 'a'
    a = [int(i) for i in input().split()]

    # Lire une nouvelle entrée : le nombre de requêtes (souvent associé à des opérations ou questions à traiter)
    Q = int(input())

    # Créer une version triée de la liste 'a' pour obtenir l'ordre attendu (ordre croissant)
    sort_a = sorted(a)
    # 'sorted' crée une nouvelle liste triée, ne modifie pas la liste originale

    # Initialiser un compteur, qui sera utilisé pour comptabiliser le nombre d'éléments
    # qui ne sont pas à leur position correcte (comparé à la version triée)
    judge = 0

    # Boucle pour parcourir chaque position de la liste (de l'index 0 à N-1)
    for i in range(N):
        # Comparer si l'élément à la position i dans la liste originale 'a'
        # est différent de l'élément à la même position dans la liste triée 'sort_a'
        if a[i] != sort_a[i]:
            # Si les deux éléments diffèrent, cela signifie que la position n'est pas correcte
            # On incrémente alors le compteur 'judge' de 1
            judge += 1

    # Si 'judge' vaut exactement 0, cela signifie que tous les éléments sont à la bonne position
    # c'est-à-dire que la liste est déjà triée
    if judge == 0:
        # On affiche 0 puisque aucune opération n'est nécessaire
        print(0)
    else:
        # Si la liste n'est pas triée, on va alors effectuer jusqu'à Q opérations (maximum)
        for i in range(Q):
            # Pour chaque opération, on demande deux entiers sur une même ligne,
            # représentant les indices des deux éléments à échanger ('swap')
            # 'map' permet d'appliquer int à chaque valeur renvoyée par split()
            x, y = map(int, input().split())

            # En Python, les indices commencent à 0, mais souvent les indices donnés sont à partir de 1
            # Donc on soustrait 1 à chaque valeur pour avoir le bon indice
            # Sauvegarder la valeur en position x-1 temporairement
            tmp = a[x - 1]

            # Effectuer l'échange entre les deux éléments indiqués, à l'aide de la variable temporaire
            a[x - 1] = a[y - 1]
            a[y - 1] = tmp

            # Vérifier l'impact de cet échange sur le nombre d'éléments mal placés 'judge'

            # Si après l'échange, la valeur en x-1 correspond à la bonne (dans sort_a), et que
            # avant l'échange, celle placée à y-1 n'était pas la bonne pour x-1, on réduit judge
            if a[x - 1] == sort_a[x - 1] and a[y - 1] != sort_a[x - 1]:
                judge -= 1

            # Si après l'échange, la valeur en x-1 ne correspond pas, mais,
            # celle en y-1 était la bonne valeur pour x-1, alors on augmente judge
            if a[x - 1] != sort_a[x - 1] and a[y - 1] == sort_a[x - 1]:
                judge += 1

            # Même principe, on vérifie l'élément à y-1 : si après l'échange il correspond et qu'avant non,
            # on diminue judge
            if a[y - 1] == sort_a[y - 1] and a[x - 1] != sort_a[y - 1]:
                judge -= 1

            # Si après l'échange il ne correspond pas, mais que la valeur avant échange était correcte, on augmente judge
            if a[y - 1] != sort_a[y - 1] and a[x - 1] == sort_a[y - 1]:
                judge += 1

            # Après cette mise à jour, si judge est retombé à 0 (tous les éléments sont à leurs bonnes places)
            if judge == 0:
                # On affiche l'opération courante (attention : numéro d'opération = index du for + 1)
                print(i + 1)
                # On quitte la boucle car on a réussi à trier la liste
                break
        else:
            # Si l'on n'a jamais atteint judge == 0 après toutes les opérations,
            # alors la liste n'est pas triée même après Q échanges
            print(-1)

# Ce bloc spécial vérifie si ce fichier est exécuté directement (pas importé comme module)
# Si tel est le cas, alors la fonction 'solve' sera appelée pour exécuter ce programme
if __name__ == '__main__':
    solve()