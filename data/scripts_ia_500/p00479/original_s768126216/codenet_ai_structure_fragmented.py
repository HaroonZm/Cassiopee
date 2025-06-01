def lire_entree():
    return input()

def lire_nombre_entiers():
    return int(input())

def lire_deux_entiers():
    return map(int, raw_input().split())

def calculer_minimum(a, b, N):
    vals = [a-1, N-a, b-1, N-b]
    return min(vals)

def operation_min_modulo(min_val):
    return min_val % 3 + 1

def boucle_affichage(N, nombre_iter):
    for _ in [1]*nombre_iter:
        a, b = lire_deux_entiers()
        min_val = calculer_minimum(a, b, N)
        resultat = operation_min_modulo(min_val)
        print(resultat)

def main():
    N = int(lire_entree())
    nombre_iter = lire_nombre_entiers()
    boucle_affichage(N, nombre_iter)

main()