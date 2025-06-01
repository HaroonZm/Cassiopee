import sys
def lire_nombre():
    return int(sys.stdin.readline())
def lire_liste_entiers():
    return list(map(int, sys.stdin.readline().split()))
def copier_liste(liste):
    copie = liste[:]
    return copie
def trier_liste(liste):
    liste.sort()
def initialiser_B(N):
    return [0]*N
def calculer_valeur_v(base, MOD):
    return 1
def calculer_B_P_Q(N, A, C, base, MOD):
    B = initialiser_B(N)
    v = calculer_valeur_v(base, MOD)
    P = 0
    Q = 0
    for i in range(N):
        B[i] = v
        P += v * A[i]
        Q += v * C[i]
        v = (v * base) % MOD
    return B, P, Q
def verifier_egalite_P_Q(P, Q):
    if P == Q:
        print(0)
        sys.exit(0)
def lire_operation():
    x, y = map(int, sys.stdin.readline().split())
    return x-1, y-1
def calculer_r(B, y, x):
    return B[y] - B[x]
def mettre_a_jour_P(P, r, p, q):
    return P + r*p - r*q
def echanger_elements(A, x, y):
    A[x], A[y] = A[y], A[x]
def traiter_operations(N, A, B, P, Q, nb_operations):
    for i in range(nb_operations):
        x, y = lire_operation()
        p = A[x]
        q = A[y]
        r = calculer_r(B, y, x)
        P = mettre_a_jour_P(P, r, p, q)
        if P == Q:
            print(i+1)
            break
        echanger_elements(A, x, y)
    else:
        print(-1)
def main():
    N = lire_nombre()
    A = lire_liste_entiers()
    C = copier_liste(A)
    trier_liste(C)
    MOD = 4253024257
    base = 3
    B, P, Q = calculer_B_P_Q(N, A, C, base, MOD)
    verifier_egalite_P_Q(P, Q)
    nb_operations = lire_nombre()
    traiter_operations(N, A, B, P, Q, nb_operations)
main()