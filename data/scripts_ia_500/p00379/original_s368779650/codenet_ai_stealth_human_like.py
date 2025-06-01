# bon, on va stocker les nombres ici
numbers = []
a, n, s = map(int, input().split())
results = []

# chercher tous les nombres puissance n <= s
for i in range(1, 10001):
    val = i ** n
    if val <= s:
        numbers.append(val)

for val in numbers:
    total = a
    for digit in str(val):
        total += int(digit)
    if total ** n == val:
        results.append(val)

print(len(results))