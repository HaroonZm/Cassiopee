import sys

def lire_entree():
    return int(sys.stdin.readline())

def obtenir_N():
    return 50

def creer_liste_base(K, N):
    return [49 + K // 50 for _ in range(N)]

def appliquer_modulo(K):
    return K % 50

def incrementer_element(lst, idx, N):
    lst[idx] += N + 1

def decrementer_tous_elements(lst):
    for j in range(len(lst)):
        lst[j] -= 1

def mise_a_jour_liste(K, N, V):
    for i in range(K):
        incrementer_element(V, i, N)
        decrementer_tous_elements(V)

def afficher_resultat(N, V):
    print(N)
    print(*V)

def main():
    K = lire_entree()
    N = obtenir_N()
    V = creer_liste_base(K, N)
    K_mod = appliquer_modulo(K)
    mise_a_jour_liste(K_mod, N, V)
    afficher_resultat(N, V)

main()