while True:
    n = input()
    if n == '0':
        break

    calorieSet = []
    for i in range(int(n)):
        line = input()
        parts = line.split()
        num = int(parts[0])
        protein = int(parts[1])
        lipid = int(parts[2])
        carbohydrate = int(parts[3])
        sumCalorie = protein * 4 + carbohydrate * 4 + lipid * 9
        calorieSet.append((num, protein, lipid, carbohydrate, sumCalorie))

    limit_line = input()
    limit_parts = limit_line.split()
    limit = [int(x) for x in limit_parts]

    good = []
    for item in calorieSet:
        ok = True
        for i in range(1, 5):
            if item[i] > limit[i-1]:
                ok = False
                break
        if ok:
            good.append(item[0])

    if len(good) == 0:
        print("NA")
    else:
        for val in good:
            print(val)