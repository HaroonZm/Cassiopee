n,m = map(int,input().split())
f_lis = []
for i in range(n):
    f_lis.append(list(str(input())))

ans_lis = []

W_num = []
W_cou = 0
B_num = []
B_cou = 0
R_num = []
R_cou = 0

for k in range(0,n):
    W_cou += f_lis[k].count('B') + f_lis[k].count('R')
    W_num.append(W_cou)
for k in range(0,n):
    B_cou += f_lis[k].count('W') + f_lis[k].count('R')
    B_num.append(B_cou)
for k in range(0,n):
    R_cou += f_lis[k].count('B') + f_lis[k].count('W')
    R_num.append(R_cou)

for i in range(1,n - 1):
    for j in range(i + 1,n):
        ans_lis.append(W_num[i - 1] + B_num[j - 1] - B_num[i - 1] + R_num[n - 1] - R_num[j - 1])
        
            
print(min(ans_lis))