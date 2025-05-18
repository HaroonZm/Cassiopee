import sys
S = input()
A = S[0]
B = S[1]
C = S[2]
D = S[3]
if int(A) + int(B) + int(C) + int(D) == 7:
    print(A + '+' + B + '+' + C + '+' + D + '=7')
    sys.exit()
if int(A) - int(B) + int(C) + int(D) == 7:
    print(A + '-' + B + '+' + C + '+' + D + '=7')
    sys.exit()
if int(A) + int(B) - int(C) + int(D) == 7:
    print(A + '+' + B + '-' + C + '+' + D + '=7')
    sys.exit()
if int(A) - int(B) - int(C) + int(D) == 7:
    print(A + '-' + B + '-' + C + '+' + D + '=7')
    sys.exit()
if int(A) + int(B) + int(C) - int(D) == 7:
    print(A + '+' + B + '+' + C + '-' + D + '=7')
    sys.exit()
if int(A) - int(B) + int(C) - int(D) == 7:
    print(A + '-' + B + '+' + C + '-' + D + '=7')
    sys.exit()
if int(A) + int(B) - int(C) - int(D) == 7:
    print(A + '+' + B + '-' + C + '-' + D + '=7')
    sys.exit()
if int(A) - int(B) - int(C) - int(D) == 7:
    print(A + '-' + B + '-' + C + '-' + D + '=7')
    sys.exit()