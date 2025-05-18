while 1:
    try:
        n=int(input())
        ans=[]
        for i in range(10):
            if n>=2**(9-i):
                ans.append(2**(9-i))
                n-=2**(9-i)
        print(' '.join(map(str,ans[::-1])))
    except:break