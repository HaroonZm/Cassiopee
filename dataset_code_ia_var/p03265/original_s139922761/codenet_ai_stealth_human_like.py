# Ok, je vais essayer d'écrire ça comme je le ferais un dimanche soir

a, b, c, d = map(int, input().split())  # lecture un peu bourrine, mais ça fait le taf

# calcul des déplacements (flemme de nommer les variables mieux)
dx = c - a
dy = d - b

# on bidouille un peu les coordonnées
x1 = c - dy
y1 = d + dx
x2 = a - dy  # Là je crois que ça marche mais bon, faudrait vérifier...
y2 = b + dx

print(x1, y1, x2, y2)  # On affiche tout, normalement c'est bon ?