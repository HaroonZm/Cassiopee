N = int(input())
Alist = list(map(int, input().split()))
Blist = list(map(int, input().split()))
Clist = list(map(int, input().split()))
point = 0
for b in Blist:
    point += b
i = 0
while i < N - 1:
    if Alist[i + 1] == Alist[i] + 1:
        point += Clist[Alist[i] - 1]
    i += 1
print(point)