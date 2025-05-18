n = int (input())
a_l = list(map(int,input().split()))

ans=max(a_l)-min(a_l)
print(ans)