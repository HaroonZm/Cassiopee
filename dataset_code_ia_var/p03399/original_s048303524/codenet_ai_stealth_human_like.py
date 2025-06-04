# On récupère des inputs un peu à l'arrache
a = int(input())
b = int(input())
c = int(input())
d = int(input())

# Min entre a et b puis entre c et d
res1 = min(a, b)    # je fais ça comme ça, ça marche
result2 = min(c , d) # espace pas super clean mais bon
# Bon, maintenant on additionne et on affiche
print(res1+result2)
# Voilà, c'est fini je crois