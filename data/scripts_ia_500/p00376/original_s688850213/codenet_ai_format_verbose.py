premier_nombre, deuxieme_nombre = map(int, input().split())

if premier_nombre < deuxieme_nombre:
    
    difference = deuxieme_nombre - premier_nombre
    print(difference)

if premier_nombre > deuxieme_nombre:
    
    difference = premier_nombre - deuxieme_nombre
    print(difference)

if premier_nombre == deuxieme_nombre:
    
    print('0')