while True:
    nombre_entrees = eval(input())
    if nombre_entrees == 0:
        break
    valeurs_entrees = input().split()
    somme_valeurs = sum([eval(valeur) for valeur in valeurs_entrees])
    moyenne_internes = int(somme_valeurs / (nombre_entrees - 1))
    print(moyenne_internes)