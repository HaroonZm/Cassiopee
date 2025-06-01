import sys

def initialiser_arr():
    return {'A':1,'B':0,'C':0}

def lire_lignes():
    return sys.stdin

def splitter_ligne(line):
    return line.split(',')

def extraire_n(s):
    return s[0]

def extraire_m(s):
    return s[1][0]

def condition_inversion(arr, n, m):
    return arr[n] == 1 or arr[m] == 1

def inverser_valeur(val):
    return (val + 1) % 2

def appliquer_inversion(arr, n, m):
    arr[n] = inverser_valeur(arr[n])
    arr[m] = inverser_valeur(arr[m])

def traitement_ligne(arr, line):
    s = splitter_ligne(line)
    n = extraire_n(s)
    m = extraire_m(s)
    if condition_inversion(arr, n, m):
        appliquer_inversion(arr, n, m)

def afficher_resultats(arr):
    for k, v in arr.items():
        if v == 1:
            print(k)

def main():
    arr = initialiser_arr()
    for line in lire_lignes():
        traitement_ligne(arr, line)
    afficher_resultats(arr)

if __name__ == "__main__":
    main()