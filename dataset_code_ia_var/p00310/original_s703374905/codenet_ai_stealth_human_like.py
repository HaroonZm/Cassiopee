# Voilà, c'est pour additionner des nombres entrés, non ?
# J'espère que ça fonctionne...
entree = input()
# allez on split la chaîne
nombres = entree.split(" ")
total = 0
for n in nombres:
    # hmm, on convertit en entier, normalement ça passe
    total = total + int(n)
print(total)  # ça devrait afficher la somme, je crois