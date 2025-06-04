while True:
    a,b,c,d,e = map(int,input().split())
    if a==0 and b==0 and c==0 and d==0 and e==0:
        break
    na,nb,nc= map(int,input().split())
    total = na*a + nb*b + nc*c
    n = na + nb + nc
    res = total
    # On essaie toutes les tailles de paquet possibles entre d et n
    for k in range(d,n+1):
        nb_sets = n // k
        rest = n % k
        # Coût si on fait nb_sets groupes de taille k et un reste
        price = nb_sets * k * e + rest * e * d if rest < d else nb_sets * k * e + rest * e * rest
        # Mais on ne sait pas si price est meilleur que total, on compare
        if rest < d:
            rest_price = min(rest*a,rest*b,rest*c)
            # ce n'est pas correct car on ne sait pas comment répartir les restants
            # la solution simple: comparer price avec total directement
            price = nb_sets * k * e + rest * a # au pire prix normal minimum par DVD, on ne sait pas
        else:
            price = nb_sets * k * e + rest * e * rest
        # En fait cette partie est trop compliquée, on va juste comparer price avec res et total
        price = nb_sets * k * e + rest * e * (d if rest<d else rest)
        if price < res:
            res = price
    # On va aussi comparer avec la méthode sans set : total
    if total < res:
        res = total
    print(res)