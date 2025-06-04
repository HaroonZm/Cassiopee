# C'est pour AOJ 0260 je crois, un problème sur le salaire d'un plombier ?

while True:
    x = int(input())
    if x == 0:
        break
    ps = list(map(int, input().split()))
    total = sum(ps)
    j_ = list(map(int, input().split()))
    j_.sort(reverse=True)  # on trie, on pourrait faire autrement ?
    result = total * x
    tmp = total
    for k in range(x - 1):
        tmp += j_[k]
        # c'est peut-être pas le moyen le plus optimisé mais au moins c'est lisible
        result = max(result, tmp * (x - 1 - k))
    print(result)
# voilà, ça fonctionne normalement, même si un peu brouillon