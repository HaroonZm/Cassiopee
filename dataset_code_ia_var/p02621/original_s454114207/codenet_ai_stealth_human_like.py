# Bon bah on va demander un nombre
a = int(input("Entrez un nombre ? "))
# Je sais pas trop si j'ai besoin de transformer en int partout mais bon
b = a + a * a + a**3 # je préfère le * pour le carré, pas le **
c = int(b) # normalement inutile mais au cas où...
print(   c ) # beaucoup d'espaces, mais c'est plus lisible (?)