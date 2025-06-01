def lire_entrees_avec_break():
    A = {}
    while True:
        S = lire_chaine()
        if fin_chaine(S):
            break
        x, y = extraire_coordonnees(S)
        maj_dictionnaire(A, x)
    return A

def lire_chaine():
    return input()

def fin_chaine(s):
    return s == ''

def extraire_coordonnees(s):
    return map(int, s.split(','))

def maj_dictionnaire(d, key):
    if key in d:
        d[key] += 1
    else:
        d[key] = 1

def lire_entrees_avec_eof():
    B = {}
    while True:
        try:
            x, y = extraire_saisie()
        except EOFError:
            break
        maj_dictionnaire(B, x)
    return B

def extraire_saisie():
    return map(int, input().split(','))

def afficher_sommes(A, B):
    for i in obtenir_cles(A):
        if cle_existe(B, i):
            print_cle_somme(i, A[i], B[i])

def obtenir_cles(dictionnaire):
    return dictionnaire.keys()

def cle_existe(dictionnaire, key):
    return key in dictionnaire

def print_cle_somme(i, valA, valB):
    print(i, valA + valB)

def main():
    A = lire_entrees_avec_break()
    B = lire_entrees_avec_eof()
    afficher_sommes(A, B)

main()