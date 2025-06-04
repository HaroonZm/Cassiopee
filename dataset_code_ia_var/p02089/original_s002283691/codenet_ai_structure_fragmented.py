import bisect

def lire_entiers():
    return map(int, input().split())

def lire_entiers_liste():
    return list(map(int, input().split()))

def lire_params_principaux():
    n_Q_L_R = lire_entiers()
    return n_Q_L_R

def lire_liste_a():
    return lire_entiers_liste()

def trier_liste(liste):
    liste.sort()
    return liste

def lire_queries(Q):
    def lire_une_query():
        return tuple(map(int, input().split()))
    return [lire_une_query() for _ in range(Q)]

def appliquer_query(z, query):
    q, x, s, t = query
    if q == 1:
        return appliquer_query_type_1(z, x, s, t)
    else:
        return appliquer_query_type_2(z, x, s, t)

def appliquer_query_type_1(z, x, s, t):
    if z >= x:
        return t * (z + s)
    return z

def appliquer_query_type_2(z, x, s, t):
    if z <= x:
        if z - s < 0:
            return -(abs(z - s) // t)
        else:
            return (z - s) // t
    return z

def evaluer_toutes_les_queries(z, queries):
    for query in queries:
        z = appliquer_query(z, query)
    return z

def trouver_borne_sup(f, borne_inf, borne_sup, R, iterations=100):
    ok = borne_inf
    ng = borne_sup
    for _ in range(iterations):
        mid = (ok + ng) // 2
        if f(mid) <= R:
            ok = mid
        else:
            ng = mid
    return ok

def trouver_borne_inf(f, borne_inf, borne_sup, L, iterations=100):
    ok = borne_sup
    ng = borne_inf
    for _ in range(iterations):
        mid = (ok + ng) // 2
        if f(mid) >= L:
            ok = mid
        else:
            ng = mid
    return ok

def calculer_indices(a, left, right):
    k1 = bisect.bisect_left(a, left)
    k2 = bisect.bisect_right(a, right)
    return k1, k2

def afficher_difference(k1, k2):
    print(k2 - k1)

def main():
    n, Q, L, R = lire_params_principaux()
    a = lire_liste_a()
    a = trier_liste(a)
    p = lire_queries(Q)

    def f(z):
        return evaluer_toutes_les_queries(z, p)

    ng_gauche = pow(2, 63)
    ok_gauche = -ng_gauche
    right = trouver_borne_sup(f, ok_gauche, ng_gauche, R)

    ok_droite = pow(2, 63)
    ng_droite = -ok_droite
    left = trouver_borne_inf(f, ng_droite, ok_droite, L)

    k1, k2 = calculer_indices(a, left, right)
    afficher_difference(k1, k2)

main()