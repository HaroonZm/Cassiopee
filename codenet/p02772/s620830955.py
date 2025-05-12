N = int(input())
A = list(map(int,input().split()))
flag = 0
for i in A:
    if i%2==0:
        if i%5!=0 and i%3!=0:
            flag = 1
            break
if flag==0:
    print('APPROVED')
else:
    print('DENIED')