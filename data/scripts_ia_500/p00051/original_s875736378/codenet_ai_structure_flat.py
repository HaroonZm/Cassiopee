N=int(input())
for _ in range(N):
    num=list(map(int,input()))
    min_list=sorted(num,reverse=True)
    max_list=sorted(num)
    max_num=0
    min_num=0
    for i in range(len(num)):
        max_num+=max_list[i]*(10**i)
        min_num+=min_list[i]*(10**i)
    print(max_num-min_num)