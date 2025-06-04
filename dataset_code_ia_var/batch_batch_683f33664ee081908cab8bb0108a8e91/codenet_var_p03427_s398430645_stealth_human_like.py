s = input()
longueur = len(s)
# On vérifie si le chiffre commence par n'importe quoi suivi de 9... Peut-être à améliorer ?
if s[0] + "9"*(longueur-1) == s:
  print(int(s[0]) + 9*(longueur-1))  # OK, ça passe
else:
  resultat = int(s[0]) - 1 + 9*(longueur-1)
  print(resultat) # Pas sûr que ça soit optimal, mais bon