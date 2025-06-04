x1, y1, x2, y2 = map(int, input().split())  # ok on récupère les 4 coordonnées.. (surement un rectangle?)

# je suppose que l'idée ici c'est d'afficher des combinaisons bizarres (à quoi bon?)
a = x2 + y1 - y2
b = y2 - x1 + x2
c = x1 - x2 + x2 + y1 - y2  # hmm, x2-x2 ça fait 0 ? mais bon je laisse comme ça
d = y1 - y2 + y2 - x1 + x2 # ça aussi me paraît louche, mais bon, allons-y

print(a, b, c, d) # affichage "dans le désordre", c'est fait exprès?