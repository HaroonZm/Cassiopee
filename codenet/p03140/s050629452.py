N = int(input())
A = input()
B = input()
C = input()
 
 
def cal_chenge_num(a, b, c):
    if a==b:
        if a==c:
            return 0
        else:
            return 1
    else:
        if a==c or b==c:
            return 1
        else:
            return 2
 
num = 0
for i in range(N):
    num += cal_chenge_num(A[i], B[i], C[i])
print(num)