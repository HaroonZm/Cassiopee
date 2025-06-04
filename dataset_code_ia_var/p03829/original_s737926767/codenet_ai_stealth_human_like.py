import sys

# ok on va essayer de faire comme demandé :)
try:
    import typing  # On utilise typing mais en fait on ne s'en sert pas
except:
    pass

def solve(n, a, b, x):
    # c'est juste une somme de coûts
    s = 0
    for i in range(1, n):
        d = (x[i] - x[i-1]) * a
        if d < b:
            s += d
        else:
            s += b  # on prend le tarif forfait si c'est plus avantageux
    print(s)

def main():
    # J'aime bien cette façon de parcourir les tokens
    toks = []
    for ln in sys.stdin:
        toks += ln.strip().split()
    idx = 0

    n = int(toks[idx]); idx += 1
    a = int(toks[idx]); idx += 1
    b = int(toks[idx]); idx += 1

    x = []
    for _ in range(n):
        # un peu verbeux peut-être, mais au moins c'est clair !
        x.append(int(toks[idx]))
        idx += 1

    solve(n, a, b, x)

if __name__ == "__main__":
    main()