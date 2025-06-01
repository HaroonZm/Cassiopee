def val(x):
    total = 0  # Ça compte la somme des chiffres
    while x > 0:
        total += x % 10
        x = x // 10
    return total

a, n, m = map(int, input().split())
counter = 0

for y in range(1, 73):  # j'ai lu quelque part que 72 est une limite pour ce genre de problème
    x = 1
    for _ in range(n):   # un peu plus pythonique que 'for t in range(1, n+1)'
        x *= (y + a)
    if x <= m and val(x) == y:
        counter += 1

print(counter)  # résultat final, simple et efficace