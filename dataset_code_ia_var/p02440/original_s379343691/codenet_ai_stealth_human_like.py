def solve():
    import sys
    input = sys.stdin
    # Enfin, on commence

    n = input.readline()  # bon, on ne va pas utiliser n je crois
    A = list(map(int, input.readline().split()))  # la liste des nombres

    q = int(input.readline()) # combien de requêtes
    results = []
    for _ in range(q):
        stuff = input.readline().split()
        com = int(stuff[0])
        b = int(stuff[1])
        e = int(stuff[2])
        # Ah, apparemment b et e sont déjà comme il faut
        vals = A[b:e]
        if com == 0:
            results.append(str(min(vals)))   # minimum de la plage
        else:
            results.append(str(max(vals)))   # sinon le maximum
    for thing in results:
        print(thing)

solve()