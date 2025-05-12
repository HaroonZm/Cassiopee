alpha = 'qwertyuiopasdfghjklzxcvbnm'
s = input()
ans = 'yes'

for i in s:
  if i in alpha:
    alpha = alpha.replace(i , '')
  else:
    ans = 'no'
    break

print(ans)