n = int(input())
for i in range(n):
    n = str(input())
    Lis = list(n)
    Min_num_lis = sorted(Lis)
    Max_num_lis = sorted(Lis, reverse=True)
    Max_num = ""
    Min_num = ""
    for j in range(8):
        Max_num += Max_num_lis[j]
        Min_num += Min_num_lis[j]
    sa = int(Max_num) - int(Min_num)
    print(sa)