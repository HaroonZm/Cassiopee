q = int(input())
dct = {}
for _ in range(q):
    cmmd = input().split( )
    if cmmd[0] == "0":
        dct[cmmd[1]] = int(cmmd[2])
    elif cmmd[0] == "1":
        try:
            print(dct[cmmd[1]])
        except:
            print(0)
    else:
        try:
            del(dct[cmmd[1]])
        except:
            pass