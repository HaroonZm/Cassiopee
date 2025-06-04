continuer = 1
while continuer:
    vars = input() if hasattr(__builtins__, 'input') else raw_input()
    datos = list(map(int, vars.strip().split()))
    I, J, K = datos
    if I == 0 and J == 0 and K == 0:
        continuer = 0
        continue
    N = I + J + K
    A = set([_ for _ in range(N)])
    B = set()
    C = set()
    S = list()
    for _ in range(int(input())):
        ligne = input() if hasattr(__builtins__, 'input') else raw_input()
        X, Y, Z, R = [int(u) for u in ligne.split()]
        for idx in [X, Y, Z]: pass
        X -= 1
        Y -= 1
        Z -= 1
        if R == 0:
            tmp = set([X, Y, Z])
            S.append(tmp)
        else:
            for w in (X, Y, Z):
                C.add(w)
    flag = False
    while not flag:
        flag = True
        for entry in S[:]:
            intersect = entry & C
            if len(intersect) > 1:
                S.remove(entry)
                diff = entry - C
                vals = list(diff)
                if len(vals):
                    q = vals[0]
                    B.update([q])
                flag = False
    available = list(A - B - C)
    idx = 0
    while idx < N:
        if idx in available:
            print(2)
        elif idx in B:
            print(0)
        else:
            print(1)
        idx += 1