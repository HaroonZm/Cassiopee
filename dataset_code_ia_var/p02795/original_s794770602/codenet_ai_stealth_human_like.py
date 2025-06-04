import math

def get_integer():
    # Petite fonction, juste pour demander un entier à l'utilisateur
    return int(input()) # On suppose que l'utilisateur sait ce qu'il fait

# Récupérer la hauteur
H = get_integer()
W = get_integer()
N = get_integer()   # le nombre total (?)

length = max(H, W)
# J'aurais pu appeler ça max_side, tant pis

answer = math.ceil(N / float(length))  # on divise, normalement ça donne ce qu'il faut

print(int(answer)) # juste au cas où, on imprime bien un entier