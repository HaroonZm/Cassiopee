n = int(input())
k = int(input())
ans = 1
count = 0
while count < n:
    if ans < k:
        ans = ans * 2
    else:
        ans = ans + k
    count = count + 1
print(ans)