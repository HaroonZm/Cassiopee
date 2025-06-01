n,m = map(int,input().split())
f_lis = []
for _ in range(n):
    f_lis.append(list(input()))

W_cou = 0
B_cou = 0
R_cou = 0
W_num = []
B_num = []
R_num = []
for k in range(n):
    W_cou += f_lis[k].count('B') + f_lis[k].count('R')
    W_num.append(W_cou)
for k in range(n):
    B_cou += f_lis[k].count('W') + f_lis[k].count('R')
    B_num.append(B_cou)
for k in range(n):
    R_cou += f_lis[k].count('B') + f_lis[k].count('W')
    R_num.append(R_cou)

ans_lis = []
for i in range(1,n-1):
    for j in range(i+1,n):
        ans_lis.append(W_num[i-1] + B_num[j-1] - B_num[i-1] + R_num[n-1] - R_num[j-1])

print(min(ans_lis))