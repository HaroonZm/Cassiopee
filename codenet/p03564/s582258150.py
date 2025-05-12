n = int(input())
k = int(input())
ans = 1
count = 0
while count < n:
  if ans < k:
    ans *= 2
  else:
    ans += k
  count += 1  
print(ans)