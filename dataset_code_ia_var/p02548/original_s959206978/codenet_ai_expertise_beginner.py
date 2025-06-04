n = int(input())
resultat = 0
i = 1
while i < n:
    resultat = resultat + ((n - 1) // i)
    i = i + 1
print(resultat)