s=str(input())
if len(s)<6 :
    print("INVALID")
else:
    num=0
    ABC=0
    abc=0
    for i in range(len(s)) :
        if ord(s[i])>=48 and ord(s[i])<=57:
            num+=1
        if ord(s[i])>=97 and ord(s[i])<=122:
            ABC+=1
        if ord(s[i])>=65 and ord(s[i])<=90:
            abc+=1
    if num==0 or ABC==0 or abc==0:
        print("INVALID")
    else :
        print("VALID")