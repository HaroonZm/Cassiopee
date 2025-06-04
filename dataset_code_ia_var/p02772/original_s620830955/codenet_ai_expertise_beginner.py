N = int(input())
A = input().split()
flag = 0
for i in range(N):
    num = int(A[i])
    if num % 2 == 0:
        if num % 3 != 0 and num % 5 != 0:
            flag = 1
            break
if flag == 0:
    print('APPROVED')
else:
    print('DENIED')