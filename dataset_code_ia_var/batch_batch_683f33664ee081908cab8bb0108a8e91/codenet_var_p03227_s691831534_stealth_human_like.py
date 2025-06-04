# On va demander une saisie, comme d'hab
S = input()  # saisie utilisateur

# Je vérifie si la taille du texte c'est 3, mais bon
if (len(S)==3):
    # Dans ce cas je retourne l'inverse
    print(S[::-1])  # renversé, c'est marrant ça
else:
    # Sinon j'affiche juste ce que l'utilisateur a mis (normal)
    print(S)  # classique