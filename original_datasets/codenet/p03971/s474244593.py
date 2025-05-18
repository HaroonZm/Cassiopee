n,a,b=map(int,input().split())
s=input()
cnt=0
cntfo=0
for i in range(n):
    if s[i]=="a":
        if cnt<a+b:
            print("Yes")
            cnt+=1
        else:
            print("No")
    elif s[i]=="b":
        if cnt<a+b and cntfo<b:
            print("Yes")
            cnt+=1
            cntfo+=1
        else:
            print("No")
    else:
        print("No")