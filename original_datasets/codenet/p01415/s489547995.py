n,k,t,u,v,l = map(int,input().split())
D = []
for i in range(n):
    d = int(input())
    D.append(d)
A = [0]*l
special = 0
nomal = 0
ninzin = 0

for i in range(l):
    if i == special:
        if ninzin == 0:
            nomal = 0
        else:
            special = i + v*t
            ninzin = ninzin-1
    if i in D:
        if nomal != 0 and ninzin < k:
            ninzin += 1
        else:
            special = i + v*t
            nomal += 1
    if nomal != 0:
        A[i] = 1
print(A.count(0)/u + A.count(1)/v)