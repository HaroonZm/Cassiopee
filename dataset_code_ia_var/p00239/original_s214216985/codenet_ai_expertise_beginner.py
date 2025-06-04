while True:
    n = input()
    if n == '0':
        break

    calorie_list = []
    for i in range(int(n)):
        line = input().split()
        num = int(line[0])
        protein = int(line[1])
        lipid = int(line[2])
        carbohydrate = int(line[3])
        total = protein * 4 + carbohydrate * 4 + lipid * 9
        calorie_list.append([num, protein, lipid, carbohydrate, total])

    limit = list(map(int, input().split()))
    valid = []
    for item in calorie_list:
        ok = True
        for value, lim in zip(item[1:], limit):
            if value > lim:
                ok = False
                break
        if ok:
            valid.append(item[0])

    if len(valid) == 0:
        print("NA")
    else:
        for v in valid:
            print(v)