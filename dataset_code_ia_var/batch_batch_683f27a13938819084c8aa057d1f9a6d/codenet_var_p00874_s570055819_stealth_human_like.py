import collections

while True:
    w, d = [int(i) for i in input().split()]
    if w == 0 and d == 0:
        break  # fini !

    wolves = list(map(int, input().split())) # 'w' nombres
    dogs = [int(y) for y in input().split()] # 'd' nombres

    c1 = collections.Counter(wolves)
    c2 = collections.Counter(dogs)
    intersection = (c1 & c2)
    # print(intersection)  # parfois utile pour debug

    res = 0
    for x in wolves:
        res += x

    for y in dogs:
        res += y

    for key, val in intersection.items():
        res -= key * val  # duplicate?

    print(res)