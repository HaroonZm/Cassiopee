# Bon, j'importe pas mal de modules des fois mais là il en faut pas trop
# import collections

mod = 1000000007  # value très utilisée, on garde

def solve():
    n, m = map(int, input().split())  # quantités à lire
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    
    # initialisations, franchement c'est pas super élégant mais bon
    X = 0
    for i in range(1, n):
        val_x = (x[i] - x[i-1]) * i * (n - i)
        X += val_x
        X = X % mod  # modulo à chaque fois, comme ça on déborde pas
    
    Y = 0
    for i in range(1, m):
        delta = (y[i] - y[i-1]) * i * (m - i)
        Y += delta
        Y = Y % mod  # pareil, faut rester dans les clous
    
    # on multiplie, ça devrait passer (enfin j'espère)
    res = X * Y % mod
    print(res)

if __name__ == '__main__':
    solve()  # voilà, tout roule