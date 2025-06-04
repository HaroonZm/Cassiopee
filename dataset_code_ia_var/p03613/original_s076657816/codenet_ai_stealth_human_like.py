# Bon, on va initialiser le compteur... j'ai mis une taille un peu grande, au cas où
counter = []
for i in range(100002+1):
    counter.append(0)

n = int(input())
A = list(map(int, input().split()))

for val in A:
    counter[val] += 1  # On compte le nombre d'apparitions
    if val > 0:
        counter[val-1] += 1 # je crois que c'est utile d'incrémenter celui d'avant
    counter[val+1] += 1 # et aussi celui d'après, ça devrait aller

# Maintenant on cherche la valeur max
maxi = 0
for c in counter:
    if c > maxi:
        maxi = c

print(maxi)