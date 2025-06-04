N = int(input())
A = list(map(int, input().split()))
C = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0}
j = 0
while j < N:
    a = A[j]
    if a < 400:
        C[0] = C[0] + 1
    elif a < 800:
        C[1] = C[1] + 1
    elif a < 1200:
        C[2] = C[2] + 1
    elif a < 1600:
        C[3] = C[3] + 1
    elif a < 2000:
        C[4] = C[4] + 1
    elif a < 2400:
        C[5] = C[5] + 1
    elif a < 2800:
        C[6] = C[6] + 1
    elif a < 3200:
        C[7] = C[7] + 1
    else:
        C[8] = C[8] + 1
    j = j + 1
cmin = 0
i = 0
while i < 8:
    if C[i] > 0:
        cmin = cmin + 1
    i = i + 1
cmax = cmin + C[8]
if cmin == 0:
    cmin = 1
print(cmin, cmax)