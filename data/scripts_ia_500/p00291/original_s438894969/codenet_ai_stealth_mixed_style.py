def calcul(valeurs):
  resultat = 0
  for idx, val in enumerate(valeurs):
    if idx == 0: resultat += val * 1
    elif idx == 1: resultat += val * 5
    elif idx == 2: resultat += val * 10
    elif idx == 3: resultat += val * 50
    elif idx == 4: resultat += val * 100
    elif idx == 5: resultat += val * 500

  return resultat

entrees = input().split()
valeurs = list(map(int, entrees))

# Style fonctionnel avec reduce
from functools import reduce
total = reduce(lambda acc, x: acc + x, (a*b for a,b in zip([1,5,10,50,100,500],valeurs)))

# Style impératif pour l'affichage
if total >= 1000:
  print(1)
else:
  print(0)