h,w=map(int,input().split())

a=[]
for _ in range(h):
    a+=list(input())

four=(h//2)*(w//2)
two=h%2*w//2+w%2*h//2
one=(h%2)*(w%2)

import collections
c = collections.Counter(a)

#print(four,two,one)
d=list(c.values())
d.sort()

for item in d:
    if item==1:
        if one==1:
            one-=1
        else:
            print("No")
            exit()
    elif item==2:
        if two>0:
            two-=1
        else:
            print("No")
            exit()
    elif item==3:
        if one==1 and two>0:
            one-=1
            two-=1
        else:
            print("No")
            exit()
    else:
        if item%2==1:
            if one==0:
                print("No")
                exit()
            else:
                item-=1
                one-=1
        #print(item,four,two,one)
        while item>=4 and four>0:
            item-=4
            four-=1
        #print(item,four,two,one)
        
        while item>=2:
            item-=2
            two-=1
        #print(item,four,two,one)
    
if one==0 and two==0 and four==0:
    print("Yes")
else:
    print("No")