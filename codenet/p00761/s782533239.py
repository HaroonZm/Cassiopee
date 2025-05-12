while 1:
    a,b=input().split()
    b=int(b)
    if b==0:
        break
    a='0'*(b-len(a))+a
    dic={}
    i=0
    while 1:
        if a in dic:
            print(dic[a],int(a),i-dic[a])
            break
        else:
            dic[a]=i
        a=str(int(''.join(sorted(list(a),reverse=True)))-int(''.join(sorted(list(a)))))
        a='0'*(b-len(a))+a
        i+=1