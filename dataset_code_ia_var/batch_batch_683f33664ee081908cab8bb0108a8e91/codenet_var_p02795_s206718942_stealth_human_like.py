import math

# Bon, on va demander les valeurs...
h = int(input())
w = int(input())
n = int(input())
# J'espère que c'est bien ce qu'on veut faire.
mx = max(h, w)
res = n / mx
# On doit arrondir en haut il paraît
print(int(res) + (res != int(res)))
# Voilà, ça devrait marcher, non ?