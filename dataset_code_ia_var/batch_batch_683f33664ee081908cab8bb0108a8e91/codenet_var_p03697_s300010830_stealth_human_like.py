# Bon alors on lit les deux nombres, séparés par un espace
mots = input().split()
a = int(mots[0])  # premier nombre
b = int(mots[1])  # deuxième nombre (c'est logique !)

somme = a + b

if somme < 10:
    print(somme)
else:
    # Je crois qu'on doit afficher 'error' ?
    print("error")