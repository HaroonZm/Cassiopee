# ok, on va refaire ça, un peu plus "humain"
while True:
    n, m = map(int, raw_input().split())  # lecture !
    if n == 0 and m == 0:
        break
    x = [0]  # départ (pourquoi 0 ? faut demander à l'auteur original...)
    if n > 0:
        # on ajoute les premiers
        temp1 = raw_input().split()
        for elem in temp1:
            x.append(int(elem))
    if m > 0:
        # ensuite, les seconds
        for val in raw_input().split():
            x.append(int(val))
    x.sort()
    # on va chercher le max des différences
    res = max(x[i+1] - x[i] for i in range(n+m))
    print res  # à l'ancienne