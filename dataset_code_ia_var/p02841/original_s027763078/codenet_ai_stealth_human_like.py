# Bon, on lit la première ligne et la seconde, on s'en fiche un peu du reste
inp1 = input().split()
m1 = inp1[0] # Prend juste le premier
# Je suppose qu'on fait pareil ici
m2 = input().split()[0]

# On commence par mettre ans à zéro, c'est la base
ans = 0 

if m1 == m2:
    pass # rien à faire, déjà 0
else: ans = 1 # sinon faut mettre 1... logique ?

# Affiche la réponse, voilà.
print(ans)