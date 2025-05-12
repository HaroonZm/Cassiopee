while 1:
    n=int(input())
    if n==0:break
    y=int(input())
    bank_list=[]
    max_m=0
    num_keep=0
    mo=0
    for i in range(n):
        bank_list.append(list(map(int,input().split())))
    for i in bank_list:
        if i[2]==1:
            mo=1+y*i[1]/100
        if i[2]==2:
            mo=(1+(i[1]/100))**y
        if mo>max_m:
            max_m=mo
            num_keep=i[0]
    print(num_keep)