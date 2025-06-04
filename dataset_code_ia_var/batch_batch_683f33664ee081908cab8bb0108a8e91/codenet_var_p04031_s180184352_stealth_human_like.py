n = int(input())
arr = list(map(int, input().split()))

# Calcul de la moyenne (peut-être arrondi?)
# Peut-être que round c'est trop, mais bon
avg = round(sum(arr) / n)

# Petite variable pour la somme
result = 0
for x in arr:
    tmp = (x - avg) ** 2
    result = result + tmp  # (Je pourrais utiliser += mais bon)

print(result)  # Voilà, c'est tout je crois