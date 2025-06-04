def lire_N():
    return int(input())

def lire_entier():
    return int(input())

def est_impair(n):
    return n % 2 == 1

def afficher_first():
    print('first')

def afficher_second():
    print('second')

def traiter_entier(a):
    if est_impair(a):
        afficher_first()
        quitter()
    return

def quitter():
    exit()

def boucle_principale(N):
    for _ in range(N):
        a = lire_entier()
        traiter_entier(a)
    afficher_second()

def main():
    N = lire_N()
    boucle_principale(N)

main()