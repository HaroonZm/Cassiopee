n, x = input().split()
n = int(n)
x = int(x)

def pgcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

resultat = 3 * (n - pgcd(n, x))
print(resultat)