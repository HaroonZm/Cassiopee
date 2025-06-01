def lire_entier():
    return int(input())

def lire_chaine():
    return list(input().strip())

def initialiser_compteurs():
    return 0, 1, 0

def caracteres_differents(S, i, j):
    return S[i] != S[j]

def incrementer_compteurs_paires(cnt1, cnt2):
    return cnt1 + 2, cnt2 + 2

def incrementer_compteurs_simples(cnt1, cnt2):
    return cnt1 + 1, cnt2 + 1

def traitement(N, S):
    cnt1, cnt2, stamp_0x = initialiser_compteurs()
    
    while cnt1 < N:
        if cnt1 < N - 1:
            if caracteres_differents(S, cnt1, cnt2):
                stamp_0x = incrementer_stamp(stamp_0x)
                cnt1, cnt2 = incrementer_compteurs_paires(cnt1, cnt2)
            else:
                cnt1, cnt2 = incrementer_compteurs_simples(cnt1, cnt2)
                continue
        else:
            cnt1 = incrementer_compteur_simple(cnt1)
    return stamp_0x

def incrementer_stamp(stamp):
    return stamp + 1

def incrementer_compteur_simple(cnt):
    return cnt + 1

def main():
    N = lire_entier()
    S = lire_chaine()
    resultat = traitement(N, S)
    print(resultat)

main()