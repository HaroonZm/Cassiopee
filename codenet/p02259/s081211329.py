def bubble_sort(num_list):
    list_length = len(num_list)-1
    cnt = 0

    for i in range(list_length):
        for j in range(list_length,i,-1):
            if num_list[j] < num_list[j-1]:
                num_list[j],num_list[j-1] = num_list[j-1],num_list[j]
                cnt += 1
    return num_list,cnt

n = int(input())
num_list = list(map(int,input().split()))
ans_list,cnt = bubble_sort(num_list)
str_ans_list = [str(i) for i in ans_list]
print(' '.join(str_ans_list))
print(cnt)