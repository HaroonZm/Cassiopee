# On commence par lire une ligne de l'entrée standard (input()), qui doit contenir deux entiers séparés par un espace
# "input()" lit la ligne sous forme de chaîne de caractères, par exemple "10 3"
# "split()" coupe cette chaîne en une liste de sous-chaînes en utilisant l'espace comme séparateur. 
# I.e., "10 3".split() donne ["10", "3"]
# "map(int, ...)" applique la fonction 'int' à chaque élément de la liste, les convertissant de chaînes de caractères à entiers. 
# "n, m = ..." affecte le premier entier à n et le deuxième à m en utilisant l'unpacking
n, m = map(int, input().split())

# On lit ensuite une deuxième ligne d'entrée qui contient m entiers séparés par des espaces
# On utilise la même méthode de 'input().split()' puis 'map(int, ...)' pour obtenir
# une séquence d'entiers, que l'on convertit ici explicitement en liste en utilisant 'list(...)'
# Cela permet de stocker les entiers pour les réutiliser plus tard
a = list(map(int, input().split()))

# On crée une nouvelle liste vide 'c' qui va contenir différents écarts calculés
# On initialise cette liste avec deux éléments :
# 1. a[0] - 1 : distance entre le premier point (a[0]) et le début (position 1)
#    - On soustrait 1 car les positions vont de 1 à n inclus
# 2. n - a[m-1] : distance entre le dernier point (a[m-1]) et la fin (position n)
#    - Cela calcule combien il y a de positions après le dernier point jusqu'à n
c = [a[0] - 1, n - a[m - 1]]

# On doit ensuite calculer les distances entre tous les points consécutifs dans la liste 'a'
# Pour ce faire, on fait une boucle 'for' sur les indices allant de 0 à m-2 inclus (soit m-1 itérations)
# - range(m - 1) donne la séquence d'entiers de 0 à m-2 inclus
for i in range(m - 1):
    # Pour chaque paire consécutive (a[i] et a[i+1]), on calcule leur écart
    # On calcule la différence a[i+1] - a[i], qui est le nombre de positions entre ces deux points
    # Puis, on fait une division entière par 2 avec l'opérateur // pour obtenir la distance maximale
    # qui peut être placée dans l'intervalle entre ces deux points, si l'on place un élément au milieu
    # Exemple: entre 3 et 7 -> (7-3) = 4 ; 4//2 = 2
    c.append((a[i + 1] - a[i]) // 2)

# On veut maintenant obtenir le maximum des différentes distances calculées, c'est-à-dire
# le plus grand nombre parmi tous les éléments de la liste 'c'
# "max(c)" renvoie la plus grande valeur contenue dans c
# 'print(...)' affiche cette valeur sur la sortie standard (terminal)
print(max(c))