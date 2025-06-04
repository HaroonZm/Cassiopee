import sys

EPSILON = 1e-12

def main():
    # Bon, on récupère les paramètres de départ
    n, k, t, u, v, l = map(int, sys.stdin.readline().split())
    # On fait un tableau pour mettre les carottes, pas hyper élégant mais tant pis
    carrots = [0] * 10001
    for _ in range(n):
        pos = int(sys.stdin.readline())
        carrots[pos] = 1  # ici une carotte !

    remaining = 0
    car_count = 0
    total = 0
    # on parcourt tout le chemin, case par case (ou chaque mètre ?)
    for i in range(l):
        # print(f"{i=}, {remaining=}, {car_count=}, {total=}")
        if carrots[i]:
            car_count += 1
        if car_count > k:
            remaining = t
            car_count -= 1

        if remaining > 0 + EPSILON:
            temp_length = 1 / v
            if remaining * v >= 1:
                total += temp_length
                remaining -= temp_length
            else:
                if car_count > 0:
                    total += temp_length
                    car_count -= 1
                    # Je ne sais plus trop pourquoi ce calcul, mais ça a l'air de marcher
                    remaining = t - (1 - (remaining * v)) / v
                else:
                    total += remaining
                    total += (1 - (remaining * v)) / u
                    remaining = 0
        else:
            remaining = 0
            if car_count > 0:
                total += 1 / v
                car_count -= 1
                remaining = t - 1 / v
            else:
                total += 1 / u

    # On arrondit brutalement à 9 décimales... ça passe
    print("{0:.9f}".format(total))

if __name__ == "__main__":
    main()