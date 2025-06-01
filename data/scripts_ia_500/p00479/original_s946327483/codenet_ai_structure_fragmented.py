def lire_N():
    return int(raw_input())

def lire_nb_iterations():
    return int(raw_input())

def lire_a_b():
    ligne = raw_input()
    return convertir_en_entiers(ligne)

def convertir_en_entiers(chaine):
    elements = chaine.split()
    return int(elements[0]), int(elements[1])

def calculer_minimum(a, N, b):
    val1 = calculer_val1(a)
    val2 = calculer_val2(N, a)
    val3 = calculer_val3(b)
    val4 = calculer_val4(N, b)
    return min(val1, val2, val3, val4)

def calculer_val1(a):
    return a-1

def calculer_val2(N, a):
    return N - a

def calculer_val3(b):
    return b - 1

def calculer_val4(N, b):
    return N - b

def calculer_resultat(min_val):
    return min_val % 3 + 1

def afficher_resultat(resultat):
    print resultat

def boucle_principale(N, iterations):
    for _ in range(iterations):
        a, b = lire_a_b()
        min_val = calculer_minimum(a, N, b)
        resultat = calculer_resultat(min_val)
        afficher_resultat(resultat)

def main():
    N = lire_N()
    iterations = lire_nb_iterations()
    boucle_principale(N, iterations)

main()