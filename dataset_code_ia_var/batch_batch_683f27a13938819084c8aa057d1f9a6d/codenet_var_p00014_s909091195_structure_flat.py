j = 0
while j < 20:
    try:
        d = int(input())
        size = 0
        i = 0
        while i < (600 // d - 1):
            i2 = i + 1
            size += ( (i2 * d) ** 2 ) * d
            i += 1
        print(int(size))
        j += 1
    except:
        break