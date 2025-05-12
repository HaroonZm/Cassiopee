def check(num,memo={}):
  if num==0:
    return 2
  elif num == 1:
    return 1
  elif num in memo:
    return memo[num]
  else:
    memo[num] = check(num-1,memo) + check(num-2,memo)
    return memo[num]

print(check(int(input())))