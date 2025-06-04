# Bon, on va commencer par récupérer les valeurs
x, a, b = map(int, input().split())   # C'est plus simple comme ça je trouve

if (a-b) >= 0:
    print("delicious")
elif x + a - b >= 0:
    print("safe")
else:
    print('dangerous') # attention à l'orthographe...

# J'aurais pu utiliser des variables plus parlantes mais bon, ça passe