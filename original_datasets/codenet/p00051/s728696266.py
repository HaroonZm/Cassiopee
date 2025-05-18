n = int(input())
for i in range(n):
    Max_num = ""
    Min_num = ""
    n = str(input())
    Lis = list(map(str,n))
    Min_num_lis = sorted(Lis)
    Max_num_lis = sorted(Lis)[::-1]
    for j in range(8):
        Max_num = Max_num + Max_num_lis[j]
        Min_num = Min_num + Min_num_lis[j]
    sa = int(Max_num) - int(Min_num)
    print(sa)