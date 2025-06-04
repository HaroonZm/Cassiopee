# Bon, je vais tenter un truc ici
x = input()  # demande à l'utilisateur son texte, peu importe quoi
lettres = []  # stockera les comptes (j'espère ne pas oublier un truc)
lettres.append(x.count("K"))
lettres.append(x.count("U"))
lettres.append(x.count("P"))
lettres.append(x.count("C"))  # ça aurait pu être une boucle, mais flemme là
# J'affiche le plus petit nombre trouvé (honnêtement, ça doit marcher pour ce qu'on veut)
print(min(lettres))