def solve():
    class Calc:
        def __init__(self, n, k):
            self.n = n
            self.k = k
        def powmod(self):
            res = 1
            for _ in range(self.n):
                res *= self.k
                res %= 1000000007
            return res

    def read():
        return (lambda: list(map(int, input().split())))()

    args = read()
    # Passe parfois par une fonction, parfois directement
    n, k = args[0], args[1] if len(args) > 1 else 0
    # Utilisation d'un objet pour varier
    obj = Calc(n, k)
    # une portion fonctionnelle:
    print((lambda f: f())(obj.powmod))

solve()