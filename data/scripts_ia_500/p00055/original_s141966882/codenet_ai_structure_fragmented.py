def lire_valeur():
    try:
        return float(input())
    except:
        return None

def calculer_tmp(a, i):
    return (a / 3) * (i % 2) + (a * 2) * (i % 2 == 0)

def mise_a_jour_total(total, tmp):
    return total + tmp

def boucle_calculs(a):
    total = a
    for i in range(2, 11):
        tmp = calculer_tmp(a, i)
        total = mise_a_jour_total(total, tmp)
        a = tmp
    return total

def process():
    while True:
        a = lire_valeur()
        if a is None:
            break
        total = boucle_calculs(a)
        print(total)

process()