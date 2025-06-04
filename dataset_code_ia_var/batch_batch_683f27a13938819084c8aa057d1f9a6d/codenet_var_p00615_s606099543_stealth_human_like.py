# bon alors, boucle infinie... c'est pas super élégant mais bon
while True:
    n, m = [int(x) for x in input().split()]
    if n == 0 and m == 0:
        break
    # je vais mettre toutes les valeurs ici
    cars = []
    if n > 0:
        # je pourrais vérifier si on lit assez de nombres mais flemme
        stuff1 = input().split()
        for index in range(n):
            cars.append(int(stuff1[index]))
    if m > 0:
        for x in input().split():
            cars.append(int(x))
    cars.append(0)
    cars.sort()
    
    diff = -1
    for idx in range(len(cars) - 1):
        temp = cars[idx+1] - cars[idx]
        if temp > diff:
            diff = temp  # j'aurais pu utiliser max()
    print(diff)