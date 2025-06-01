i, j, k, l = 0, 0, 0, 0
while True:
    listTRI = [int(x) for x in input().split()]
    if min(listTRI) <= 0:
        break
    sumList = sum(listTRI)
    if sumList - max(listTRI) <= max(listTRI):
        break
    maxIND = 0
    maxVal = listTRI[0]
    if listTRI[1] > maxVal:
        maxIND = 1
        maxVal = listTRI[1]
    if listTRI[2] > maxVal:
        maxIND = 2
        maxVal = listTRI[2]
    s = 0
    for v in listTRI:
        s += v*v
    cos1 = s - maxVal * maxVal * 2
    cos2 = sumList * 2 - maxVal * 2
    cosTRI = cos1 / cos2
    i += 1
    if cosTRI < 0:
        l += 1
    elif cosTRI > 0:
        k += 1
    else:
        j += 1
print(i, j, k, l)