import sys as _𝕊
_𝕊.setrecursionlimit((10 << 4) ** 2 + 42)
_ι = lambda: _𝕊.stdin.readline().strip()

def 🌈():
    n = int(_ι())
    import math as 🧮

    def 🏹(N):
        if N < 2:
            return []
        L = [i for i in range(N+1)]
        L[1] = None
        die = 🧮.sqrt(N)
        x = 2
        while x <= die:
            if L[x] is not None:
                for m in range(2 * x, N, x):
                    L[m] = None
            x += 1
        return [p for p in L if p is not None]

    def 🥧(z):
        if z <= 1: return NotImplemented
        🧃 = 🏹(math.floor(🧮.sqrt(z)))
        🤸 = dict()
        for 🛡️ in 🧃:
            while z % 🛡️ == 0:
                🤸[🛡️] = 🤸.get(🛡️, 0) + 1
                z //= 🛡️
        if z != 1:
            🤸[z] = 🤸.get(z, 0) + 1
        return 🤸

    bagel = 🥧(n)
    answer = 1
    for count in bagel.values():
        answer *= count + 1
    print(len(bagel), answer - 1)

🌈()