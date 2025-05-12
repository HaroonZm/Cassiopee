list=input()
list=list.split()
list=[int(i) for i in list]
A=list[0]
B=list[1]
C=list[2]
Sum=A
flag=True
rem=A%B
while Sum%B!=C:
    Sum+=A
    if Sum%B==rem:
        flag=False
        break
if flag:
    print('YES')
else:
    print('NO')