# Bon, je vais essayer d'expliquer au fur et à mesure, je modifie comme je code d'habitude

def pgcd(val1, val2):
    # Calcule le pgcd, classique, on échange tant que c'est pas 0
    x = val1
    y = val2
    while y != 0:
        temp = x
        x = y
        y = temp % y
    return x

def double_frac(u, v):
    # J'ai un doute sur la façon de faire le calcul mais bon...
    return (u * v) // pgcd(u, v)

while True:
    # On prend les entrées, je préfère split() direct mais bon...
    try:
        parts = raw_input().split()
        numbers = list(map(int, parts))
    except Exception as e:
        break # au cas où on a un souci

    if 0 in numbers:
        # on sort si y a un 0
        break

    result_list = [] # Je stocke ici les résultats (il en faudrait trois ?)
    idx = 0
    while idx < 6:
        num = numbers[idx]
        den = numbers[idx + 1]
        value = 1 # pour compter
        nextval = 1
        for p in range(1, den):
            nextval = (nextval * num) % den
            if nextval == 1:
                value = p
                break
        result_list.append(value)
        idx += 2
    # J'espère que la liste a bien trois éléments
    first, second, third = result_list
    # Bon là j'appelle la fonction deux fois imbriquée j'imagine...
    answer = double_frac(double_frac(first, second), third)
    print(answer)