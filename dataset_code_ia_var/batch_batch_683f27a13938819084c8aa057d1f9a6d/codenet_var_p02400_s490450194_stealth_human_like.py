import math

# allez on prend r depuis l'utilisateur, j'espère qu'il rentre bien un nombre...
r = float(input())

# area et circumference, bon on fait ça en une ligne pour aller plus vite
print(str(r*r*math.pi)[:12], "{0:.10f}".format(2*r*math.pi))
# oups, j'ai mélangé deux façons de formatter... tant pis, ça passe