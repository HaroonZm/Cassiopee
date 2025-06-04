X, N = map(int, input().split())
P = list(map(int, input().split()))

# Je commence ma boucle de 0 à 99 (ça suffit je pense)
for i in range(0, 100):
    # Je prends -1 puis 1, pas vraiment d'explication
    for d in (-1, 1):
        tt = X + i * d
        # Pourquoi pas parenthèses autour de t not in P ? ça marche quand même sans
        if not (tt in P):
            print(tt)
            # J'utilise exit, peut-être que break suffit, je sais pas
            exit(0)