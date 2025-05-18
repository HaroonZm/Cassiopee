def solve():
    n=int(input())
    x=list(map(int,input().split()))
    list1=[]
    def ap1(num):
        list1.append(num)
    for i in range(n):
        ap1([x[i],i+1])
    str1= lambda val: val[0]
    list1.sort(key=str1)
    numa=[]
    numb=[]
    for i in range(n):
        num3=list1[i][1]
        numa+=[num3]*(num3-1)
        numb+=[num3]*(n-num3)
    count1=0
    count2=0
    count3=0
    ans=[]
    ansnum=0
    def countnum(num):
        return ans.count(num)
    def apans(num):
        ans.append(num)
    for i in range(n*n):
        yn=0
        if count1!=n:
            if i==list1[count1][0]-1:
                if countnum(list1[count1][1])!=list1[count1][1]-1:
                    ansnum=1
                    break
                apans(list1[count1][1])
                count1+=1
                yn=1
        if yn==0:
            if count2!=len(numa):
                apans(numa[count2])
                count2+=1
            elif count3!=len(numb):
                apans(numb[count3])
                count3+=1
            else:
                if i!=n*n-1:
                    ansnum=1
                    break
    if ansnum==1:
        print("No")
    else:
        print("Yes")
        print(*ans)
solve()