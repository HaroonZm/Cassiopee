def main():
    """
    Programme principal qui traite des séquences de conversions avec probabilités maximales.

    Ce programme lit de manière répétée deux entiers n et m depuis l'entrée standard.
    - n représente le nombre d'éléments (par exemple, monnaies ou états).
    - m représente le nombre d'étapes de conversion.

    Pour chaque paire (n, m) où n n'est pas nul, le programme :
    1. Lit une matrice nxn de coefficients flottants gs représentant les probabilités ou taux de conversion.
    2. Calcule la probabilité maximale d'obtenir une conversion en exactement m étapes, 
       en utilisant une programmation dynamique.
    3. Affiche cette probabilité maximale arrondie à deux décimales.
    
    Le programme s'arrête dès que n est égal à 0.
    """
    while True:
        # Lecture de deux entiers n (nombre d'éléments) et m (nombre d'étapes)
        n, m = map(int, input().split())
        # Condition d'arrêt du programme si n vaut 0
        if n == 0:
            break
        
        # Lecture de la matrice gs contenant les coefficients de conversion entre éléments
        # gs[i][j] correspond au coefficient pour aller de l'élément i à l'élément j
        gs = [list(map(float, input().split())) for _ in range(n)]
        
        # Initialisation de la table de programmation dynamique dp
        # dp[i][j] représente la probabilité maximale d'arriver à l'élément j en i étapes
        # On a m+1 lignes (de 0 à m) et n colonnes (pour chaque élément)
        dp = [[0.0] * n for _ in range(m + 1)]
        
        # Base de la programmation dynamique :
        # En 1 étape, la probabilité d'être sur l'élément i est 1 (on part de cet élément)
        for i in range(n):
            dp[1][i] = 1.0
        
        # Calcul des probabilités maximales pour chaque nombre d'étapes de 2 à m
        for i in range(2, m + 1):
            for j in range(n):
                # Pour arriver à l'élément j en i étapes,
                # on cherche la meilleure probabilité parmi tous les éléments k
                # à l'étape i-1, multipliée par le coefficient gs[k][j]
                dp[i][j] = max(dp[i - 1][k] * gs[k][j] for k in range(n))
        
        # Affichage de la probabilité maximale après m étapes, formatée avec 2 décimales
        print(format(max(dp[m]), ".2f"))


if __name__ == "__main__":
    main()