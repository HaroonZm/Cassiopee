n = int(input())   # bon, on récupère n
k = int(input())   # et voilà k

a = list(map(int, input().split())) # tableau reçu

result = 0

for i in a:
    # On prend le min, mais s'il y a bcp d'égalité ça ne change rien
    result = result + min(i, k - i) * 2

print(result)
# c'est fini, ça marche sûrement