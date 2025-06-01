def lire_entier():
    return int(input())

def lire_triplet():
    return map(int, input().split())

def initialiser_listes(n):
    return [], [], []

def ajouter_element_listes(a_list, b_list, c_list, a, b, c):
    a_list.append(a)
    b_list.append(b)
    c_list.append(c)

def compter_valeurs(liste, valeur):
    return liste.count(valeur)

def calculer_somme_unique(a, b, c, A, B, C):
    somme = 0
    if compter_valeurs(A, a) == 1:
        somme += a
    if compter_valeurs(B, b) == 1:
        somme += b
    if compter_valeurs(C, c) == 1:
        somme += c
    return somme

def afficher_resultat(valeur):
    print(valeur)

def main():
    N = lire_entier()
    A, B, C = initialiser_listes(N)
    for _ in range(N):
        a, b, c = lire_triplet()
        ajouter_element_listes(A, B, C, a, b, c)

    ans = [0] * N
    for i in range(N):
        a, b, c = A[i], B[i], C[i]
        ans[i] = calculer_somme_unique(a, b, c, A, B, C)
        afficher_resultat(ans[i])

main()