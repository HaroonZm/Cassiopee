def lire_entree():
    return input()

def diviser_entree(entree):
    return entree.split()

def convertir_en_int(lst):
    return list(map(int, lst))

def obtenir_x(entiers):
    return entiers[0]

def obtenir_y(entiers):
    return entiers[1]

def division_entiere(y):
    return y // 2

def addition_x_ydiv2(x, ydiv2):
    return x + ydiv2

def afficher_resultat(resultat):
    print(resultat)

def main():
    entree = lire_entree()
    parties = diviser_entree(entree)
    entiers = convertir_en_int(parties)
    x = obtenir_x(entiers)
    y = obtenir_y(entiers)
    ydiv2 = division_entiere(y)
    resultat = addition_x_ydiv2(x, ydiv2)
    afficher_resultat(resultat)

main()