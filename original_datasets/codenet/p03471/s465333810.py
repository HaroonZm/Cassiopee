N,Y = map(int,input().split())
if Y-1000*N<0:
    a1 = -1
    a2 = -1
    a3 = -1
else:
    flag = 0
    for i in range((Y//1000-N)//9+1):
        if (Y//1000-N-9*i)%4==0:
            a1 = i
            a2 = (Y//1000-N-9*i)//4
            a3 = N-a1-a2
            if a1>=0 and a2>=0 and a3>=0:
                flag = 1
                break
    if flag==0:
        a1 = -1
        a2 = -1
        a3 = -1
print(a1,a2,a3)