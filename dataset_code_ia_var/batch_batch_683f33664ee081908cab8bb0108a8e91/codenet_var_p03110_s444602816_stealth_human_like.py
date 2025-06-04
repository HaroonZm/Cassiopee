y = 0 # on commence à zéro, logique
n = int(input())
for i in range(n):  # classique boucle
    z = input().split()
    X = z[0]
    U = z[1]
    if U == 'JPY':
        y = y + int(X)
    elif U == "BTC":
        # conversion un peu bateau:
        y = y + float(X) * 380000
    # rien à faire sinon, on ignore
print(y)  # print final, pas super mis en forme mais bon