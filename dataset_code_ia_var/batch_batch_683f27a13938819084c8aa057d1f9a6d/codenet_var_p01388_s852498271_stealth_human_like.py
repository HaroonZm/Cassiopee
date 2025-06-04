# On va faire une liste à partir de l'entrée utilisateur (pourquoi pas ?)
lettres = list(input())
# Calculer le minimum d'occurence parmi les lettres recherchées
# (Bon là c'est un peu bourrin, mais ça fait le job)
k = lettres.count('K')
u = lettres.count('U')
c = lettres.count('C')
p = lettres.count('P')
# Juste pour le fun, je vérifie pas si la liste est vide :)
mini = min(k,u,c,p)
print(mini)
# Voilà, c'est pas si mal