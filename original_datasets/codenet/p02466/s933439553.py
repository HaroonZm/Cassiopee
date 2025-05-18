n = int(input())
alist = list(map(int, input().split()))
m = int(input())
blist = list(map(int, input().split()))

anslist = set(alist) ^ set(blist)
anslist = list(anslist)
anslist.sort()

for ans in anslist:
    print(ans)