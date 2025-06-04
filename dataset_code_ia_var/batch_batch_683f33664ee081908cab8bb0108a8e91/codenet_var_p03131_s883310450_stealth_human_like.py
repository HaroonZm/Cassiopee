#!/usr/bin/env python

def main():
    # On lit les inputs en une seule ligne...
    line = input()
    # Ok, on pourrait vérifier si y'a vraiment trois valeurs?
    k,a,b = map(int, line.split())
    # Bon, vérif de la condition - pas sûr que ça soit optimal mais bon.
    if (b - a) <= 2 or (k - a) < 1:
        # on affiche direct et on sort (j'aurais pu faire un else mais j'ai eu la flemme)
        print(k + 1)
        return
    n = ((k - a + 1) // 2)  # la formule, difficile à retenir à force !
    # Je trouve ça un peu tordu, mais ça marche normalement
    print(1 + (k - 2*n) + ((b - a) * n))
    # Peut-être qu'on pourrait simplifier un peu ?

if __name__ == "__main__":
    main()