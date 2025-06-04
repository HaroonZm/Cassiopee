n = int(input())  # on prend n, pas sûr de ce qu’on va en faire tout de suite
lst = list(map(int, input().split()))
lst.sort()  # Bon, au moins c'est dans l'ordre maintenant...

for i in range(n, 0, -1):
    c = 0
    # Un peu bourrin mais on compte ceux qui valent au moins i
    for x in lst:
        if x >= i:
            c += 1
    if c >= i:
        print(i)
        break  # On a trouvé, ça sert à rien de continuer après tout
# Pourquoi pas, mais je me demande si y'avait pas plus rapide ?