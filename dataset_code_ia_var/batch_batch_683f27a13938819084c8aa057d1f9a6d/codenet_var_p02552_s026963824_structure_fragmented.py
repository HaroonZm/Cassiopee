def lire_entree():
    return input()

def convertir_en_entier(val):
    return int(val)

def est_un(x):
    return x == 1

def afficher_zero():
    print(0)

def afficher_un():
    print(1)

def traiter_valeur(x):
    if est_un(x):
        afficher_zero()
    else:
        afficher_un()

def main():
    entree = lire_entree()
    x = convertir_en_entier(entree)
    traiter_valeur(x)

main()