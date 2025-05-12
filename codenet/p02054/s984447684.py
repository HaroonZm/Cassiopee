A,B,C=map(int,input().split())
ANS=0
for i in [A,B,C]:
    if i%2==1:
        ANS+=1
if ANS>=2:
    print("Hom")
else:
    print("Tem")