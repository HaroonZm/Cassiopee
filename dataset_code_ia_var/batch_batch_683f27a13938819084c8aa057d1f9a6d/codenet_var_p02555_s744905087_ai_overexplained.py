# On commence par demander à l'utilisateur de saisir un entier qui sera stocké dans la variable N.
# La fonction input() lit l'entrée utilisateur sous forme de chaîne de caractères.
# La fonction int() convertit cette chaîne en un entier de type int.
N = int(input())

# On prépare une liste appelée memo qui contiendra les résultats de nos calculs intermédiaires.
# Cette liste est prédéfinie avec les valeurs pour les indices 0, 1, 2 et 3.
# Cela permet d'éviter de recalculer ces valeurs de base.
# Ici, memo[0] = 0, memo[1] = 0, memo[2] = 0, memo[3] = 1.
# L'utilisation de cette liste sert au principe de la programmation dynamique afin de mémoriser
# les résultats déjà obtenus et d'améliorer l'efficacité du code.
memo = [0, 0, 0, 1]

# On crée une boucle for pour remplir la liste memo pour tous les indices de 4 jusqu'à N inclus.
# range(4, N + 1) génère une séquence de nombres commençant à 4 et finissant à N inclusivement.
for i in range(4, N + 1):
    # On calcule la valeur pour l'indice i et on l'ajoute à la fin de la liste memo avec memo.append().
    # La valeur calculée est la somme de la valeur à l'indice (i - 1) et celle à l'indice (i - 3) dans memo.
    # Cette récurrence permet de définir chaque valeur de memo à partir des valeurs déjà présentes dans memo
    # selon la formule : memo[i] = memo[i - 1] + memo[i - 3]
    memo.append(memo[i - 1] + memo[i - 3])

# Après la boucle, la valeur recherchée pour l'indice N se trouve donc à memo[N].
# On souhaite afficher le résultat modulo 10^9 + 7 afin d'éviter d'avoir un trop grand nombre,
# ce qui est une pratique courante dans les problèmes de programmation compétitive pour éviter
# les dépassements de capacité des entiers.
# L'opérateur % (modulo) donne le reste de la division entière de memo[N] par 1_000_000_007.
print(memo[N] % (10**9 + 7))