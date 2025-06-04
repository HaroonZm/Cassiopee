def lire_entree():
    return input()

def parser_entree(entree):
    return entree.split()

def convertir_entree(chaine_list):
    return list(map(int, chaine_list))

def get_a(entiers):
    return entiers[0]

def get_b(entiers):
    return entiers[1]

def est_divisible_par_3(x):
    return x % 3 == 0

def somme(x, y):
    return x + y

def est_possible(a, b):
    if est_divisible_par_3(a):
        return True
    if est_divisible_par_3(b):
        return True
    if est_divisible_par_3(somme(a, b)):
        return True
    return False

def afficher_resultat(possible):
    if possible:
        print("Possible")
    else:
        print("Impossible")

def main():
    entree = lire_entree()
    chaines = parser_entree(entree)
    entiers = convertir_entree(chaines)
    a = get_a(entiers)
    b = get_b(entiers)
    possible = est_possible(a, b)
    afficher_resultat(possible)

main()