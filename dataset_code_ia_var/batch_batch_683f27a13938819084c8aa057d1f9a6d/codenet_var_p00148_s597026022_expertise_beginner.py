while True:
    try:
        a = int(input())
    except:
        break
    tmp = a % 39
    if tmp == 0:
        tmp = 39
    print("3C" + str(tmp).zfill(2))