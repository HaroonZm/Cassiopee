N = int(input())
A = list(map(int,input().split()))
C = {i:0 for i in range(9)}
for j in range(N):
    a = A[j]
    if a<400:
        C[0] += 1
    elif a<800:
        C[1] += 1
    elif a<1200:
        C[2] += 1
    elif a<1600:
        C[3] += 1
    elif a<2000:
        C[4] += 1
    elif a<2400:
        C[5] += 1
    elif a<2800:
        C[6] += 1
    elif a<3200:
        C[7] += 1
    else:
        C[8] += 1
cmin = 0
for i in range(8):
    if C[i]>0:
        cmin += 1
cmax = cmin+C[8]
if cmin ==0:
    cmin = 1
print(cmin,cmax)