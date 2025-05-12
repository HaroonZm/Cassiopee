while True:
    po=input()
    if po=="0":
        break
    A,B=0,0
    for i in range(1,len(po)):
        if po[i]=="A":
            A+=1
        else :
            B+=1
    if A>B:
        A+=1
    else :
        B+=1
    print(A,B)