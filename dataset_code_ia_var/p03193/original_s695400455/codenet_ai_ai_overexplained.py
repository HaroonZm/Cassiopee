# Demande à l'utilisateur d'entrer trois nombres entiers séparés par des espaces.
# Utilise la fonction input() pour lire une ligne de texte saisie par l'utilisateur.
# La méthode split() divise cette ligne en une liste de chaînes de caractères, en utilisant l'espace comme séparateur.
# La fonction map(int, ...) applique la fonction int à chaque élément de la liste obtenue pour convertit chaque chaîne en entier.
# Enfin, list() transforme le résultat en liste de trois entiers.
# On affecte respectivement ces trois valeurs aux variables n, h, w.
n, h, w = list(map(int, input().split()))

# Initialise une variable ans à 0.
# Cette variable sert de compteur pour compter le nombre de cas qui vérifient une certaine condition par la suite.
ans = 0

# Utilise une boucle for pour itérer depuis i = 0 jusqu'à i = n-1 inclus.
# La fonction range(n) génère une séquence de n entiers (0, 1, ..., n-1).
for i in range(n):
    # À chaque itération, demande à l'utilisateur d'entrer deux entiers séparés par des espaces.
    # Utilise input() pour lire la saisie utilisateur.
    # split() sépare la chaîne saisie en une liste de deux éléments.
    # map(int, ...) convertit les deux éléments en entiers.
    # list() transforme ce résultat en une liste de deux entiers.
    # Affecte la première valeur à la variable a et la deuxième à la variable b.
    a, b = list(map(int, input().split()))
    
    # Vérifie si la valeur de a est supérieure ou égale à h ET la valeur de b est supérieure ou égale à w.
    # L'opérateur >= signifie "supérieur ou égal à" en Python.
    # L'opérateur and est un opérateur logique qui renvoie True si les deux conditions sont vraies.
    if a >= h and b >= w:
        # Si la condition est vraie, incrémente ans de 1.
        # L'opérateur += additionne 1 à la valeur actuelle de ans.
        ans += 1

# Affiche la valeur finale de la variable ans.
# La fonction print() affiche le résultat à l'écran.
print(ans)