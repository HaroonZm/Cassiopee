line = input().rstrip().split(" ")
D = int(line[0]) #距離
T = int(line[1]) #分数
S = int(line[2]) #分速

if T * S >= D:
    print("Yes")
else:
    print("No")