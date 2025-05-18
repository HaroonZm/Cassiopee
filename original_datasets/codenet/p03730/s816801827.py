A, B, C = map(int,input().split())
list=[]
for i in range(B):
    list.append((i*A)%B)
if C in list:
    print('YES')
else:
    print('NO')