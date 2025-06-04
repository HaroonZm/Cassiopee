from heapq import heappush, heappop  # Importe la fonction heappush et heappop depuis le module heapq pour utiliser une file de priorité (priority queue) basée sur un min-heap

def solve():
    S = input()  # Lis une chaîne de caractères depuis l'entrée standard et la stocke dans la variable S
    K = int(input())  # Lis une entrée, la convertit en entier, la stocke dans K (on recherche le K-ième palindrome)
    L = len(S)  # Calcule la longueur de la chaîne S et la stocke dans L

    INF = 10**9  # Définit une constante représentant l'infini (un grand nombre), pour initialiser des coûts très grands

    # Crée une matrice cost de dimensions (L+1) x (L+1), initialisée à INF.
    # cost[a][b] représentera le coût minimum pour transformer le sous-intervalle S[a:b] en palindrome.
    cost = [[INF] * (L+1) for i in range(L+1)]

    # Initialisation du coût : il n'y a aucun coût pour transformer la chaîne vide en palindrome
    cost[0][L] = 0

    ss = []  # Liste vide utilisée plus tard pour stocker les couples (a, b) traités, où chaque sous-chaîne S[a:b] est considérée

    # Initialisation de la file de priorité avec un seul état : coût 0, indices a=0 et b=L, c'est-à-dire S[0:L]
    que = [(0, 0, L)]

    # On utilise l'algorithme de Dijkstra (ou BFS pondéré) pour trouver tous les coûts min pour chaque sous-chaîne S[a:b]
    while que:
        d, a, b = heappop(que)  # Récupère l'élément avec le coût minimum (d) dans la file, avec indices a et b.
        if cost[a][b] < d:  # Si un meilleur coût a déjà été trouvé pour S[a:b], on n'optimise pas plus
            continue
        ss.append((a, b))  # Ajoute (a, b) à la liste de tous les intervalles explorés pour traitement ultérieur

        # Cas de base : la sous-chaîne est de longueur 1 (un caractère, toujours un palindrome)
        if a+1 == b:
            # Vérifie si le passage à la sous-chaîne vide coûte moins cher (coût actuel + 1)
            if d+1 < cost[a+1][b]:
                cost[a+1][b] = d + 1  # Met à jour le coût si c'est mieux (retrait du dernier caractère)
            continue

        # Si les caractères aux extrémités sont identiques, on peut former un palindrome sans les changer
        if S[a] == S[b-1]:
            if d+2 < cost[a+1][b-1]:  # Coût de "remplacer" les deux caractères par eux-mêmes est 2 (on saute vers le centre)
                cost[a+1][b-1] = d + 2  # Met à jour le coût pour la sous-chaîne réduite
                if a+1 < b-1:  # On évite d'ajouter des sous-chaînes vides
                    heappush(que, (d+2, a+1, b-1))  # Ajoute ce nouvel état à la priorité pour exploration

        # Sinon, les caractères aux extrémités sont différents. On doit faire des modifications (insertion/substitution)
        else:
            # Option 1 : on remplace ou insère S[a] du côté droit pour faire un palindrome
            if d+2 < cost[a+1][b]:
                cost[a+1][b] = d+2
                if a+1 < b:
                    heappush(que, (d+2, a+1, b))
            # Option 2 : on remplace ou insère S[b-1] du côté gauche pour palindrome
            if d+2 < cost[a][b-1]:
                cost[a][b-1] = d+2
                if a < b-1:
                    heappush(que, (d+2, a, b-1))

    # Recherche du coût minimal nécessaire pour rendre la chaîne (ou sous-chaîne) un palindrome
    # On considère toutes les sous-chaînes "vides" (où a == b) et prend le minimum de leurs coûts
    ln = min(cost[i][i] for i in range(L+1))

    # Inverse l'ordre de ss, car on exploitera la programmation dynamique en partant des plus "petites" sous-chaînes possibles
    ss.reverse()

    # Initialise la table de programmation dynamique (dp) qui comptera le nombre de façons "optimales" d'obtenir un palindrome
    dp = [[0] * (L+1) for i in range(L+1)]

    # Pour chaque sous-chaîne vide (où a == b), si son coût est ln (le coût minimal), on peut terminer en palindrome d'une façon
    for i in range(L+1):
        if cost[i][i] == ln:
            dp[i][i] = 1

    # Remplit la table dp du plus "petit" au plus "grand" intervalle
    for a, b in ss:
        d = cost[a][b]  # Coût minimal pour S[a:b]
        r = 0  # Nombre de façons d'obtenir palindrome à coût d
        if a+1 == b:  # Cas d'une lettre
            if d+1 == cost[a+1][b]:
                r = dp[a+1][b]
        else:
            if S[a] == S[b-1]:  # Caractères symétriques identiques
                if d+2 == cost[a+1][b-1]:
                    r = dp[a+1][b-1]
            else:
                if d+2 == cost[a+1][b]:
                    r += dp[a+1][b]
                if d+2 == cost[a][b-1]:
                    r += dp[a][b-1]
        dp[a][b] = r  # Met à jour le nombre de solutions de S[a:b]

    # Si le nombre total de solutions optimales est inférieur à K, il n'existe pas de K-ième solution, on affiche "NONE"
    if dp[a][b] < K:
        print("NONE")
        return True  # On termine la fonction

    SL = []  # Liste pour construire la première moitié du palindrome final
    SR = []  # Liste pour construire la deuxième moitié (sera inversée à la fin)
    a = 0
    b = L

    # Construit lettre par lettre le K-ième plus petit palindrome obtenu avec le coût optimal
    while a < b:
        if a+1 == b:  # Si un seul caractère reste à placer
            assert cost[a][b]+1 == cost[a+1][b]  # On vérifie la validité logique du passage
            SL.append(S[a])  # Ajoute ce caractère
            a += 1  # Avance le pointeur à droite
            continue

        if S[a] == S[b-1]:
            assert cost[a][b]+2 == cost[a+1][b-1]
            SL.append(S[a])  # Ajoute le caractère de gauche (qui est égal à droite)
            SR.append(S[b-1])  # Ajoute le même caractère en miroir pour la moitié droite
            a += 1  # Avance le début
            b -= 1  # Recule la fin
        elif S[a] < S[b-1]:
            c = (cost[a][b]+2 == cost[a+1][b])
            if c and K <= dp[a+1][b]:
                SL.append(S[a])    # Place S[a] de chaque côté
                SR.append(S[a])
                a += 1
            else:
                if c:  # On saute les solutions commencant par S[a]
                    K -= dp[a+1][b]
                SL.append(S[b-1])
                SR.append(S[b-1])
                b -= 1
        else:
            c = (cost[a][b]+2 == cost[a][b-1])
            if c and K <= dp[a][b-1]:
                SL.append(S[b-1])
                SR.append(S[b-1])
                b -= 1
            else:
                if c:
                    K -= dp[a][b-1]  # On saute les solutions commençant par S[b-1]
                SL.append(S[a])
                SR.append(S[a])
                a += 1

    # Après la boucle, on a SL et SR contenant chacune la moitié du palindrome
    SR.reverse()  # Inverse l'ordre pour obtenir la moitié droite
    SL.extend(SR)  # Assemble les deux moitiés pour former le palindrome complet

    # Affiche la chaîne résultante, qui est le K-ième palindrome "lexicographiquement" minimal et de coût optimal
    print("".join(SL))

solve()  # Appelle la fonction principale pour exécuter tout le code