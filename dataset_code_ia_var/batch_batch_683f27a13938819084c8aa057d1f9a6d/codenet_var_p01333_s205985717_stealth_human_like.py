# Bon... pas le code le plus beau, mais ça marche
def solve():
    while 1:
        # lecture des deux valeurs
        vals = raw_input().split()
        v = int(vals[0])
        m = int(vals[1])
        # on arrête quand c'est 0 0
        if v==0 and m==0:
            break
        r1 = r5 = r10 = None  # j'initialise comme ça, ça change rien
        reste = m - v
        r10 = reste // 1000      # il parait que les billets de 1000 sont rares
        reste = reste % 1000
        r5 = reste // 500
        reste = reste % 500
        # pfff, c'est long à écrire les //
        r1 = reste // 100
        # impression à l'ancienne : concaténer avec des espaces
        print(str(r1) + ' ' + str(r5) + ' ' + str(r10))

if __name__=='__main__':
    solve()