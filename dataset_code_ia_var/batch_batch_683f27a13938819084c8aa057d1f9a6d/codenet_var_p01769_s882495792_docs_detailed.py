def main():
    """
    Programme principal qui calcule le nombre de manières de remplir une séquence
    soumise à certaines contraintes, modulo 10^9+7.

    Les contraintes sur chaque élément de la séquence sont définies par deux listes :
    - x_i : position de départ ou valeur de récurrence pour une séquence possible
    - a_i : intervalle pour générer la séquence ou 0 pour n'autoriser que x_i

    Entrée :
    - Deux entiers n (taille de la séquence) et l (longueur totale)
    - Suite de n entiers : la liste x
    - Suite de n entiers : la liste a

    Les possibles valeurs sur chaque ligne du dp sont déterminées par ces ensembles.
    """
    MOD = 1000000007  # Modulo utilisé pour les résultats
    
    # Lecture des entrées n (nombre d'ensembles) et l (longueur à atteindre)
    n, l = map(int, input().split())
    
    # Liste des positions x
    xlst = map(int, input().split())
    # Liste des intervalles/délais a
    alst = map(int, input().split())
    
    can_use = []  # can_use[i] contiendra l'ensemble des positions utilisables pour l'élément i
    
    # Calcul de l'ensemble des valeurs possibles pour chaque élément
    for x, a in zip(xlst, alst):
        if a == 0:
            # Si a == 0, seul x est autorisé
            s = {x}
        else:
            # Sinon, toutes les positions commençant à x et espacées de a, inférieures à l
            s = {k for k in range(x, l, a)}
        can_use.append(s)
    
    # Initialisation du tableau de programmation dynamique
    # dp[i][j] : nombre de façons d'utiliser les 'i+1' premiers ensembles pour obtenir une somme 'j'
    dp = [[0] * l for _ in range(n)]
    
    # Remplir la première ligne du tableau dp
    # Pour chaque position j, dp[0][j] compte le nombre d'éléments utilisables jusqu'à j
    for j in range(l):
        # Si j correspond à une valeur utilisable, on ajoute 1 à la valeur précédente
        dp[0][j] = dp[0][j - 1] + int(j in can_use[0])
    
    # Remplissage du reste du tableau dp
    # On parcourt les ensembles suivants
    for i in range(1, n):
        acc = 0  # Accumulateur pour le nombre de combinaisons
        dpi = dp[i]        # Ligne courante du dp
        dpi1 = dp[i - 1]   # Ligne précédente du dp
        st = can_use[i]    # Ensemble des valeurs utilisables pour cette ligne
        for j in range(1, l):
            # Si j est admissible pour cet ensemble
            if j in st:
                # On ajoute toutes les combinaisons menant à j-1
                acc = (acc + dpi1[j - 1]) % MOD
            # dp[i][j] prend la valeur de l'accumulateur courant
            dpi[j] = acc

    # Le résultat final est dp[n - 1][l - 1] :
    # nombre de façons d'obtenir la somme l-1 en utilisant les n ensembles
    print(dp[n - 1][l - 1])