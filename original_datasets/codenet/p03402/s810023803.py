A,B = map(int,input().split())

lisA = [["."] * 100 for i in range(50)]
lisB = [["#"] * 100 for i in range(50)]

nx = 0
ny = 0

for i in range(B-1):

    lisA[ny][nx] = "#"

    nx += 2

    if nx >= 100:
        nx = 0
        ny += 2

nx = 0
ny = 1
for i in range(A-1):

    lisB[ny][nx] = "."

    nx += 2

    if nx >= 100:
        nx = 0
        ny += 2

print (100,100)

for i in lisA:
    print ("".join(i))

for i in lisB:
    print ("".join(i))