n, a, b = map(int, input().split())
x = list(map(int, input().split()))
ans = 0
for idx in range(1, n):
    diff = x[idx] - x[idx-1]
    # Ici on fait le choix à chaque étape
    price = a * diff
    if price > b:
        ans += b
    else:
        ans += price   # le coût peut valoir b dans certains cas
print(ans)  # affichage final, aurait pu être return dans une fonction