while True:
    n = input()
    if n == 0:
        break
    calorieSet = []
    for _ in range(n):
        num, protein, lipid, carbohydrate = map(int, input().split())
        sumCalorie = protein * 4 + carbohydrate * 4 + lipid * 9
        calorieSet.append((num, protein, lipid, carbohydrate, sumCalorie))
    limit = list(map(int, input().split()))
    good = []
    for var in calorieSet:
        judge = True
        for cal, lim in zip(var[1:], limit):
            if cal > lim:
                judge = False
                break
        if judge:
            good.append(var[0])
    if not good:
        print("NA")
    else:
        for var in good:
            print(var)