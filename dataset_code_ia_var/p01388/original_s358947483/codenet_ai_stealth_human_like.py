# Bon, je crois que ça marche...  
s = input() # On lit la chaîne ici
# je fais une liste pour compter les lettres qu'on veut
lst = []
lst.append(s.count('K'))  # pour K
lst.append(s.count("U"))  # U pareil
lst.append(s.count('P')) # P aussi
lst.append(s.count("C"))# et on oublie pas le C, évidemment

# Je suis pas sûr s'il faut vraiment faire comme ça mais bon...
ans = min(lst) # je prends le plus petit
print(ans)  # on affiche le truc