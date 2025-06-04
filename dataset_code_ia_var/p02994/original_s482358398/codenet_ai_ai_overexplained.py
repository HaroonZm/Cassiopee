# Cette ligne lit une ligne d'entrée de l'utilisateur (par défaut depuis le clavier),
# puis la divise (split) en deux parties à chaque espace. Les deux parties résultantes sont des chaînes de caractères,
# que l'on convertit en entiers (int) grâce à la fonction map. Enfin, on récupère ces deux entiers et on les assigne respectivement
# aux variables n et l. Par exemple, si l'utilisateur tape "3 5", alors n=3 et l=5.
n, l = map(int, input().split())

# Ici, on initialise une variable taste avec la valeur 10000.
# Cette variable va être utilisée afin de stocker la valeur de "saveur la plus faible en valeur absolue"
# rencontrée lors de l'itération dans la boucle suivante.
taste = 10000

# On utilise une boucle for afin de parcourir tous les entiers allant de 1 jusqu'à n inclus (attention : range(a, b) s'arrête à b-1).
# Donc range(1, n+1) permet d'obtenir la séquence 1, 2, 3, ..., n une à une sous forme de la variable i.
for i in range(1, n + 1):
    # Pour chaque i, on évalue la valeur suivante : l + i - 1.
    # Cela correspond à tester successivement l, l+1, l+2, ..., l+n-1.
    # Ensuite, on calcule la valeur absolue de taste (débutant à 10000, qui est très grand pour assurer la prise de la première valeur),
    # puis la valeur absolue de l + i - 1 et on compare les deux.
    # Si la valeur absolue courante (abs(l+i-1)) est plus petite que la plus petite trouvée jusqu'à présent,
    # alors taste prend la nouvelle valeur (non absolue !)
    if abs(taste) > abs(l + i - 1):
        # On remplace taste par la valeur courante l + i - 1.
        taste = l + i - 1

# Après la boucle, taste contient l'élément de la séquence l, l+1, ..., l+n-1 dont la valeur absolue est la plus faible.

# Maintenant, nous calculons et affichons le résultat final.
# Détaillons chaque partie du calcul :
# n * l : produit le nombre total d'éléments multiplié par la valeur de départ l,
# ce qui donnerait la somme si tous les éléments étaient égaux à l.
# n * (n + 1) // 2 : calcule la somme des entiers de 1 à n.
# Par exemple, pour n=3, cela fait 1+2+3=6. Nous utilisons // pour la division entière (pas de virgule).
# On soustrait n pour ajuster la somme (car dans cette séquence l, l+1, ..., l+n-1, la somme réelle est n*l + somme de 0 à n-1).
# Enfin, on soustrait la valeur taste (la "saveur" à enlever) selon le problème sous-jacent,
# pour obtenir le résultat final en excluant la valeur la plus "neutre" selon la valeur absolue.
print(n * l + (n * (n + 1) // 2) - n - taste)