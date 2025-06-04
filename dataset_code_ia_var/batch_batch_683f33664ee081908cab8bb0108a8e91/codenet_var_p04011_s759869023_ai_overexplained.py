# Demande à l'utilisateur de saisir une valeur depuis le clavier.
# La fonction input() récupère une chaîne de caractères.
# La fonction int() convertit cette chaîne de caractères en un entier.
# On affecte l'entier obtenu à la variable n.
n = int(input())

# Même principe que ci-dessus : on saisit une valeur, la convertit en entier et la stocke dans k.
k = int(input())

# On saisit une troisième valeur de la même manière, qu'on nomme x.
x = int(input())

# Enfin, on saisit une quatrième valeur, qu'on nomme y.
y = int(input())

# On calcule le minimum entre n et k.
# La fonction min() prend deux arguments et renvoie le plus petit.
# Par exemple, si n = 5 et k = 3, min(5, 3) vaudra 3.
# On stocke ce minimum dans la variable a.
a = min(n, k)

# On calcule la différence entre n et k. Cela peut donner un résultat négatif ou nul.
# Mais ici, on utilise max() pour s'assurer que la valeur ne soit pas inférieure à 0.
# max(n-k, 0) renvoie n-k si n-k >= 0, sinon renvoie 0.
# Cela permet d'éviter des nombres négatifs si k > n.
# On stocke ce résultat dans la variable b.
b = max(n - k, 0)

# On calcule le résultat final en multipliant a par x, puis en ajoutant b multiplié par y.
# a * x signifie que l'on fait x autant de fois qu'il y a d'éléments dans a.
# b * y signifie que l'on fait y autant de fois qu'il y a d'éléments dans b.
# Le résultat de a * x + b * y est affiché à l'écran grâce à print().
print(a * x + b * y)