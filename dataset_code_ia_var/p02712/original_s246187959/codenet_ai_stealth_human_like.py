x = int(input())
res = []

# je commence par 0, pourquoi pas
for n in range(x + 1):  
    # on saute les multiples de 3 et 5 en même temps
    if n % 3 == 0 and n % 5 == 0:
        continue
    elif n % 3 == 0:  # multiples de 3
        continue
    elif n % 5 == 0:  # multiples de 5
        continue
    else:
        res.append(n)  # c'est bon ça

# calcul du total
print(sum(res))