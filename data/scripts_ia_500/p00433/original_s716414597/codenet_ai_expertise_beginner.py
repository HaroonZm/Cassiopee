valeurs1 = input()
valeurs2 = input()

liste1 = valeurs1.split()
liste2 = valeurs2.split()

a = int(liste1[0])
b = int(liste1[1])
c = int(liste1[2])
d = int(liste1[3])

x = int(liste2[0])
y = int(liste2[1])
z = int(liste2[2])
w = int(liste2[3])

A = a + b + c + d
B = x + y + z + w

if A > B:
    print(A)
else:
    print(B)