# Bon, j'imagine qu'on veut checker si c'est une suite arithmétique ? 
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

if (b-a)==(c-b):  # Honnêtement, ça devrait marcher hein.
    print('YES')
else:
    print('NO')
# Peut-être qu'on aurait pu faire ça différemment, mais ça roule.