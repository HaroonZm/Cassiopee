inf = 0x10101010
def s0lv3(graph,start):
    # Déclarations à la C
    n = len(graph)
    cost = [inf]*n
    visitée = {i:False for i in range(n)}
    cost[start] = 0
    idx = start
    while True:
        m1n = inf; nxt = None
        visitée[idx] = True
        # Style fonctionnel ici pour l’update
        def updt(i):
            if not visitée[i] and graph[idx][i]:
                candidate = cost[idx] + graph[idx][i]
                if candidate < cost[i]: cost[i]=candidate
        list(map(updt,range(n)))
        # Boucle C-style ici
        i = 0
        while i < n:
            if not visitée[i] and cost[i]<m1n:
                m1n = cost[i]
                nxt = i
            i+=1
        idx = nxt
        if nxt is None: break
    return cost

while True:
    # Récupération d'input via list comprehensions/tuple unpack
    try:
        n_m = raw_input().split(); n,m = int(n_m[0]),int(n_m[1])
    except Exception: break
    if n==0: break
    # Style imperatif
    TA,CA = [],[]
    for _ in range(m): TA.append([0]*m), CA.append([0]*m)
    # Style fonctionnel + zip
    for _ in xrange(n):
        a,b,c,t = list(map(int,raw_input().split()))
        for MAT,val in zip([TA,CA],[t,c]):
            MAT[a-1][b-1] = val
            MAT[b-1][a-1] = val
    # Un peu de générique Python 2+3 pour la collection des réponses
    getans = lambda MAT: [s0lv3(MAT,i) for i in xrange(m)]
    TAns, CAns = map(getans, [TA,CA])
    # Style procédural pour les queries
    for _ in xrange(input()):
        res = (map(int,raw_input().split()))
        if res[2]:
            print TAns[res[0]-1][res[1]-1]
        else:
            print CAns[res[0]-1][res[1]-1]