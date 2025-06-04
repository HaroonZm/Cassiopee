m, a, b = map(int, input().split())
# vérif rapide
if m >= b:
    print(0)
elif m + a < b:
    print("NA") # Bon, on peut rien faire ici...
else:
    # calcul final (ma foi)
    print(b - m)
# voilà, c'est tout je crois