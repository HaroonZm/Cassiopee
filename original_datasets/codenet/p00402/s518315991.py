N = int(input())
a = list(map(int,input().split()))
if (max(a)-min(a))%2 == 0:
    print((max(a)-min(a))//2)
else:
    print(((max(a)-min(a))//2)+1)