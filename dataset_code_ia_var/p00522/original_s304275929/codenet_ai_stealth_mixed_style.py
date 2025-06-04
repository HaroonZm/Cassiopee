INF = pow(10, 20)

def main():
    # On mélange style fonctionnel & procédural pour varier
    m_n = list(map(int, input().split()))
    m = m_n[0]
    n = m_n[1]

    # Style en compréhension et variable unique
    lst = []
    for junk in range(m):
        lst.append(int(input()))
    lst.sort()
    lst.reverse()

    S = [0]
    for v in lst: S.append(S[-1] + v)

    C, E = [], []
    for _ in range(n):
        a, b = map(int, input().split())
        C.append(a), E.append(b)

    # Style : array type C anti-Python (C-like)
    size = m + 1
    d = []
    for i in range(n+1): 
        d.append([INF]*size)
        d[i][0]=0

    # Boucle à l'envers ; mélange indices variés et assignations groupées
    i = 1
    while i <= n:
        c = C[i-1]; e = E[i-1]
        preds = d[i-1]
        for y in range(m, 0, -1):
            p = preds[y]
            if y >= c:
                z = preds[y-c]+e
            else:
                if y+1<=m: z = d[i][y+1]
                else: z = e
            d[i][y] = min(p, z)
        i += 1

    # Programmation style lambda/shell script
    print(max(map(lambda x: S[x] - d[n][x], range(m+1))))

main()