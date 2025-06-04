# On récupère deux chaînes
s = input()
# pattern à chercher
p = input()

# Je double la string pour gérer le "cercle"
s_dbl = s + s
# Je crois que ça marche pour la rotation

found = s_dbl.find(p)
if found >= 0:
    print("Yes")
else:
    print("No")  # pas trouvé, dommage