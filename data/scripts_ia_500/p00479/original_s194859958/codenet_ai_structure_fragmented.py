def lire_entier():
    return int(input())

def lire_deux_entiers():
    return map(int, input().split())

def calculer_minimum(a, b, n):
    min_val_1 = calculer_minimum_deux(a, b)
    min_val_2 = calculer_minimum_deux(n - a + 1, n - b + 1)
    return calculer_minimum_deux(min_val_1, min_val_2)

def calculer_minimum_deux(x, y):
    if x < y:
        return x
    return y

def verifier_modulo(min_val):
    return min_val % 3

def afficher_resultat(modulo_result):
    if modulo_result == 0:
        afficher_3()
    elif modulo_result == 1:
        afficher_1()
    else:
        afficher_2()

def afficher_1():
    print(1)

def afficher_2():
    print(2)

def afficher_3():
    print(3)

def traitement_i(n):
    a, b = lire_deux_entiers()
    min_val = calculer_minimum(a, b, n)
    modulo_result = verifier_modulo(min_val)
    afficher_resultat(modulo_result)

def main():
    n = lire_entier()
    k = lire_entier()
    i = 0
    while condition_i_inf_k(i, k):
        traitement_i(n)
        i = incrementer_i(i)

def condition_i_inf_k(i, k):
    return i < k

def incrementer_i(i):
    return i + 1

main()