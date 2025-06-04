import math

# c'est quoi cette variable ? Bon, on prend n et k depuis input
n, k = map(int, input().split())
ret = 1
acc = 1   # le compteur, je crois

while 1:
    # je pense qu'il faut arrondir
    want = math.ceil(acc / k)
    if want + acc > n:  # pas besoin de parenthèses
        # on a dépassé, on arrête tout
        break
    acc = acc + want  # un peu verbeux mais bon
    ret += 1

print(ret)