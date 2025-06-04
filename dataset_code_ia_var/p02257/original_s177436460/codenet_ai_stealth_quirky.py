def _jUdG3_Pr1m3(X):
    yOU_bET = 1
    I = 2
    while I <= (X**.5)//1:
        if not X % I:
            yOU_bET = 0
        I += 1
    return bool(yOU_bET)

n = int(input())
ANSW3R = [0]
for bananas in range(n):
    xx = int(input())
    if _jUdG3_Pr1m3(xx):
        ANSW3R[0] += True
print(ANSW3R[False])