# Déclaration d'une liste 'a' qui sera créée à partir de la lecture de 10 nombres entiers depuis l'entrée utilisateur
# La comprehension de liste [int(input()) for i in range(10)] effectue 10 itérations (i allant de 0 à 9)
# À chaque itération, elle exécute input() qui attend une entrée utilisateur sous forme de chaîne de caractères
# La fonction int() convertit cette chaîne en nombre entier
# Ainsi, après la compréhension, 'a' est une liste de 10 entiers fournis par l'utilisateur
a = [int(input()) for i in range(10)]

# Initialisation d'une liste vide 'b'
b=[]

# Tri de la liste 'a' en ordre décroissant à l'aide de la fonction sorted()
# sorted(a, reverse=True) retourne une nouvelle liste triée sans modifier 'a'
# Ensuite, on récupère uniquement les 3 premiers éléments de cette liste triée grâce à la notation [:3]
# Ces 3 éléments correspondent aux 3 plus grandes valeurs de la liste 'a' car le tri est dans l'ordre décroissant
# On stocke cette sous-liste dans 'b'
b=sorted(a, reverse=True)[:3]

# Affichage de la somme des 3 nombres les plus grands stockés dans 'b'
# b[0], b[1], b[2] accèdent respectivement au premier, deuxième et troisième élément de la liste 'b'
# L'addition de ces 3 éléments donne la somme des 3 plus grands nombres
# La fonction print() affiche cette somme à l'écran
# L'argument end=' ' dans print() permet de remplacer le saut de ligne habituel par un espace,
# ainsi le prochain affichage sera sur la même ligne, juste après cette somme et suivi d'un espace
print(b[0]+b[1]+b[2],end=' ')

# Déclaration d'une liste 'c' similaire à 'a', contenant 10 nombres entiers lus depuis l'entrée utilisateur
c= [int(input()) for i in range(10)]

# Initialisation d'une liste vide 'd'
d=[]

# Tri de la liste 'c' en ordre décroissant et extraction des 3 premiers éléments
# Fonctionne comme pour 'b' et 'a'
d=sorted(c, reverse=True)[:3]

# Affichage de la somme des 3 plus grandes valeurs contenues dans 'd'
# Contrairement à l'affichage précédent, on utilise ici le print() sans argument end,
# ce qui provoque un saut de ligne après l'affichage
print(d[0]+d[1]+d[2])