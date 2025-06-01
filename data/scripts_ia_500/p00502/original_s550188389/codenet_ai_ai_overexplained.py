INF = 10 ** 20  # Définition d'une constante INF qui représente une très grande valeur (10 puissance 20), utilisée pour marquer une valeur impossible ou infiniment petite dans le contexte de l'algorithme.

def main():
    # Lecture de deux entiers séparés par un espace à partir de l'entrée standard (typiquement l'utilisateur),
    # puis conversion en deux variables entières d et n.
    # d : nombre de jours
    # n : nombre d'éléments (par exemple dans un contexte de planning ou autre)
    d, n = map(int, input().split())
    
    # Lecture de d entiers chacun sur une ligne distincte, pour remplir la liste 'temp' de températures ou valeurs.
    # La compréhension de liste [int(input()) for i in range(d)] permet de répéter 'd' fois la lecture et la conversion en entier.
    temp = [int(input()) for i in range(d)]
    
    # Insertion de la valeur 0 au début de la liste 'temp'. Cela décale tous les indices d'1.
    # Cela permet d'utiliser des indices à partir de 1 plutôt que 0, ce qui peut faciliter la compréhension (les jours sont comptés à partir de 1)
    temp.insert(0, 0)
    
    # Initialisation de trois listes vides qui vont contenir respectivement a, b, et c pour chaque élément (n éléments).
    # Ces listes permettront de stocker les bornes et la valeur associée pour chaque élément.
    alst = []
    blst = []
    clst = []
    
    # Lecture de n lignes, chacune contenant trois entiers a, b, c.
    # Ces triplets sont ajoutés dans leurs listes respectives.
    for i in range(n):
        a, b, c = map(int, input().split())
        alst.append(a)  # Limite inférieure pour le i-ème élément
        blst.append(b)  # Limite supérieure pour le i-ème élément
        clst.append(c)  # Valeur associée pour le i-ème élément
    
    # Initialisation d'une matrice 'dp' (programmation dynamique),
    # de taille (d+1) x n, remplie initialement de valeurs 0.
    # dp[i][j] représentera la meilleure valeur calculée pour le jour i en choisissant l'élément j.
    dp = [[0] * n for i in range(d + 1)]
    
    # Récupération de la température/température du premier jour (indice 1, car on a inséré 0 au début).
    t1 = temp[1]
    
    # Pour chaque élément j (de 0 à n-1), on vérifie si la température t1 du premier jour respecte la contrainte
    # que t1 soit dans l'intervalle [alst[j], blst[j]].
    # Si ce n'est pas le cas, cela signifie que l'élément j n'est pas valide pour le premier jour,
    # on assigne donc à dp[1][j] une très grande valeur négative (-INF),
    # indiquant une invalidité ou une impossibilité de choisir cet élément au jour 1.
    for i in range(n):
        if not (alst[i] <= t1 <= blst[i]):
            dp[1][i] = -INF
    
    # Pour les jours suivants, de 2 à d inclus :
    for i in range(2, d + 1):
        # Récupération de la température pour le jour i
        t = temp[i]
        
        # prédiction des valeurs du jour précédent dans dp (pour optimisation d'accès)
        predp = dp[i - 1]
        
        # Pour chaque élément j du jour i :
        for j in range(n):
            # récupère la valeur associée au j-ième élément
            cj = clst[j]
            
            # On vérifie si la température au jour i respecte la contrainte d'intervalle [alst[j], blst[j]]
            if alst[j] <= t <= blst[j]:
                # Calcul de dp[i][j] comme étant le maximum sur tous les x (éléments du jour précédent),
                # de la somme de la valeur dp[i-1][x] plus la valeur absolue de la différence entre cj (valeur actuelle)
                # et clst[x] (valeur du jour précédent).
                # Ici, on écrit l'expression (cj - clst[x] if cj >= clst[x] else clst[x] - cj) pour calculer la valeur absolue
                # de la différence entre cj et clst[x] sans utiliser abs() pour des raisons de performance ou style.
                dp[i][j] = max(predp[x] + (cj - clst[x] if cj >= clst[x] else clst[x] - cj) for x in range(n))
    
    # Une fois tous les jours traités et tous les états calculés,
    # on affiche la valeur maximale finale sur le dernier jour d,
    # parmi tous les éléments j possibles ce jour-là.
    print(max(dp[d]))

# Appel de la fonction principale 'main' pour démarrer l'exécution du programme.
main()