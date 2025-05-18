x = int(input())
def f(x):
  if x == 1:
    return 7
  else:
    return f(x-1) * 2 + 1
  
ans = f(x) - 1

print(ans)