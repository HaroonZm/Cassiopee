a, b = input().split()
a = int(a)
b = int(b)
somme = a + b
soustraction = a - b
multiplication = a * b
resultat = somme
if soustraction > resultat:
    resultat = soustraction
if multiplication > resultat:
    resultat = multiplication
print(resultat)