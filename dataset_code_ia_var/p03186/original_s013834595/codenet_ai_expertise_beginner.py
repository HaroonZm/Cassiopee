A = int(input())
B = int(input())
C = int(input())

cure = A + B - C

if cure > -1:
    print(B + C)
else:
    print(B + C + cure + 1)