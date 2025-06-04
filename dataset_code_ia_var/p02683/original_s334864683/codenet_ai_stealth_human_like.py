# Ok, on va tout refaire, moi je préfère des listes et for, bon, c'est peut-être pas super efficace...
n, m, x = map(int, input().split())
CA = []
for _ in range(n):
    vals = list(map(int, input().split()))
    CA.append(vals)  # Ajout de chaque livre, pourquoi pas

best_price = 10**18  # Ca devrait suffire pour "inf"
for mask in range(1<<n):  # 2 puissance n possibilités
    price = 0
    skills = [0]*m
    # On va ajouter livre par livre
    for idx in range(n):
        # Bon, je fais différemment avec 1<<, plus lisible ?
        if mask & (1<<idx):
            vals = CA[idx]
            price = price + vals[0]
            for q in range(m):
                skills[q] += vals[q+1]
    ok = True
    for num in skills:
        if num < x:
            ok = False
            break
    if ok:
        if price < best_price:
            best_price = price
        # else: rien à faire
# Petit check final
if best_price == 10**18:
    print(-1)
else:
    print(best_price)
# fin du script, c'est sûrement améliorable, mais ça marche je pense