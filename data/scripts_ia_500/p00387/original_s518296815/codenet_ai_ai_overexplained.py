# On commence par lire une ligne depuis l'entrée standard, c'est-à-dire le terminal ou la console, avec la fonction input().
# Cette fonction attend que l'utilisateur entre une donnée sous forme de texte (une chaîne de caractères) puis appuie sur Entrée.
# Cette chaîne de caractères peut contenir plusieurs mots ou nombres séparés par des espaces.
# Exemple : "10 3"

# Ensuite, on utilise la méthode split() sur cette chaîne de caractères.
# La méthode split() découpe la chaîne en une liste de sous-chaînes, en utilisant par défaut l'espace comme séparateur.
# Par exemple, "10 3".split() donnera la liste ['10', '3'].

# La fonction map() est utilisée pour appliquer une fonction à chaque élément d'une liste.
# Ici, on applique int, la fonction qui convertit une chaîne de caractères en un entier.
# Donc map(int, ['10', '3']) convertira chaque élément en entier, créant un itérable équivalent à [10, 3].

# Puis, on assigne ces deux valeurs entières à deux variables, a et b, grâce au mécanisme de déballage des valeurs.
# Cela signifie que la première valeur est assignée à a, la deuxième à b.
# Ainsi, a vaudra 10, b vaudra 3 dans notre exemple.

a, b = map(int, input().split())

# Maintenant, on va effectuer un calcul mathématique.
# L'expression (b + a - 1) // a est une opération entière.
# Le double slash '//' est l'opérateur de division entière en Python.
# Cela signifie que le résultat de la division sera arrondi vers le bas à l'entier le plus proche.

# Pour comprendre cette expression, on peut voir que c'est une façon d'effectuer un "arrondi vers le haut" de la division de b par a.
# Plus précisément, (b + a - 1) // a calcule combien de fois a rentre complètement dans b, mais en arrondissant à l'entier supérieur.
# Par exemple, si b=3 et a=10, (3+10-1)//10 = 12//10 = 1
# Si b=20 et a=10, (20+10-1)//10 = 29//10 = 2
# C'est une technique classique pour calculer le nombre minimal d'unités de taille a nécessaires pour couvrir b unités.

# Enfin, on affiche le résultat avec print().
# La fonction print() affiche le contenu donné à l'intérieur des parenthèses dans la console ou le terminal,
# suivi d'un retour à la ligne automatique.

print((b + a - 1) // a)