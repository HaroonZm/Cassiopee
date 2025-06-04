# Lire deux entiers de l'entrée standard, séparés par un espace.
# La fonction input() lit une ligne au format texte (string) depuis l'entrée standard.
# La méthode split() sépare cette ligne en une liste de sous-chaînes sur les espaces.
# La fonction map(int, ...) applique int() à chaque élément de cette liste, convertissant chaque chaîne en entier.
# Enfin, list(...) convertit le résultat de map en une liste explicite.
N, M = list(map(int, input().split()))

# La fonction divmod(a, b) retourne un tuple de deux éléments :
# 1. Le quotient de la division entière de a par b (a // b)
# 2. Le reste de la division de a par b (a % b)
# Ici, on divise M par N pour obtenir le nombre de fois que N entre dans M (quotient s) et le reste r.
s, r = divmod(M, N)

# On crée une variable appelée ans et on lui affecte la valeur 1.
# Bien que cette variable ne soit pas utilisée dans le reste du code, elle peut servir dans certains contextes.
ans = 1

# On commence une boucle for décroissante.
# La fonction range(start, stop, step) produit une séquence de nombres.
# Ici, elle commence à s et se termine à 1 inclus (car stop=0 et le step est négatif),
# en décrémentant de 1 à chaque itération.
for i in range(s, 0, -1):
    # Pour chaque valeur de i dans la séquence, on vérifie si i est un diviseur de M.
    # L'opérateur modulo % retourne le reste de la division entière de M par i.
    # Si M % i == 0, cela signifie que i divise M sans reste, donc i est un diviseur de M.
    if M % i == 0:
        # On affiche la valeur de i trouvée à l'aide de la fonction print().
        print(i)
        # On sort immédiatement de la boucle for avec l'instruction break.
        # Cela signifie qu'après avoir trouvé et affiché le premier diviseur trouvé en partant de s,
        # le programme arrête la recherche et sort de la boucle.
        break