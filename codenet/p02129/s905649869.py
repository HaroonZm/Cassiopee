N = int(input())
SET = [0,0,0,0,0,0]
judge = [[2,1,3],[1,3,2],[3,2,1],[2,3,1],[3,1,2],[1,2,3]]
for _ in range(0,N):
    ID = [1, 2, 3]
    amida = [int(x) for x in input().split()]
    for j in range(1,len(amida)):
        if amida[j] == 0:
            ID[0],ID[1] = ID[1],ID[0]
            #print(ID)
        elif amida[j] == 1:
            ID[1],ID[2] = ID[2],ID[1]
            #print(ID)

    for i in range(0,len(judge)):
        if ID == judge[i]:
            SET[i] += 1

#print(SET)

if ((SET[5] > 0) or (SET[0] > 1) or (SET[1] > 1) or (SET[2] > 1) or
        ((SET[0] > 0) and (SET[1] > 0) and (SET[4] > 0)) or
        ((SET[0] > 0) and (SET[2] > 0) and (SET[4] > 0)) or
        ((SET[0] > 0) and (SET[2] > 0) and (SET[4] > 0)) or
        ((SET[0] > 0) and (SET[1] > 0) and (SET[3] > 0)) or
        ((SET[0] > 0) and (SET[2] > 0) and (SET[3] > 0)) or
        ((SET[1] > 0) and (SET[2] > 0) and (SET[4] > 0)) or
        ((SET[3] > 0) and (SET[4] > 0)) or
        (SET[3] > 2) or (SET[4] > 2)):
    print("yes")
else:
    print("no")