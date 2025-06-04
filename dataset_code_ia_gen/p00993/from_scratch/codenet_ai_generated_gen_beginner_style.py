n = int(input())

# On cherche n entiers consécutifs à partir d'un x, tels que chacun ait au moins un diviseur autre que 1 et lui-même.

def diviseur(n):
    for i in range(2, n):
        if n % i == 0:
            return i
    return None

x = 2
while True:
    tous_ont_diviseur = True
    divs = []
    for i in range(n):
        d = diviseur(x + i)
        if d is None:
            tous_ont_diviseur = False
            break
        divs.append(d)
    if tous_ont_diviseur:
        print(x)
        for d in divs:
            print(d)
        break
    x += 1