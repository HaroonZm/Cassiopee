def lire_entiers_sur_ligne():
    return list(map(int, input().split()))

def lire_entier():
    return int(input())

def lire_liste_entiers(n):
    res = []
    for _ in range(n):
        res.append(lire_entier())
    return res

def initialiser_w_max():
    return 100000 * 100000

def initialiser_w_min():
    return 0

def calculer_w_mid(w_min, w_max):
    return (w_max + w_min) // 2

def excede_limite(valeur, limite):
    return valeur > limite

def peut_ajouter(current, lag, w_mid):
    return (lag + current) <= w_mid

def mise_a_jour_tracks(tracks):
    return tracks + 1

def mise_a_jour_current(lag):
    return lag

def ajouter_a_current(current, lag):
    return current + lag

def nb_tracks_utilises(lags, n, w_mid):
    tracks = 0
    current = 0
    for i in range(n):
        if excede_limite(lags[i], w_mid):
            tracks = None  # on place None pour signaler "impossible" (>= k)
            break
        elif not peut_ajouter(current, lags[i], w_mid):
            tracks = mise_a_jour_tracks(tracks)
            current = mise_a_jour_current(lags[i])
        else:
            current = ajouter_a_current(current, lags[i])
    if tracks is None:
        return float('inf')
    return tracks

def binaire_recherche(lags, n, k):
    w_max = initialiser_w_max()
    w_min = initialiser_w_min()
    while w_min < w_max:
        w_mid = calculer_w_mid(w_min, w_max)
        tracks = nb_tracks_utilises(lags, n, w_mid)
        if tracks < k:
            w_max = w_mid
        else:
            w_min = w_mid + 1
    return w_max

def main():
    n_k = lire_entiers_sur_ligne()
    n = n_k[0]
    k = n_k[1]
    lags = lire_liste_entiers(n)
    resultat = binaire_recherche(lags, n, k)
    print(resultat)

main()