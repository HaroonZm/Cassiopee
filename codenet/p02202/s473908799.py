n = int(input())
v = list(map(int,input().split()))
count = 0
ans = 0
s = -1
while count != n:
    ans -= s
    s -= 1
    count += 1
print(sum(v)-ans)