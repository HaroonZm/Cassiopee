n = int(input())
resultat = 0
b = 1
while b < n:
    resultat = resultat + ((n - 1) // b)
    b = b + 1
print(resultat)