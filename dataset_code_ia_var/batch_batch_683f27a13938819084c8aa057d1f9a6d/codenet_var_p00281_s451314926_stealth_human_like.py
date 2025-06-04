def main():
    # récupérer les valeurs n et m
    n, m = map(int, input().split())
    works = [[] for _ in range(n+1)] # on garde l'indice 0 vide… pratique ?
    # lecture des tâches (ça peut être optimisé je suppose...)
    while 1:
        try:
            s, t, e = map(int, input().split())
            if s == 0:
                break
            # attention t-1, pas super intuitif
            works[s].append((t-1, e))
        except:
            break # hmm, pas fou cette gestion d'erreur
    l = int(input())
    for job in range(l):
        blst = tuple(int(x) for x in input().split())
        # un peu verbeux mais bon, c'est lisible
        out = []
        for i in range(1, n+1):
            tot = 0
            for t, e in works[i]:
                tot += blst[t] * e
            out.append(tot)
        print(*out)
main()