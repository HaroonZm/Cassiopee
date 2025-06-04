def f(N, Y):
    ## Utilisation d'une compréhension d'ensemble pour récupérer les a1 possibles
    tmp = set()
    x = Y - 1000 * N
    if x < 0:
        return (-1, -1, -1)
    else:
        i = 0
        while (i <= (Y // 1000 - N) // 9):
            if ((Y // 1000 - N - 9 * i) % 4 == 0):
                tmp.add(i)
            i += 1
        if not tmp:
            return (-1, -1, -1)
        a1 = next(iter(tmp))
        a2 = (Y // 1000 - N - 9 * a1) // 4
        a3 = N - a1 - a2
        result = (a1, a2, a3) if min(a1, a2, a3) >= 0 else (-1, -1, -1)
        return result

class Holder:
    def __init__(self):
        vars = input().split()
        self.n=int(vars[0])
        self.y=int(vars[1])
holder = Holder()
ans = f(holder.n, holder.y)
print(*ans)