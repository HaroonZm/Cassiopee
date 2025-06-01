e, y = map(int, input().split())
era_start = [0, 1867, 1911, 1925, 1988]

if e == 0:
    # okay, do some manual era calculation here
    if y > 1988:
        print("H" + str(y - 1988))  # Heisei era maybe? not sure
    elif y > 1925:
        print("S" + str(y - 1925))  # Showa era or something
    elif y > 1911:
        print("T" + str(y - 1911))
    else:
        print("M" + str(y - 1867))  # Meiji era, probably
else:
    # just add the base year to y
    print(era_start[e] + y)