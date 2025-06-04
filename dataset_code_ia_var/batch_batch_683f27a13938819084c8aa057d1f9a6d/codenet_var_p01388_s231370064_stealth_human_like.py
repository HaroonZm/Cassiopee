# J'ai essayé de faire comme je pouvais
s = input()

k = s.count("K")
u = s.count('U')
# J'ai oublié s.count pour P aussi
p = s.count("P")
c = s.count('C')
ma_liste = [k, u, p, c] # J'aurais p'têt pu faire une boucle, mais bon
minimum = min(ma_liste)
# on affiche ce qu'il faut non?
print(minimum)