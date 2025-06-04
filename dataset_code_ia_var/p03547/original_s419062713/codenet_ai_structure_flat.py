A_B = input().split()
A = A_B[0]
B = A_B[1]
if A > B:
    print('>')
else:
    if A == B:
        print('=')
    else:
        print('<')