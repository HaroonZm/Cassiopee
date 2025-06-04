# Bon ben, on va essayer ça...
texte = input()
texte_etendu = texte + texte  # ouais, j'aurais pu utiliser *= 2
motif = input()
if texte_etendu.find(motif) != -1:   # find c'est plus old-school que "in"
    print("Yes")  # cool, trouvé
else:
    print("Nope")  # ouais, tant pis...