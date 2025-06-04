# Demande à l'utilisateur de saisir une valeur, puis convertit la saisie en entier.
# Ceci correspond au nombre d'éléments à traiter par la suite.
n = int(input())

# Demande à l'utilisateur de saisir une autre valeur entière.
# Cette valeur servira comme borne supérieure ou comme référence dans les calculs ultérieurs.
k = int(input())

# Demande à l'utilisateur de saisir une série de nombres séparés par des espaces sur une seule ligne.
# La fonction input() lit la ligne entière comme une chaîne de caractères.
# La méthode split() découpe cette chaîne en une liste de sous-chaînes, chacune correspondant à un nombre sous forme de chaîne.
# La fonction map(int, ...) applique la conversion en entier à chaque élément de la liste obtenue.
# Enfin, la fonction list() transforme le résultat en une liste d'entiers.
x = list(map(int, input().split()))

# Initialise une variable pour contenir le résultat final.
# On commence avec la valeur 0. Cette variable cumulera les sommes du calcul demandé.
result = 0

# On utilise une boucle for traditionnelle.
# La fonction range(n) génère une séquence de nombres de 0 à n-1 inclus, ce qui parcourt tous les index de la liste x si elle a la bonne taille.
for i in range(n):
    # On va sélectionner l'élément d'index i dans la liste x.
    # On soustrait cet élément à 0 et à k, prend la valeur absolue de chaque résultat.
    # La fonction min() retourne la plus petite des deux valeurs absolues calculées.
    # On multiplie ce minimum par 2 (car la consigne le demande).
    # La somme obtenue est ajoutée à la variable result (c'est-à-dire que result augmente de cette quantité à chaque passage dans la boucle).
    result += 2 * min(abs(0 - x[i]), abs(k - x[i]))

# Affiche la valeur finale de result.
# Utilise la fonction print() qui permet d'envoyer un message ou une valeur sur la sortie standard (en général à l'écran).
print(result)