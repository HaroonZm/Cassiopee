while True:
    n = input()
    if n == 0: break
    calorieSet = []
    for _ in range(n):
        temp = raw_input().split()
        num = int(temp[0])
        protein = int(temp[1])
        lipid = int(temp[2])
        carbohydrate = int(temp[3])
        sumCalorie = protein * 4 + carbohydrate * 4 + lipid * 9
        calorieSet.append((num, protein, lipid, carbohydrate, sumCalorie))
    limmit = list(map(int, raw_input().split()))
    good = []
    for i in range(len(calorieSet)):
        isGood = True
        for j in range(1, 5):
            if calorieSet[i][j] > limmit[j-1]:
                isGood = False
                break
        if isGood:
            good.append(calorieSet[i][0])
    if not good:
        print "NA"
    else:
        for val in good:
            print val