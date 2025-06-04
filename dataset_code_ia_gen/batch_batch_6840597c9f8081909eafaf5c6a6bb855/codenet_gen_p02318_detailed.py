# Fonction pour calculer la distance d'édition (Levenshtein Distance) entre deux chaînes s1 et s2
def edit_distance(s1, s2):
    # longueur de s1 et s2
    n = len(s1)
    m = len(s2)
    
    # Création d'une matrice dp de taille (n+1) x (m+1)
    # dp[i][j] contiendra la distance d'édition entre s1[:i] et s2[:j]
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    # Initialisation de la première colonne (transformer s1[:i] en chaîne vide s2[:0])
    for i in range(1, n + 1):
        dp[i][0] = i  # i suppressions nécessaires
    
    # Initialisation de la première ligne (transformer chaîne vide s1[:0] en s2[:j])
    for j in range(1, m + 1):
        dp[0][j] = j  # j insertions nécessaires
    
    # Remplissage de la matrice dp
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # Si les caractères correspondent, pas d'opération supplémentaire nécessaire
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                # Sinon, considérer les trois opérations et prendre le minimum :
                # - suppression (dp[i-1][j] + 1)
                # - insertion (dp[i][j-1] + 1)
                # - substitution (dp[i-1][j-1] + 1)
                dp[i][j] = 1 + min(
                    dp[i - 1][j],    # suppression
                    dp[i][j - 1],    # insertion
                    dp[i - 1][j - 1] # substitution
                )
    # La distance d'édition entre s1 et s2 est dans dp[n][m]
    return dp[n][m]

# Lecture de l'entrée
s1 = input().strip()
s2 = input().strip()

# Calcul et affichage de la distance d'édition
print(edit_distance(s1, s2))