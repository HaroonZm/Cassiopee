import bisect

def lire_entrees():
    n, m = lire_deux_entiers()
    pos = lire_liste_positions()
    q = lire_entier_unique()
    l = lire_liste_limites()
    return n, m, pos, q, l

def lire_deux_entiers():
    return map(int, input().split())

def lire_liste_positions():
    return list(map(int, input().split()))

def lire_entier_unique():
    return int(input())

def lire_liste_limites():
    return list(map(int, input().split()))

def preparer_positions(pos, n):
    nouvelle_pos = pos[:]
    nouvelle_pos.append(n + 1)
    return nouvelle_pos

def calculer_ecarts(pos, m):
    return [pos[i+1] - pos[i] - 1 for i in range(m)]

def trier_liste(liste):
    nouvelle_liste = liste[:]
    nouvelle_liste.sort()
    return nouvelle_liste

def prefix_sum(liste, longueur):
    s = [0] * (longueur + 1)
    for i in range(len(liste)):
        s[i+1] = s[i] + liste[i]
    return s

def executer_requete(lim, n, m, d, s, pos0):
    premiere_valeur = n + 1
    valeur_min = 0
    resultat = effectuer_recherche_binaire(lim, premiere_valeur, valeur_min, d, s, m, pos0, n)
    return resultat

def effectuer_recherche_binaire(lim, ok, ng, d, s, m, pos0, n):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        idx = trouver_index(d, mid)
        cout = calculer_cout(s, idx, d, m, mid, pos0)
        if cout <= lim:
            ok = mid
        else:
            ng = mid
    if ok <= n:
        return ok
    else:
        return -1

def trouver_index(d, mid):
    return bisect.bisect_left(d, mid)

def calculer_cout(s, idx, d, m, mid, pos0):
    somme = s[-1] - s[idx]
    quantite = m - idx
    ajustement = quantite * (mid - 1)
    return somme - ajustement + (pos0 - 1)

def afficher_resultats(resultats):
    for res in resultats:
        print(res)

def main():
    n, m, pos, q, l = lire_entrees()
    pos = preparer_positions(pos, n)
    d = calculer_ecarts(pos, m)
    d = trier_liste(d)
    s = prefix_sum(d, m)
    resultats = []
    for lim in l:
        resultat = executer_requete(lim, n, m, d, s, pos[0])
        resultats.append(resultat)
    afficher_resultats(resultats)

main()