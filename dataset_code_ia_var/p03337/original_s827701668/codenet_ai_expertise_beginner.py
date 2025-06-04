A_B = input().split()
A = int(A_B[0])
B = int(A_B[1])

a = A + B
b = A - B
c = A * B

if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)