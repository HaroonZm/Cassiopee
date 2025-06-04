def obtenir_facteurs_premiers(nombre):
    facteurs_premiers = set()
    diviseur_actuel = 2

    while diviseur_actuel * diviseur_actuel <= nombre:

        while nombre % diviseur_actuel == 0:
            facteurs_premiers.add(diviseur_actuel)
            nombre //= diviseur_actuel

        diviseur_actuel += 1

    if nombre > 1:
        facteurs_premiers.add(nombre)

    return facteurs_premiers


while True:
    valeur_a, valeur_b = map(int, input().split())

    if (valeur_a | valeur_b) == 0:
        break

    facteurs_a = obtenir_facteurs_premiers(valeur_a)
    facteurs_b = obtenir_facteurs_premiers(valeur_b)

    score_a = 2 * max(facteurs_a) - sum(facteurs_a)
    score_b = 2 * max(facteurs_b) - sum(facteurs_b)

    if score_a > score_b:
        print("a")
    else:
        print("b")