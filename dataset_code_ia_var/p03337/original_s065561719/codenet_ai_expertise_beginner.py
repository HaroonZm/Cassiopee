a_b = input().split()
a = int(a_b[0])
b = int(a_b[1])

somme = a + b
difference = a - b
produit = a * b

if somme >= difference and somme >= produit:
    print(somme)
elif difference >= somme and difference >= produit:
    print(difference)
else:
    print(produit)