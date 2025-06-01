import sys

def main():
    """
    Lit des données depuis l'entrée standard pour déterminer le nombre minimal de segments
    nécessaires où chaque segment respecte une contrainte de poids comparée à certaines capacités.
    
    La fonction procède en plusieurs étapes :
    - Lecture du nombre d'éléments et des couples (capacité, poids) associés.
    - Initialisation d'une matrice de validité pour identifier quels intervalles sont valides.
    - Calcul d'une somme cumulée des poids pour permettre des calculs rapides de sommes d'intervalles.
    - Remplissage de la matrice de validité p selon les règles données sur les capacités et poids.
    - Utilisation d'une programmation dynamique pour calculer le nombre minimal de segments requis.
    - Affichage du résultat final.
    """
    f = sys.stdin

    # Lecture du nombre d'éléments
    n = int(f.readline())
    
    # Lecture des couples (capacités c, poids w) pour chaque élément
    s = [list(map(int, line.split())) for line in f]

    # Initialisation de la matrice p de validité des intervalles de taille (n+1)x(n+1)
    # p[i][j] == True signifie que l'intervalle [i, j] est valide selon les conditions de capacité/poids
    # On initialise p[i][i] à True pour tous les i (intervalles vides ou d'un seul élément)
    p = [[i == j for j in range(n + 1)] for i in range(n + 1)]

    # Extraction des capacités c et des poids w depuis la liste s
    # On ajoute un élément imaginaire en position 0 avec capacité 0 pour faciliter les indices
    c = [0] + [c for c, w in s]
    sum_w = [0] + [w for c, w in s]

    # Calcul de la somme cumulée des poids pour permettre un accès rapide à la somme des poids
    for i in range(1, len(sum_w)):
        sum_w[i] += sum_w[i - 1]

    # Remplissage de la matrice p
    # On étudie tous les intervalles [i, j] avec i <= j
    for length in range(n):
        # i désigne l'indice de début de l'intervalle
        for i in range(1, n + 1 - length):
            j = i + length  # indice de fin de l'intervalle
            if not p[i][j]:
                # Si l'intervalle [i,j] n'est pas valide, on ne procède pas aux mises à jour
                continue
            
            # Vérification si on peut étendre l'intervalle à droite : [i, j+1]
            if j + 1 <= n:
                # La somme des poids dans l'intervalle [i, j] = sum_w[j] - sum_w[i-1]
                # On vérifie si cette somme est inférieure ou égale à la capacité du prochain élément c[j+1]
                if sum_w[j] - sum_w[i - 1] <= c[j + 1]:
                    p[i][j + 1] = True
            
            # Vérification si on peut étendre l'intervalle à gauche : [i-1, j]
            # On vérifie que la somme du poids reste inférieure ou égale à la capacité c[i-1]
            if i - 1 >= 0 and sum_w[j] - sum_w[i - 1] <= c[i - 1]:
                p[i - 1][j] = True

    # Initialisation du tableau dp pour la programmation dynamique
    # dp[e] représente le nombre minimal de segments pour couvrir les éléments jusqu'à l'indice e
    # On initialise avec une très grande valeur (infinie) pour signifier que la solution n'est pas encore trouvée
    dp = [999999999] * (n + 1)
    dp[0] = 0  # Base : aucun élément couvert nécessite 0 segment

    # Calcul du nombre minimal de segments nécessaires
    for b in range(1, n + 1):
        for e in range(1, n + 1):
            # Si l'intervalle [b, e] est valide (p[b][e] == True),
            # on peut envisager de couvrir cette portion en un segment
            if p[b][e]:
                # On met à jour la valeur minimale pour dp[e]
                # dp[b-1] + 1 représente ajouter un segment couvrant [b, e] après avoir couvert jusqu'à b-1
                dp[e] = min(dp[e], dp[b - 1] + 1)

    # Affichage du résultat : nombre minimal de segments pour couvrir tous les éléments
    print(dp[-1])

if __name__ == "__main__":
    main()