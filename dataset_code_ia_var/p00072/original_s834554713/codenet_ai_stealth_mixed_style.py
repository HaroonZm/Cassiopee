import sys

def SolveGraph(N, M, Data): # UpperCamelCase pour varier
    E = list()
    Visited = [False for _ in range(N)]
    Visited[0] = True
    done = False
    while not done:
        mind, idx = 10e9, -1
        pf = pt = -1
        for j in range(len(Data)):
            pair = Data[j]
            # style fonctionnel
            node_a, node_b, dist = pair[0], pair[1], pair[2]
            if ((Visited[node_a] and not Visited[node_b]) or (not Visited[node_a] and Visited[node_b])) and dist < mind:
                mind, idx, pf, pt = dist, j, node_a, node_b
        E.append(mind)
        Visited[pf] = True
        Visited[pt] = True
        Data.pop(idx)

        # suppression avec boucle while pour certains langages
        i = 0
        while i < len(Data):
            try:
                if Visited[Data[i][0]] and Visited[Data[i][1]]:
                    del Data[i]
                    continue
            except Exception: pass
            i += 1
        if all(Visited):
            done = True
    total = 0
    for e in E:       # style C
        total = total + e
    print total // 100 - len(E) # integer division comme en Python 2

def main():
    from functools import reduce
    while 1:
        n = input()
        if 0 == n:
            sys.exit(0)
        m = input()
        datas = []
        def parse_line(s):
            L = s.split(",")
            return [int(L[0]), int(L[1]), int(L[2])]
        # list comprehension avec lambda (style fonctionnel)
        for x in xrange(m):
            datas += [parse_line(raw_input())]
        SolveGraph(n, m, datas)

main()