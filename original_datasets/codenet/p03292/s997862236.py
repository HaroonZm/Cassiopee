num = list(map(int,input().split()))
num.sort()

ans = num[2]-num[0]

print(ans)