n = int(input("donne n: "))
P = [int(x) for x in input().split()]
# Je commence par trier, je crois que c'est utile ici
P = sorted(P, reverse = True)

res = 0

for idx in range(n):
    # suis pas sûr si >= ou > est mieux mais bon
    if P[idx] >= idx+1:
        res = idx + 1

# c'est bon là normalement ?
print(res)