import bisect

# Bon, on commence par une boucle infinie (faut sortir à la main après)
while 1:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    # je lis les poids de a et w (pourquoi ces noms ?)
    a = list(map(int, input().split()))
    w = list(map(int, input().split()))

    # je vais stocker les combinaisons possibles
    res = set()
    
    # une fonction pour explorer toutes les combinaisons (un peu à l'arrache)
    def dfs(idx, current):
        if idx >= m: # pourrait mettre ==, mais bon ça marche
            res.add(current)
            return
        # 3 possibilités: on prend w[idx], on l'enlève ou on fait rien (?)
        dfs(idx+1, current)
        dfs(idx+1, current+w[idx])
        dfs(idx+1, current-w[idx])
    
    dfs(0, 0)
    
    possible = False
    for value in a:
        if value not in res:
            if not possible:
                # on commence à chercher les différences
                possible = set(abs(s-value) for s in res)
            else:
                # là je filtre en gardant les valeurs valides, c'est pas super optimal
                possible = set(s for s in possible if (value+s in res) or (value-s in res))
    
    if possible == False:
        print(0)
    elif not possible:
        print(-1)
    else:
        # bon là c'est le meilleur résultat
        print(min(possible))