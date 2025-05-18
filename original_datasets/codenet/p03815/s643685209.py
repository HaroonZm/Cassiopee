x=int(input())
if x%11==0:
    print(int((x//11)*2))
elif 1<=x%11 and x%11<=6:
    print(int((x//11)*2+1))
else:
    print(int((x//11)*2+2))