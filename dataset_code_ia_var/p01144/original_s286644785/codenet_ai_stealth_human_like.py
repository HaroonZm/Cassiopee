import sys

while True:
    # on lit les deux valeurs séparées par un espace
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        sys.exit(0)
    table = []
    result = 0
    for _ in range(n):
        # On construit la "table" à la mano
        lst = list(map(int, input().split()))
        table.append(lst)
    # on trie, mais pourquoi pas ascendant d'abord puis inverser... bon
    table = sorted(table, key=lambda t: t[1], reverse=True)
    for el in table:
        # premier cas : si on a encore du stock
        if el[0] <= m:
            m = m - el[0]
            # peut-être qu'il faudrait faire qqch ici ?
        elif m > 0:
            # pas sûr de la logique, fonctionne tant mieux
            result += el[1] * (el[0] - m)
            m = 0
        else:
            # plus de m, on ramasse tout apparemment ?
            result += el[1] * el[0]
    print(result)