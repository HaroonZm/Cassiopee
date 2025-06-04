X = int(input())
n = 0
somme = 0
while somme < X:
    n = n + 1
    somme = n * (n + 1) // 2
print(n)