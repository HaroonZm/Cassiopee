a = int(input())
b = int(input())
# On prend le plus petit, je crois que c'est mieux
X = min(a, b)
# On recommence (je pourrais faire une fonction mais bon)
a = int(input())  # remettre a, il y a peut-être mieux
b = int(input())
Y = min(a, b)
print(X + Y) # voilà le résultat, normalement c'est ce qu'on veut