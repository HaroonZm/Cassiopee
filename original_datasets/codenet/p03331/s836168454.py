n = int(input())
if n%10==0:
  print(10)
else:
  ans = [char for char in str(n)]
  for i in range(0, len(ans)): 
    ans[i] = int(ans[i]) 
  print(sum(ans))