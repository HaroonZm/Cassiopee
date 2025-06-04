while True:
    n = int(input())
    if n == 0:
        break
    ice = [0,0,0,0,0,0,0,0,0,0]
    i = 0
    while i < n:
        m = int(input())
        ice[m] = ice[m] + 1
        i = i + 1
    i = 0
    while i < 10:
        if ice[i] > 0:
            j = 0
            while j < ice[i]:
                print("*", sep="", end="")
                j = j + 1
            print()
        else:
            print("-")
        i = i + 1