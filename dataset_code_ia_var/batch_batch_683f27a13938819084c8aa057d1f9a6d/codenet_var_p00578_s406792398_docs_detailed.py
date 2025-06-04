def max_segment_count():
    """
    Lit la taille d'une séquence et la séquence elle-même depuis l'entrée standard,
    puis calcule le plus grand nombre de segments contigus pouvant être formés pour
    des valeurs strictement supérieures à zéro, avec des valeurs identiques considérées dans le même lot.

    Un segment est défini comme une suite de positions consécutives contenant des valeurs supérieures à un certain seuil.
    La fonction imprime enfin ce nombre maximal de segments.
    """
    # Lecture du nombre d'éléments dans la séquence
    N = int(input())

    # Lecture de la séquence elle-même sous forme de liste d'entiers
    A = [int(a) for a in input().split()]

    # Associer chaque élément à son indice initial, pour garder trace de la position après le tri
    for i in range(N):
        A[i] = (A[i], i)

    # Liste permettant de marquer si une position est "active" (1) ou non (0)
    L = [0] * N

    # Trie la liste A par valeur décroissante tout en conservant l'indice d'origine
    A.sort(reverse=True)

    # Compteur du nombre de segments courants
    cnt = 0

    # Réponse : maximum du nombre de segments rencontrés
    ans = 0

    # Parcours de tous les éléments après le tri (par valeur décroissante)
    for i in range(N):
        # Ajoute une nouvelle position active, donc le nombre de segments augmente d'un
        cnt += 1
        # Marque l'indice courant comme actif
        L[A[i][1]] = 1

        # Si la position à gauche existe et est active, cela fusionne deux segments donc on décrémente
        if A[i][1] > 0 and L[A[i][1] - 1] == 1:
            cnt -= 1
        # Si la position à droite existe et est active, cela fusionne deux segments donc on décrémente
        if A[i][1] < N - 1 and L[A[i][1] + 1] == 1:
            cnt -= 1

        # Si la valeur courante est la même que la suivante, on continue sans mettre à jour la réponse
        if i < N - 1 and A[i][0] == A[i + 1][0]:
            continue

        # Si la valeur courante est 0, on ne peut plus former de segments, on arrête la boucle
        if A[i][0] == 0:
            break

        # Mise à jour du maximum de segments rencontrés
        ans = max(ans, cnt)

    # Affichage du résultat final
    print(ans)

# Appel de la fonction principale
max_segment_count()