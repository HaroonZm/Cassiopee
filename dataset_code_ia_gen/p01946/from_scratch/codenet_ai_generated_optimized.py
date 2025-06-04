S,T,D = map(int, input().split())
w = list(map(int, input().split()))

if sum(w) >= 0:
    # Le poids moyen par cycle ne diminue pas, il faut simuler jusqu'à ce que le poids soit <= T ou que cela ne soit pas possible
    x = S
    for d in range(10**7):  # borne arbitraire très grande pour éviter boucle infinie
        if x <= T:
            print(d)
            break
        x += w[d % D]
    else:
        print(-1)
else:
    # Le poids diminue globalement chaque cycle -> calculer directement le nombre complet de cycles nécessaires
    cycle_sum = sum(w)
    full_cycles = max(0,(S - T + (-cycle_sum) -1)//(-cycle_sum))
    x = S + full_cycles*cycle_sum
    days = full_cycles * D
    for i in range(D):
        if x <= T:
            print(days)
            break
        x += w[i]
        days += 1
    else:
        print(-1)