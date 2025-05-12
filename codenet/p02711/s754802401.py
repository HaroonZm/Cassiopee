N = input()
flag = 0
for i in N:
    if i == '7':
        flag = 1
        print('Yes')
        break
if flag == 0:
    print('No')