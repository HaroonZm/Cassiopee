s = str(input())
cou = 0
for i in range(len(s)-1):
  if s[i+1] != s[i]:
    cou += 1
print(cou)