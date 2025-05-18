N = int(input())
Alist = list(map(int, input().split()))
Blist = list(map(int, input().split()))
Clist = list(map(int, input().split()))
point = sum(Blist)
for i in range(0, N - 1):
    if Alist[i + 1] == Alist[i] + 1:
        point += Clist[Alist[i] - 1]

print(point)