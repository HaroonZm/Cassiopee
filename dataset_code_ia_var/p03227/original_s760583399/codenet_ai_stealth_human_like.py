# Voilà, on prend l'entrée mais je me demande si c'est la bonne méthode...
txt = input()
if len(txt) == 2:  # Si c'est deux caractères, on affiche tel quel (c'est peut-être trop simple ?)
    print(txt)
else:
    # J'inverse comme ils ont dit, mais uniquement les 3 premiers, pourquoi pas tous ? A voir
    print(txt[2] + txt[1] + txt[0])  # Hm, ça buggera si la taille est < 3, m'enfin tant pis