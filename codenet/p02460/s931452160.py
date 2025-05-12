n=int(input())
dic={}
for i in range(n):
    q,*args=map(str,input().split())
    key=args[0]
    val=args[0]
    if q=="0":
        val=int(args[1])
        dic[key]=val
    elif q=="1":
        if key in dic.keys():
            print(dic[key])
        else:
            print(0)
    else:
        if key in dic:
            dic.pop(key)
        else :
            None