def read_input():
    """
    Lit les données d'entrée de l'utilisateur. 
    L'utilisateur saisit d'abord un entier n (nombre d'éléments), 
    puis saisit n entiers (la liste des couleurs, ou valeurs quelconques).
    
    Returns:
        int: Le nombre d'éléments n.
        list of int: La liste des entiers saisis.
    """
    n = int(input())
    c = [int(input()) for _ in range(n)]
    return n, c

def calculate_previous_occurrences(c):
    """
    Pour chaque valeur de la liste c, trouve la position précédente où cette valeur est apparue.
    Si une valeur n'a jamais été vue auparavant, assigne -1.

    Args:
        c (list of int): La liste des entiers représentant des couleurs ou valeurs quelconques.

    Returns:
        list of int: Une liste r telle que r[i] est l'index précédent de c[i]
                     où c[i] == c[r[i]], ou -1 si c[i] n'est jamais apparu avant.
    """
    n = len(c)
    r = [-1] * n  # tableau résultat initialisé à -1
    last_seen = dict()  # dictionnaire pour mémoriser la dernière occurrence de chaque valeur
    for i, value in enumerate(c):
        if value in last_seen:
            # Si déjà vu, on stocke la dernière position et on met à jour
            r[i] = last_seen[value]
        # Met à jour l'index courant pour ce value
        last_seen[value] = i
    return r

def compute_dp(r, modulo=10**9+7):
    """
    Applique le calcul dynamique basé sur les occurrences passées enregistrées dans r.
    Calcule pour chaque position le nombre de façons d'atteindre cette position selon les règles :
        - Si la valeur à l'indice i n'a jamais été vue ou juste vue à l'indice i-1, on ne change rien.
        - Sinon, on additionne les façons du pas précédent et de la précédente occurrence trouvée.
    Le résultat est calculé modulo le paramètre modulo.

    Args:
        r (list of int): La liste indiquant l'apparition précédente de chaque valeur.
        modulo (int): L'entier par lequel on prend le reste pour éviter les débordements.

    Returns:
        list of int: Le tableau dynamique des résultats intermédiaires jusqu'à chaque position.
    """
    n = len(r)
    dp = [1] * n  # Initialisation : il y a au moins une façon pour chaque élément
    dp[0] = 1     # La première case est toujours 1
    for i in range(1, n):
        if r[i] == -1:
            # Si aucune occurrence précédente, même valeur que dp[i-1]
            dp[i] = dp[i-1]
        elif r[i] == i-1:
            # Si occurrence précédente immédiatement avant, même valeur que dp[i-1]
            dp[i] = dp[i-1]
        else:
            # Sinon, ajoute le nombre de façons jusqu'à la précédente occurrence
            dp[i] = (dp[i-1] + dp[r[i]]) % modulo
    return dp

def main():
    """
    Point d'entrée du script. 
    1. Lit les entrées utilisateur,
    2. Calcule les occurrences précédentes,
    3. Applique la programmation dynamique pour obtenir le résultat final,
    4. Affiche le résultat pour la dernière position de la liste saisie.
    """
    n, c = read_input()
    r = calculate_previous_occurrences(c)
    dp = compute_dp(r)
    print(dp[-1])

if __name__ == '__main__':
    main()