import re
s = input()
pat = "(J*)(O*)(I*)"
ans = 0
for m in re.findall(pat, s):
 j = len(m[0])
 o = len(m[1])
 i = len(m[2])
 if j >= o and i >= o:
  if o > ans:
   ans = o
print(ans)