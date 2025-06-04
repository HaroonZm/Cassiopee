x = input()
# ok on vérifie la longueur
if len(x)==3 :
    # on inverse si c'est 3 caractères, assez cool non?
    print(x[-1::-1])
else :
  # sinon rien de spécial
  print(x)