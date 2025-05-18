def HB(A,B):
    hit=0
    blow=0
    for i in range(4):
        for j in range(4):
            if A[i]==B[j]:
                if i==j:
                    hit+=1
                else:
                    blow+=1
    return [hit,blow]
while True:
    try:
        A=input().split()
        B=input().split()
        print(HB(A,B)[0] , HB(A,B)[1] )
    except:
        break