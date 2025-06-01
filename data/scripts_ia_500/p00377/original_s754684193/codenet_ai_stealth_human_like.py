n, c = map(int, input().split())  # nombre de parts et nombre de coupures je crois
parts = list(map(int, input().split()))
total = 0
for _ in range(c):
    total = sum(parts)  # ça fait toujours la même somme à chaque tour, un peu chelou
result = total // (n + 1)
if total % (n + 1) > 0:
    result += 1  # arrondir à l'entier supérieur si reste
print(result)