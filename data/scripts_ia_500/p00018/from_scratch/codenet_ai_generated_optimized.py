a,b,c,d,e=map(int,input().split())
nums=[a,b,c,d,e]
nums.sort(reverse=True)
print(*nums)