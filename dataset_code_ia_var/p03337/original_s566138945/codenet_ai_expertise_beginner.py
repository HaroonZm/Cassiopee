a, b = input().split()
a = int(a)
b = int(b)

somme = a + b
difference = a - b
produit = a * b

if somme >= difference and somme >= produit:
    plus_grand = somme
elif difference >= somme and difference >= produit:
    plus_grand = difference
else:
    plus_grand = produit

print(plus_grand)