def main():
    # Lire la première ligne d'entrée contenant trois entiers séparés par des espaces
    # n : nombre total d'éléments ou d'inputs à traiter
    # t : un entier représentant une limite supérieure, souvent un temps ou une capacité maximale
    # s : un entier représentant une valeur seuil, une contrainte liée au temps ou à la capacité
    # La fonction input() récupère une chaîne de caractères en entrée,
    # split() la découpe en une liste de chaînes autour des espaces,
    # map(int, ...) convertit chaque élément de cette liste en entier,
    # et l'affectation multiple assigne ces valeurs respectivement à n, t, et s
    n, t, s = map(int, input().split())
    
    # Initialisation de deux listes vides qui vont stocker respectivement
    # des valeurs a et b associées aux n entrées suivantes
    A = []
    B = []
    
    # Boucle répétée n fois, où chaque itération lit une nouvelle paire d'entiers a et b
    # Ces a et b représentent des paramètres liés aux éléments traités (par exemple valeurs et coûts)
    for _ in range(n):
        # Lecture d'une ligne, découpage en deux entiers a et b, conversion en int
        a, b = map(int, input().split())
        # Ajout de ces valeurs dans les listes A et B à la fin, respectivement
        A.append(a)
        B.append(b)
    
    # Commentaire explicatif (en japonais dans l'original) décrivant la logique du tableau dp
    # Ici dp est une table à deux dimensions utilisée pour la programmation dynamique
    # dp[x+1][y] signifie la valeur maximale atteignable en considérant les x premiers éléments (0-based)
    # et en disposant d'une capacité ou temps y (par ex. temps maximum jusqu'à y)
    # La relation de récurrence est décrite comme suit :
    # dp[x+1][y] = max(
    #   dp[x][y],                       # ne pas prendre le x-ième élément
    #   dp[x+1][y - 1],                 # réduire le temps y d'une unité sans prendre nouvel élément
    #   dp[x][y - B[x]] + A[x]          # prendre le x-ième élément si conditions sur y-B[x] sont remplies
    # )
    # Condition importante : on ne peut prendre l'élément que si y-B[x] n'est pas strictement
    # entre s et y (c'est-à-dire pas dans l'intervalle ouvert (s,y))
    
    # Création d'un tableau dp à deux dimensions de taille (n+1) x (t+1)
    # Chaque entrée initialisée à 0 (par défaut),
    # signifiant que sans éléments ou temps, la valeur maximale est zéro
    dp = [[0] * (t + 1) for _ in range(n + 1)]
    
    # Traitement en programmation dynamique
    # Pour chaque élément x (de 0 à n-1)
    for x in range(n):
        # Récupération du coût/temps B[x] et de la valeur A[x] correspondante
        bx = B[x]
        ax = A[x]
        # Références pour optimiser l'accès mémoire lors des calculs
        dpx = dp[x]       # ligne correspondant à l'état avec les x éléments considérés
        dpx1 = dp[x + 1]  # ligne correspondant à l'état avec les x+1 éléments considérés
        
        # Pour chaque capacité/temps possible y de 1 à t (inclus)
        for y in range(1, t + 1):
            # Vérification des conditions pour décider si on peut prendre l'élément x à ce temps y
            # Condition : y - bx >= 0 (on reste dans les indices valides)
            # et il n'est pas vrai que y - bx < s < y (c'est la contrainte liée à s)
            if 0 <= y - bx and not (y - bx < s < y):
                # On calcule donc la meilleure valeur possible en choisissant la meilleure
                # entre ne pas prendre l'élément, avancer de 1 dans le temps sans prendre,
                # ou prendre l'élément (on regarde la meilleure valeur jusqu'à y - bx et on ajoute ax)
                dpx1[y] = max(
                    dpx[y],            # ne pas prendre le nouvel élément à ce temps y
                    dpx1[y - 1],       # avancer le temps d'une unité sans nouvel élément
                    dpx[y - bx] + ax   # prendre l'élément x et ajouter sa valeur
                )
            else:
                # Sinon, on ne peut pas prendre l'élément x à ce temps y
                # La valeur maximale est donc soit de ne rien changer ou d'avancer le temps d'une unité
                dpx1[y] = max(
                    dpx[y],          # ne pas prendre l'élément
                    dpx1[y - 1]      # avancer le temps sans prendre
                )
    
    # Affichage du résultat final : la valeur maximale atteinte en considérant tous les éléments (n)
    # et le temps/capacité maximal (t)
    print(dp[n][t])

# Appel de la fonction principale pour lancer l'exécution
main()