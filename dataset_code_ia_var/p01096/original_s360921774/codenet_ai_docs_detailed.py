def solve(n, lst):
    """
    Résout le problème principal en recherchant le nombre maximal d'éléments pouvant être retirés selon les conditions spécifiées.

    Arguments :
        n (int): Taille de la liste 'lst'.
        lst (tuple of int): Séquence d'entiers représentant les objets à analyser.

    La fonction construit une table DP où dp[i][j] contient le nombre maximal d'éléments retirables
    d'une sous-liste de taille i commençant à l'indice j. L'état dp[i][j] est mis à jour en considérant
    différentes façons de partitionner la sous-liste, soit en retirant des groupes valides (si les extrémités sont proches,
    et le centre est également validable récursivement), soit en divisant en groupes plus petits et en sommant les résultats.
    À la fin, le résultat maximal pour la séquence complète est affiché.
    """
    # Initialisation de la table DP. dp[i][j] représente le nombre maximal d'objets
    # pouvant être retirés d'une sous-séquence de taille i commençant à l'indice j.
    dp = [[0] * n for _ in range(n + 1)]

    # Initialisation de dp pour les groupes de taille 2 :
    # On regarde chaque paire consécutive, si la différence est au plus 1, on peut retirer les deux.
    for j in range(n - 1):
        if abs(lst[j] - lst[j + 1]) <= 1:
            dp[2][j] = 2

    # Traitement pour toutes les tailles de groupes de 3 à n inclus
    for i in range(3, n + 1):
        # On considère toutes les sous-séquences de taille i commençant à j
        for j in range(n - i + 1):
            max_removed = 0  # Valeur maximale trouvée pour cette sous-séquence

            if i % 2 == 0:
                # Cas d'un groupe de taille paire (2m)
                # Si les extrémités sont proches et le centre est totalement retirable, on retire tout le groupe
                if abs(lst[j] - lst[j + i - 1]) <= 1:
                    if dp[i - 2][j + 1] == i - 2:
                        dp[i][j] = i
                        continue  # On a trouvé la meilleure option pour ce cas

                # Sinon, on essaie de diviser l'intervalle en deux sous-intervalles de tailles paires,
                # et on maximise la somme des éléments retirés dans chaque sous-intervalle
                max_removed = dp[i - 2][j + 1]  # Retirer le centre si possible
                for k in range(2, i, 2):
                    # On essaie toutes les divisions possibles en deux sous-groupes de taille paire
                    if max_removed < dp[k][j] + dp[i - k][j + k]:
                        max_removed = dp[k][j] + dp[i - k][j + k]
                        # Si on a atteint le maximum possible, on arrête la recherche
                        if max_removed == i:
                            break
            else:
                # Cas d'un groupe de taille impaire (2m+1)
                # Ici, on essaie toutes les divisions en deux sous-segments de tailles impaires et paires
                for k in range(1, i, 2):
                    if max_removed < dp[k][j] + dp[i - k][j + k]:
                        max_removed = dp[k][j] + dp[i - k][j + k]

            # On stocke le résultat pour la sous-séquence considèreée
            dp[i][j] = max_removed

    # Affiche le nombre maximal d'éléments pouvant être retirés de la séquence complète
    print(dp[n][0])
    # Pour le débogage : affiche la table DP complète
    # print(dp)


def main():
    """
    Fonction principale qui lit les entrées, appelle la solution, et se termine quand 'n' devient 0.
    """
    while True:
        n = int(input())
        if n == 0:
            break
        lst = tuple(map(int, input().split()))
        solve(n, lst)


# Appel du point d'entrée principal
if __name__ == '__main__':
    main()