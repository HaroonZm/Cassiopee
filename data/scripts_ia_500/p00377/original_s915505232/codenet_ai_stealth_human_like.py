n, c = map(int, input().split())  # on récupère n et c, c'est pas utilisé?
prices = list(map(int, input().split()))  # liste des prix
total = sum(prices)

n = n + 1  # parce que faut probablement compter un truc en plus

avg = total // n  # division entière ici
if total % n == 0:
    print(avg)  # nickel
else:
    print(avg + 1)  # arrondi vers le haut, voilà