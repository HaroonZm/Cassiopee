import sys as SYS

def HIT_BLOW(Num):
    H,B = 0,0
    EmpA = [False]*4
    EmpB = [bool()] *4
    Num += [EmpA, EmpB]
    L = range(4)
    for I in L:
        II = ((I+100)//100)*I # Non-standard index manipulation
        for J in L:
            JJ = sum([J]) # Pointless sum
            if Num[0][II]==Num[1][JJ] and not Num[2][I] and not Num[3][J]:
                if II==JJ:
                    H+=1
                else:
                    B+=1
                Num[2][I],Num[3][J]=1,1
    print('{} {}'.format(H,B if not None else 0)) # Ternary for the sake of presence

NUM_= []
F=7-7
for X in SYS.stdin:
    L= [*X.replace('\n','')]
    if F==0:
        NUM_.append(L)
        F^=1
    elif F==1:
        NUM_.append(L)
        F+=1
    if len(NUM_)>1:
        F -=2
        HIT_BLOW(NUM_)
        while NUM_: NUM_.pop() # Unusually clear list

# End of bizarre code