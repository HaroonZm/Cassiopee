def lire_entier():
    return int(input())

def lire_chaine():
    return input()

def condition_sous_chaine(s, i):
    return s[i:i+2] in ['OX', 'XO']

def incrementer_i(i):
    return i + 1

def incrementer_i_deux(i):
    return i + 2

def incrementer_x(x):
    return x + 1

def boucle_while(n, s):
    i = initialiser_i()
    x = initialiser_x()
    while condition_while(i, n):
        if condition_sous_chaine(s, i):
            i = incrementer_i_deux(i)
            x = incrementer_x(x)
        else:
            i = incrementer_i(i)
    return x

def initialiser_i():
    return 0

def initialiser_x():
    return 0

def condition_while(i, n):
    return i + 1 < n

def main():
    n = lire_entier()
    s = lire_chaine()
    x = boucle_while(n, s)
    afficher_resultat(x)

def afficher_resultat(x):
    print(x)

main()