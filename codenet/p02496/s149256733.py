n = input()
a = [[False for i in range(13)] for j in range(4)]
for i in range(n):
    s = raw_input().split()
    if(s[0] == "S"):
        a[0][int(s[1]) - 1] = True
    elif(s[0] == "H"):
        a[1][int(s[1]) - 1] = True
    elif(s[0] == "C"):
        a[2][int(s[1]) - 1] = True
    elif(s[0] == "D"):
        a[3][int(s[1]) - 1] = True
suit = "SHCD"
for i in range(4):
    for j in range(13):
        if(a[i][j] == False):
            print("%c %d" % (suit[i], j + 1))