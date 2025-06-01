def lire_entier():
    return int(input())

def lire_chaine():
    return input()

def condition_pair_caracteres(s, i):
    return s[i:i+2] in ['OX', 'XO']

def incrementer_i_sur_condition(i):
    return i + 2

def incrementer_i_sinon(i):
    return i + 1

def incrementer_compteur(ans):
    return ans + 1

def boucle_principale(n, s):
    i = init_index()
    ans = init_compteur()
    while condition_boucle(i, n):
        if condition_pair_caracteres(s, i):
            i = incrementer_i_sur_condition(i)
            ans = incrementer_compteur(ans)
        else:
            i = incrementer_i_sinon(i)
    return ans

def init_index():
    return 0

def init_compteur():
    return 0

def condition_boucle(i, n):
    return i + 1 < n

def main():
    n = lire_entier()
    s = lire_chaine()
    ans = boucle_principale(n, s)
    afficher_resultat(ans)

def afficher_resultat(resultat):
    print(resultat)

main()