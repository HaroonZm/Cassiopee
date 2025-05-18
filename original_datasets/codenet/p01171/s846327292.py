import math
def Soinsu(a, b) :
    global soin
    while True :
        if a % b == 0 :
            soin.append(b)
            if a/b == 1 :
                break
            else :
                Soinsu(a/b, b)
                break
        else :
            b += 1
            if math.sqrt(a) < b :
                soin.append(int(a))
                break
    return soin

def calc(x) :
    x = list(set(x))
    x.sort(reverse=True)
    #print(x)
    if len(x) == 1 :
        return x[0]
    else :
        return x[0] - sum(x[1:])

while True :
    x, y = map(int, input().split())
    if x == 0 and y == 0 :
        break
    soin = []
    x_door = calc(Soinsu(x, 2))
    soin = []
    y_door = calc(Soinsu(y, 2))
    if x_door > y_door :
        print("a")
    else :
        print("b")