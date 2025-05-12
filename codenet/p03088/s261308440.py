n = int(input())
l=[{} for i in range(2)]
mod = 10**9+7

def judge(s):
  t=list(s)
  if ''.join(t).find('AGC') != -1:
    return False
  t[0],t[1]=t[1],t[0]
  if ''.join(t).find('AGC') != -1:
    return False
  t[0],t[1]=t[1],t[0]
  t[1],t[2]=t[2],t[1]
  if ''.join(t).find('AGC') != -1:
    return False
  t[1],t[2]=t[2],t[1]
  t[2],t[3]=t[3],t[2]
  if ''.join(t).find('AGC') != -1:
    return False
  return True

l[1]['XXX']=1

for i in range(n):
  l[i%2].clear()
  for s in l[(i+1)%2]:
    for c in 'ACGT':
      l[i%2][s[1:]+c] = 0

  t = 0
  for s in l[(i+1)%2]:
    for c in 'ACGT':
      if judge(s+c):
        l[i%2][s[1:]+c] = (l[i%2][s[1:]+c]+l[(i+1)%2][s]) % mod
        t = (t + l[(i+1)%2][s]) % mod
print(t)