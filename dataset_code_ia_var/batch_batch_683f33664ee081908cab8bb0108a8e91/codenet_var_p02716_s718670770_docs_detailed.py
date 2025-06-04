def max_sum_alternating_subsequence():
    """
    Lis une séquence d'entiers et calcule la somme maximale d'une sous-séquence alternante 
    selon une contrainte dépendant de la parité de la longueur de la séquence.
    
    Le code utilise la programmation dynamique pour explorer toutes les possibilités de la 
    construction de sous-séquences alternantes avec jusqu'à 3 "groupes" (indiqué par l'indice j).
    Les états dp[i][j][k] mémorisent pour i éléments, j groupes, k flag (si on est à l'intérieur 
    d'un segment sélectionné ou entre), la meilleure somme atteignable.

    Entrées :
        - n (int) : taille de la séquence
        - a (List[int]) : liste d'entiers

    Sortie :
        - Affiche la somme maximale trouvée sous la contrainte du problème

    Remarque : Les contraintes et la signification précise de l'algorithme dépend du problème d'origine.
    """
    # Lecture de la longueur de la séquence.
    n = int(input())
    # Lecture puis conversion de la séquence d'entrée en liste d'entiers.
    a = list(map(int, input().split()))
    
    # Initialisation de la table de programmation dynamique.
    # dp[i][j][k] mémorise la meilleure somme possible pour :
    # i (éléments considérés), j (nombre de groupes - peut représenter le nombre de sous-séquences), 
    # k (flag indiquant si le dernier groupe inclut le i-ème élément (1) ou non (0))
    # On initialise toutes les valeurs à -10^15 (très petit), sauf le cas de base.
    dp = [[[-10**15, -10**15] for _ in range(4)] for _ in range(n+1)]
    
    # Cas de base : avant tout choix, somme nulle, 0 groupe, hors segment.
    dp[0][0][0] = 0

    # Remplissage de la table DP.
    for i in range(n):  # Pour chaque position de l'élément considéré.
        for j in range(4):  # Pour chaque nombre de groupes possibles (max 3 autorisés ici).
            for k in range(2):  # Pour chaque état : "non en cours de sélection" (0) ou "en cours" (1)
                if j == 3:
                    # Si on a déjà atteint 3 groupes :
                    # Option 1 : clore le segment courant (si on était dans un groupe)
                    dp[i+1][3][0] = max(dp[i][3][1], dp[i+1][3][0])
                    # Option 2 : poursuivre dans le 3e groupe avec l'élément courant
                    dp[i+1][3][1] = max(dp[i][3][0]+a[i], dp[i+1][3][1])
                elif j == 2:
                    # Cas du 2e groupe
                    # Clore le segment courant
                    dp[i+1][2][0] = max(dp[i][2][1], dp[i+1][2][0])
                    # Poursuivre dans le 2e groupe
                    dp[i+1][2][1] = max(dp[i][2][0]+a[i], dp[i+1][2][1])
                    # Ouvrir un nouveau groupe (passer à j+1 groupe)
                    dp[i+1][3][0] = max(dp[i][2][0], dp[i+1][3][0])
                elif j == 1:
                    # Cas du 1er groupe
                    # Clore le segment courant
                    dp[i+1][1][0] = max(dp[i][1][1], dp[i+1][1][0])
                    # Poursuivre dans le 1er groupe
                    dp[i+1][1][1] = max(dp[i][1][0]+a[i], dp[i+1][1][1])
                    # Ouvrir un nouveau groupe
                    dp[i+1][2][0] = max(dp[i][1][0], dp[i+1][2][0])
                else:
                    # Cas initial (j == 0)
                    # Clore le segment courant (ici ça n'a d'effet que pour case 0,0,1)
                    dp[i+1][0][0] = max(dp[i][0][1], dp[i+1][0][0])
                    # Commencer le 1er groupe avec l'élément courant
                    dp[i+1][0][1] = max(dp[i][0][0]+a[i], dp[i+1][0][1])
                    # Ouvrir le groupe suivant (le premier à partir de l'état initial)
                    dp[i+1][1][0] = max(dp[i][0][0], dp[i+1][1][0])

    # Calcul du résultat final selon la parité de n.
    # Le résultat dépend de la contrainte de sélection des sous-séquences alternantes.
    ans = 0
    if n % 2 == 0:
        # Si la séquence a une longueur paire, on ne considère pas certaines transitions.
        ans = max(max(dp[n][0]), dp[n][1][1])
    else:
        # Si sequence impaire, on autorise plus de configurations.
        ans = max(max(dp[n][0]), max(dp[n][1]), dp[n][2][1])

    # Affichage du résultat optimal
    print(ans)

# Appel de la fonction principale
max_sum_alternating_subsequence()