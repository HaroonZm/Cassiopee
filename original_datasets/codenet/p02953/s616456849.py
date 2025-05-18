N = int(input())
H = list(map(int, input().split(' ')))

if N == 1:
    print('Yes')
else:
    for i in range(1, N):
        if H[i - 1] < H[i]:
            H[i] -= 1

    no_flag = 0
    for i in range(1, N):
        if H[i - 1] > H[i]:
            no_flag = 1
    if no_flag == 0:
        print('Yes')
    else:
        print('No')
    #print(H)