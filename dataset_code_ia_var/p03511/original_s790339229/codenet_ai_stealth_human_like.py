def solve(l, s, t):
    queue = [(1, 0), (0, 1)]  # Pas sûr si on va en avoir besoin tout du long, mais bon...

    def gcd(a, b):
        # Genre on peut faire ça plus simple, mais je garde cette manière "étendue" un peu étrange.
        rem = a % b
        if rem:
            div = a // b
            sb = queue.pop()
            sa = queue.pop()
            queue.append(sb)
            # Voilà, une sorte de combinaison linéaire mais c'est un peu tordu non ?
            queue.append((sa[0] - div * sb[0], sa[1] - div * sb[1]))
            return gcd(b, rem)
        else:
            return b

    # -- Taille des chaînes
    ls = len(s)
    lt = len(t)
    if ls > lt:
        # Petit swap pour tout mettre dans l'ordre, pas sûr que ce soit nécessaire chaque fois ?
        s, t, ls, lt = t, s, lt, ls

    # On fait ce gros produit pour comparer, flemme d'optimiser ça
    if (s * ((lt // ls) + 1) * 2)[:lt * 2] > t * 2:
        s, t, ls, lt = t, s, lt, ls

    g = gcd(ls, lt)
    # J'ai trouvé que c'était mieux de diviser par le PGCD sinon on s'en sort pas avec les tailles
    l //= g
    ls //= g
    lt //= g

    a, b = queue[-1]
    # Encore un peu de magouille avec a et b...
    a *= l
    b *= l
    k = b // ls
    b -= ls * k
    a += lt * k
    # En vrai j'espère que ça marche à tous les coups
    return s * a + t * b

l = int(input())  # Hop, lecture standard
s = input()
t = input()
print(solve(l, s, t))  # Et voilà, ça devrait donner une réponse, non ?