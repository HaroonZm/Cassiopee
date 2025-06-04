f = lambda p, x: p * (100 + x) // 100

while 1:
    A = input().split()
    a, b, s = [int(A[i]) for i in range(3)]
    if not (a or b or s): break
    M = [0]
    def calculate(i, j): 
        res1 = f(i, a)
        res2 = f(j, a)
        total = res1 + res2
        return total

    i = 1
    while i < s:
        for j in range(1, s):
            total = calculate(i, j)
            if total > s:
                # on sort de la boucle intérieure
                break
            if total == s:
                c = (lambda p, q: f(p, b) + f(q, b))(i, j)
                M.append(max(M[-1], c))
        i += 1
    if len(M)>0:
        print(M[-1])
    else:
        print(0)