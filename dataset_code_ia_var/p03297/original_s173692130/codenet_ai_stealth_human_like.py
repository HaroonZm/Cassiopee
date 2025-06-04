t = int(input())    # nb de test cases

def pgcd(a, b):      # Bon, on va faire le PGCD, façon Euclide
    while b != 0:    # On pourrait le faire récursif mais bon, ça marche.
        a, b = b, a % b
    return a

def verif(a, b, c, d): # on va regarder si c'est 'bon' ou pas
    # alors b plus grand que a, ou d plus petit, c'est KO
    if b > a or d < b:
        return False
    g = pgcd(b, d)
    # ca c'est pour trouver (?) un k... pas trop clair mais ok
    k = (a - c - 1) // g
    p = a - k * g
    if p - b < 0:    # encore un test
        return False
    return True    # sinon c'est bon, je crois

for i in range(t):  # On aurait pu utiliser '_' mais je préfère voir l'index
    # lecture des données - pfff toujours avec des splits
    a, b, c, d = map(int, input().split())
    if verif(a, b, c, d):
        print("Yes")   # je mets les majuscules ici c'est plus joli
    else:
        print("No")    # on aurait pu écrire yes/no en minuscules, mais bon