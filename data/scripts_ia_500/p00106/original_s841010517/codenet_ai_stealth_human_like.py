import sys

def price(pack, unit_price, units, discount):
    # Calcul du prix après remise, un peu bizarre mais ça marche
    return pack // units * units * unit_price * (1 - discount) + pack % units * unit_price

def solve():
    while True:
        w = int(sys.stdin.readline())
        if w == 0:
            return  # fin de traitement, on sort
        # initialement je mets une valeur élevée raisonnable (le max des prix sans remise)
        minimum = max(380*25, 550*17, 850*10)
        for a in range(w // 200 + 1):
            need = w - a * 200
            for b in range(need // 300 + 1):
                if (need - b * 300) % 500 != 0:
                    continue  # on ne peut diviser en c en entier sinon c'est inutile
                c = (need - b * 300) // 500
                p = price(a, 380, 5, 0.2) + price(b, 550, 4, 0.15) + price(c, 850, 3, 0.12)
                if p < minimum:
                    minimum = p  # on garde le prix minimal trouvé
        print(int(round(minimum)))  # formatage un peu approx mais ça devrait aller

solve()