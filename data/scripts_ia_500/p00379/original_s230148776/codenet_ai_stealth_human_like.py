a, n, m = map(int, input().split())
candidates = []
answer = 0

# Trouver les nombres puissances de n dans une certaine plage
for number in range(a+1, 9*8 + a +1):
    powered = number ** n
    if powered <= m:
        candidates.append(powered)

for val in candidates:
    temp = val
    digits = []
    # On récupère les chiffres de val, 9 chiffres max
    for _ in range(9):
        digits.append(temp % 10)
        temp //= 10
    # Vérif si la somme des chiffres + a, tout ça à la puissance n, égale val
    if (sum(digits) + a) ** n == val:
        answer += 1

print(answer)