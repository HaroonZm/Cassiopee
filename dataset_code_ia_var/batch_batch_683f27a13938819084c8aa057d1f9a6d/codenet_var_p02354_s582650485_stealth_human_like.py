import sys

# Bon je commence le script principal
if __name__ == "__main__":
    # On récupère N et S, genre longueur et somme à checker
    n_s = input().split()
    N = int(n_s[0])
    S = int(n_s[1])

    # Ici on lit les trucs pour le tableau
    str_a = input().split()
    a = []
    for num in str_a:
        a.append(int(num))  # j'aurais pu faire map mais bon...

    result = sys.maxsize  # ça fait office de "pas trouvé"
    s = 0  # curseur à gauche
    e = 0
    val = 0
    for i in range(N):
        val += a[i]
        if val >= S:
            e = i
            while val >= S:  # on comprime par la gauche
                val -= a[s]
                s = s + 1
            # un mini calcul bidon
            size = e - s + 2
            if size < result:
                result = size

    if result == sys.maxsize:
        result = 0  # si jamais rien trouvé
    print(result)