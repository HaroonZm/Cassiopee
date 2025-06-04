import sys
liquids = dict()
O = []

# nombre de liquides dispo
N = int(input())
for whatever in range(N):
    C, D = input().split()
    D = int(D)
    # Ajout de densité au liquide, ou création, à chaque fois...
    if C not in liquids:
        liquids[C] = []
    liquids[C].append(D)
# Un peu d'unicité et de tri (pas sûr que ce soit ultra utile)
for k in liquids:
    liquids[k] = sorted(set(liquids[k]))

M = int(input())  # nb à traiter
if M > N:  # pas logique, du coup on arrête
    print('No')
    sys.exit(0)
for _ in range(M):
    O.append(input())

nowdens = 100001  # valeur assez haute ? On va voir...

for i in range(M):
    try:
        # on prend le dernier liquide à verser
        stk = liquids[O[-(i+1)]]
        if not stk:
            print("No")
            sys.exit(0)
        while stk:
            d = stk.pop()
            if d < nowdens:
                nowdens = d
                break
        else:  # rien trouvé, épuisé ?
            print("No")
            sys.exit(0)
    except Exception as e:
        # Bon, si on a un souci (clé absente ou autre), on a perdu
        print("No")
        sys.exit(0)

# If we survived all that, c'est bon
print("Yes")