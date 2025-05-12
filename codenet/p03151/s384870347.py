n = int(input())
a_list = list(map(int,input().split()))
b_list = list(map(int,input().split()))
if sum(a_list)<sum(b_list):
    print(-1)
else:
    diff_list = [a_list[i]-b_list[i] for i in range(n)]
    posi_list=[]
    cnt,diff_sum = 0,0
    for diff in diff_list:
        if diff<0:
            cnt+=1
            diff_sum+=diff
        elif diff>0:
            posi_list.append(diff)
    diff_sum*=(-1)
    posi_list.sort(reverse=True)
    i,S=0,0
    while S<diff_sum:
        S+=posi_list[i]
        i+=1
    print(i+cnt)